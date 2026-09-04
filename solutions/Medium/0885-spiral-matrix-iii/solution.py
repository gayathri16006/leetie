# ──────────────────────────────────────────────────
# Problem  : 885. Spiral Matrix III
# Difficulty: Medium
# Tags     : Array, Matrix, Simulation
# Link     : https://leetcode.com/problems/spiral-matrix-iii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12376000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        # East, South, West, North
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        total_cells = rows * cols
        ans = [[rStart, cStart]]
        
        r, c = rStart, cStart
        step_len = 1
        d = 0
        
        while len(ans) < total_cells:
            # Each step length is repeated for two consecutive directions
            for _ in range(2):
                dr, dc = directions[d]
                for _ in range(step_len):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                        if len(ans) == total_cells:
                            return ans
                
                # Turn right (next direction)
                d = (d + 1) % 4
            
            # Increase step length after two directions
            step_len += 1

        return ans