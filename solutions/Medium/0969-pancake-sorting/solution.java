// ──────────────────────────────────────────────────
// Problem  : 969. Pancake Sorting
// Difficulty: Medium
// Tags     : Array, Two Pointers, Greedy, Sorting
// Link     : https://leetcode.com/problems/pancake-sorting/
// Runtime  : 1 ms (beats 100%)
// Memory   : 43928000 (beats 70%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        List<Integer> result = new ArrayList<>();
        
        for (int valueToPlace = arr.length; valueToPlace > 0; valueToPlace--) {
            // Find the index of the current target value
            int index = find(arr, valueToPlace);
            
            // Already in the correct position
            if (index == valueToPlace - 1) {
                continue;
            }
            
            // If it's not at the front, flip it to the front
            if (index != 0) {
                result.add(index + 1);
                reverse(arr, index + 1);
            }
            
            // Flip it to its target position
            result.add(valueToPlace);
            reverse(arr, valueToPlace);
        }
        
        return result;
    }
    
    private int find(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }
    
    private void reverse(int[] arr, int k) {
        int left = 0;
        int right = k - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}