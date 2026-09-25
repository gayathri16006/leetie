// ──────────────────────────────────────────────────
// Problem  : 1096. Brace Expansion II
// Difficulty: Hard
// Tags     : Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting
// Link     : https://leetcode.com/problems/brace-expansion-ii/
// Runtime  : 11 ms (beats 47%)
// Memory   : 47136000 (beats 64%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.*;

class Solution {
    public List<String> braceExpansionII(String expression) {
        Deque<Object> stack = new ArrayDeque<>();
        
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);
            
            if (c == '{') {
                stack.push(c);
            } else if (c == ',') {
                stack.push(c);
            } else if (c == '}') {
                // Pop and union everything until the matching '{'
                List<TreeSet<String>> toUnion = new ArrayList<>();
                while (!stack.isEmpty() && !(stack.peek() instanceof Character && (char) stack.peek() == '{')) {
                    Object top = stack.pop();
                    if (top instanceof TreeSet) {
                        toUnion.add((TreeSet<String>) top);
                    }
                    // Commas are simply discarded
                }
                stack.pop(); // Pop '{'
                
                TreeSet<String> unionSet = new TreeSet<>();
                for (TreeSet<String> s : toUnion) {
                    unionSet.addAll(s);
                }
                
                // Concatenate with previous adjacent set if not preceded by ',' or '{'
                pushAndConcatenate(stack, unionSet);
            } else {
                // Character literal
                StringBuilder sb = new StringBuilder();
                while (i < expression.length() && Character.isLowerCase(expression.charAt(i))) {
                    sb.append(expression.charAt(i++));
                }
                i--; // Step back after loop
                
                TreeSet<String> set = new TreeSet<>();
                set.add(sb.toString());
                
                pushAndConcatenate(stack, set);
            }
        }
        
        // Final union of remaining sets on the stack (separated by commas)
        TreeSet<String> result = new TreeSet<>();
        while (!stack.isEmpty()) {
            Object obj = stack.pop();
            if (obj instanceof TreeSet) {
                result.addAll((TreeSet<String>) obj);
            }
        }
        
        return new ArrayList<>(result);
    }
    
    private void pushAndConcatenate(Deque<Object> stack, TreeSet<String> current) {
        // If the top element on stack is another set (implicit concatenation), multiply them
        while (!stack.isEmpty() && stack.peek() instanceof TreeSet) {
            TreeSet<String> prev = (TreeSet<String>) stack.pop();
            TreeSet<String> product = new TreeSet<>();
            for (String a : prev) {
                for (String b : current) {
                    product.add(a + b);
                }
            }
            current = product;
        }
        stack.push(current);
    }
}