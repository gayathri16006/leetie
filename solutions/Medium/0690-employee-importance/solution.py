# ──────────────────────────────────────────────────
# Problem  : 690. Employee Importance
# Difficulty: Medium
# Tags     : Array, Hash Table, Tree, Depth-First Search, Breadth-First Search
# Link     : https://leetcode.com/problems/employee-importance/
# Runtime  : 52 ms (beats 0%)
# Memory   : 19724000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Map employee ID to the Employee object for O(1) lookup
        emp_map = {emp.id: emp for emp in employees}
        
        def dfs(emp_id: int) -> int:
            emp = emp_map[emp_id]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total
            
        return dfs(id)