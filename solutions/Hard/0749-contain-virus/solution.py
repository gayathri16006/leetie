# ──────────────────────────────────────────────────
# Problem  : 749. Contain Virus
# Difficulty: Hard
# Tags     : Array, Depth-First Search, Breadth-First Search, Matrix, Simulation
# Link     : https://leetcode.com/problems/contain-virus/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19332000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0

        def get_regions():
            visited = set()
            regions = []           # List of sets of infected cells
            uninfected_frontiers = []  # List of sets of uninfected neighbors
            walls_needed = []      # Walls needed to contain this region

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        region = set([(r, c)])
                        frontier = set()
                        walls = 0
                        
                        queue = [(r, c)]
                        visited.add((r, c))
                        
                        while queue:
                            cr, cc = queue.pop(0)
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = cr + dr, cc + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 1:
                                        if (nr, nc) not in visited:
                                            visited.add((nr, nc))
                                            region.add((nr, nc))
                                            queue.append((nr, nc))
                                    elif isInfected[nr][nc] == 0:
                                        walls += 1
                                        frontier.add((nr, nc))
                                        
                        regions.append(region)
                        uninfected_frontiers.append(frontier)
                        walls_needed.append(walls)
                        
            return regions, uninfected_frontiers, walls_needed

        while True:
            regions, frontiers, walls = get_regions()
            if not regions:
                break

            # Find the region that threatens the most uninfected cells
            max_threat_idx = -1
            max_threat_count = -1
            for i, frontier in enumerate(frontiers):
                if len(frontier) > max_threat_count:
                    max_threat_count = len(frontier)
                    max_threat_idx = i

            # If no uninfected cells are threatened, stop
            if max_threat_idx == -1 or max_threat_count == 0:
                break

            # Contain the most dangerous region with walls
            total_walls += walls[max_threat_idx]
            for r, c in regions[max_threat_idx]:
                isInfected[r][c] = -1  # Mark as permanently contained

            # Spread remaining uncontained regions
            for i in range(len(regions)):
                if i == max_threat_idx:
                    continue
                for r, c in frontiers[i]:
                    isInfected[r][c] = 1

        return total_walls