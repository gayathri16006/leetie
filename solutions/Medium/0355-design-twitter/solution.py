# ──────────────────────────────────────────────────
# Problem  : 355. Design Twitter
# Difficulty: Medium
# Tags     : Hash Table, Linked List, Design, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/design-twitter/
# Runtime  : 21 ms (beats 56%)
# Memory   : 21384000 (beats 95%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    # userId -> list of (-time, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time += 1
        # Store with negative timestamp for min-heap extraction
        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        # Include tweets from the user themselves plus everyone they follow
        users = self.following[userId] | {userId}
        
        # Push the most recent tweet from each relevant user into the heap
        for u in users:
            if self.tweets[u]:
                last_idx = len(self.tweets[u]) - 1
                time, tweet_id = self.tweets[u][last_idx]
                # (timestamp, tweet_id, user_id, next_index_to_check)
                heap.append((time, tweet_id, u, last_idx - 1))
        
        heapq.heapify(heap)
        feed = []
        
        # Extract up to 10 most recent tweets across all followed users
        while heap and len(feed) < 10:
            time, tweet_id, u, next_idx = heapq.heappop(heap)
            feed.append(tweet_id)
            if next_idx >= 0:
                next_time, next_tweet_id = self.tweets[u][next_idx]
                heapq.heappush(heap, (next_time, next_tweet_id, u, next_idx - 1))
                
        return feed

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.following[followerId].discard(followeeId)