# ──────────────────────────────────────────────────
# Problem  : 833. Find And Replace in String
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Sorting
# Link     : https://leetcode.com/problems/find-and-replace-in-string/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12480000 (beats 34%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def findReplaceString(self, s, indices, sources, targets):
    """
    :type s: str
    :type indices: List[int]
    :type sources: List[str]
    :type targets: List[str]
    :rtype: str
    """
    lookup = {}
    for idx, src, tgt in zip(indices, sources, targets):
      if s.startswith(src, idx):
        lookup[idx] = (src, tgt)

    res = []
    i = 0
    n = len(s)

    while i < n:
      if i in lookup:
        src, tgt = lookup[i]
        res.append(tgt)
        i += len(src)
      else:
        res.append(s[i])
        i += 1

    return "".join(res)