# ──────────────────────────────────────────────────
# Problem  : 943. Find the Shortest Superstring
# Difficulty: Hard
# Tags     : Array, String, Dynamic Programming, Bit Manipulation, Bitmask, Hamiltonian Path
# Link     : https://leetcode.com/problems/find-the-shortest-superstring/
# Runtime  : 423 ms (beats 96%)
# Memory   : 13836000 (beats 85%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        
        # Precompute the overlap between all pairs (words[i] followed by words[j])
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    m = min(len(words[i]), len(words[j]))
                    for k in range(m, 0, -1):
                        if words[i][-k:] == words[j][:k]:
                            overlap[i][j] = k
                            break
        
        # dp[mask][i] = max total overlap ending at word i with visited set = mask
        dp = [[-1] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        
        for i in range(n):
            dp[1 << i][i] = 0
            
        for mask in range(1 << n):
            for i in range(n):
                if dp[mask][i] == -1:
                    continue
                for j in range(n):
                    if not (mask & (1 << j)):
                        next_mask = mask | (1 << j)
                        val = dp[mask][i] + overlap[i][j]
                        if val > dp[next_mask][j]:
                            dp[next_mask][j] = val
                            parent[next_mask][j] = i
                            
        # Find the ending word with the maximum overlap for the full mask
        last = 0
        full_mask = (1 << n) - 1
        for i in range(1, n):
            if dp[full_mask][i] > dp[full_mask][last]:
                last = i
                
        # Reconstruct the optimal path
        path = []
        curr_mask = full_mask
        curr = last
        while curr != -1:
            path.append(curr)
            prev = parent[curr_mask][curr]
            curr_mask ^= (1 << curr)
            curr = prev
            
        path.reverse()
        
        # Build the final superstring
        res = [words[path[0]]]
        for i in range(1, len(path)):
            u, v = path[i - 1], path[i]
            k = overlap[u][v]
            res.append(words[v][k:])
            
        return "".join(res)