# ──────────────────────────────────────────────────
# Problem  : 636. Exclusive Time of Functions
# Difficulty: Medium
# Tags     : Array, Stack
# Link     : https://leetcode.com/problems/exclusive-time-of-functions/
# Runtime  : 7 ms (beats 61%)
# Memory   : 19548000 (beats 7%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn_id_str, event_type, time_str = log.split(":")
            fn_id = int(fn_id_str)
            timestamp = int(time_str)
            
            if event_type == "start":
                if stack:
                    # Credit elapsed time to the currently running function
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                # "end" event is inclusive, so add 1
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
                
        return res