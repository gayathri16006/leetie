# ──────────────────────────────────────────────────
# Problem  : 220. Contains Duplicate III
# Difficulty: Hard
# Tags     : Array, Sliding Window, Sorting, Bucket Sort, Ordered Set
# Link     : https://leetcode.com/problems/contains-duplicate-iii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12248000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if indexDiff <= 0 or valueDiff < 0:
            return False

        # Bucket width is valueDiff + 1 so values with difference <= valueDiff fall in the same or adjacent buckets
        bucket_width = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket_id = num // bucket_width

            # 1. Check if same bucket already contains a number
            if bucket_id in buckets:
                return True

            # 2. Check adjacent left bucket
            if (
                bucket_id - 1 in buckets
                and abs(num - buckets[bucket_id - 1]) <= valueDiff
            ):
                return True

            # 3. Check adjacent right bucket
            if (
                bucket_id + 1 in buckets
                and abs(num - buckets[bucket_id + 1]) <= valueDiff
            ):
                return True

            # Store current number in its bucket
            buckets[bucket_id] = num

            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_width
                del buckets[old_bucket_id]

        return False