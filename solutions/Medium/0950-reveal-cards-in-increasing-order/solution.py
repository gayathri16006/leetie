# ──────────────────────────────────────────────────
# Problem  : 950. Reveal Cards In Increasing Order
# Difficulty: Medium
# Tags     : Array, Queue, Sorting, Simulation
# Link     : https://leetcode.com/problems/reveal-cards-in-increasing-order/
# Runtime  : 4 ms (beats 32%)
# Memory   : 12564000 (beats 53%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        deck.sort()
        
        # Queue storing the indices of the resulting array
        index_queue = deque(range(n))
        res = [0] * n
        
        for card in deck:
            # Reveal the card at the top index
            res[index_queue.popleft()] = card
           
            if index_queue:
                index_queue.append(index_queue.popleft())
                
        return res