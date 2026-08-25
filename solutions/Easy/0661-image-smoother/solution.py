# ──────────────────────────────────────────────────
# Problem  : 661. Image Smoother
# Difficulty: Easy
# Tags     : Array, Matrix
# Link     : https://leetcode.com/problems/image-smoother/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19432000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                total_sum = 0
                count = 0
                
                # Check the 3x3 surrounding window
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            total_sum += img[nr][nc]
                            count += 1
                            
                res[r][c] = total_sum // count
                
        return res