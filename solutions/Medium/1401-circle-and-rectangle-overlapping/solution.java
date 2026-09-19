// ──────────────────────────────────────────────────
// Problem  : 1401. Circle and Rectangle Overlapping
// Difficulty: Medium
// Tags     : Math, Geometry
// Link     : https://leetcode.com/problems/circle-and-rectangle-overlapping/
// Runtime  : 0 ms (beats 100%)
// Memory   : 42176000 (beats 61%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        // Find the point on the rectangle closest to the circle's center
        int closestX = Math.max(x1, Math.min(xCenter, x2));
        int closestY = Math.max(y1, Math.min(yCenter, y2));

        // Calculate the squared distance between the center and the closest point
        int dx = xCenter - closestX;
        int dy = yCenter - closestY;

        // If the squared distance is within the radius squared, they overlap
        return (dx * dx + dy * dy) <= (radius * radius);
    }
}