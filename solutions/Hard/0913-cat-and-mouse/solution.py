# ──────────────────────────────────────────────────
# Problem  : 913. Cat and Mouse
# Difficulty: Hard
# Tags     : Math, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Minimax, Game Theory, Zero-Sum Game
# Link     : https://leetcode.com/problems/cat-and-mouse/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12612000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2
        
        # color[m][c][turn] will store the outcome: 0: DRAW, 1: MOUSE, 2: CAT
        color = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        # degree[m][c][turn] counts the number of available moves for current player
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len([nxt for nxt in graph[c] if nxt != 0])
                
        queue = deque()
        
        # Base terminal states:
        for c in range(1, n):
            # Mouse is at the hole (0) -> Mouse wins
            for turn in (0, 1):
                color[0][c][turn] = MOUSE
                queue.append((0, c, turn, MOUSE))
                
            # Cat catches Mouse (m == c, m != 0) -> Cat wins
            for turn in (0, 1):
                color[c][c][turn] = CAT
                queue.append((c, c, turn, CAT))
                
        # Bottom-up Minimax via Topological Sort / BFS
        while queue:
            m, c, turn, result = queue.popleft()
            
            # Find all previous states that can transition to (m, c, turn)
            prev_turn = 1 - turn
            if prev_turn == 0:
                # Previous move was made by Mouse
                prev_states = [(prev_m, c) for prev_m in graph[m]]
            else:
                # Previous move was made by Cat (Cat cannot move to 0)
                prev_states = [(m, prev_c) for prev_c in graph[c] if prev_c != 0]
                
            for prev_m, prev_c in prev_states:
                if color[prev_m][prev_c][prev_turn] != DRAW:
                    continue
                
                # If current result is an immediate win for the player whose turn it was
                winning_player = MOUSE if prev_turn == 0 else CAT
                if result == winning_player:
                    color[prev_m][prev_c][prev_turn] = result
                    queue.append((prev_m, prev_c, prev_turn, result))
                else:
                    # Otherwise, decrement the degree of neutral moves
                    degree[prev_m][prev_c][prev_turn] -= 1
                    if degree[prev_m][prev_c][prev_turn] == 0:
                        
                        losing_result = CAT if prev_turn == 0 else MOUSE
                        color[prev_m][prev_c][prev_turn] = losing_result
                        queue.append((prev_m, prev_c, prev_turn, losing_result))
                        
        return color[1][2][0]