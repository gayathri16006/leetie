# ──────────────────────────────────────────────────
# Problem  : 587. Erect the Fence
# Difficulty: Hard
# Tags     : Array, Math, Geometry, Convex Hull, Polygons
# Link     : https://leetcode.com/problems/erect-the-fence/
# Runtime  : 57 ms (beats 26%)
# Memory   : 12748000 (beats 60%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        def cross_product(p, q, r):
            # 2D cross product of vector (q - p) and (r - p)
            # > 0: counter-clockwise turn
            # < 0: clockwise turn
            # = 0: collinear
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        
        # Sort points primarily by x, secondarily by y
        trees = sorted(trees, key=lambda p: (p[0], p[1]))
        
        if len(trees) <= 3:
            return trees

        # Build lower hull
        lower = []
        for p in trees:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(tuple(p))

        # Build upper hull
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(tuple(p))

        # Combine both hulls and eliminate duplicates
        return [list(p) for p in set(lower + upper)]