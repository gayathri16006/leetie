# ──────────────────────────────────────────────────
# Problem  : 134. Gas Station
# Difficulty: Medium
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/gas-station/
# Runtime  : 27 ms (beats 54%)
# Memory   : 18080000 (beats 28%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # If total gas is less than total cost, completing the circuit is impossible
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        current_tank = 0
        starting_station = 0
        
        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            current_tank += net_gain
            
            # If current tank goes negative, reset start to next station
            if current_tank < 0:
                starting_station = i + 1
                current_tank = 0
                
        return starting_station