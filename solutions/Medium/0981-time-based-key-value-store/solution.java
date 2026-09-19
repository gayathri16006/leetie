// ──────────────────────────────────────────────────
// Problem  : 981. Time Based Key-Value Store
// Difficulty: Medium
// Tags     : Hash Table, String, Binary Search, Design
// Link     : https://leetcode.com/problems/time-based-key-value-store/
// Runtime  : 3 ms (beats 0%)
// Memory   : 42976000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.*;

class TimeMap {

    private static class Entry {
        int timestamp;
        String value;

        Entry(int timestamp, String value) {
            this.timestamp = timestamp;
            this.value = value;
        }
    }

    private final Map<String, List<Entry>> map;

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(new Entry(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }

        List<Entry> list = map.get(key);
        int low = 0;
        int high = list.size() - 1;
        String result = "";

        // Binary search for the largest timestamp_prev <= timestamp
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (list.get(mid).timestamp <= timestamp) {
                result = list.get(mid).value;
                low = mid + 1; // Try to find a larger valid timestamp
            } else {
                high = mid - 1;
            }
        }

        return result;
    }
}