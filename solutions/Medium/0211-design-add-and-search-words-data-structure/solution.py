# ──────────────────────────────────────────────────
# Problem  : 211. Design Add and Search Words Data Structure
# Difficulty: Medium
# Tags     : String, Depth-First Search, Design, Trie
# Link     : https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12452000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class TrieNode:

  def __init__(self):
    self.children = {}
    self.is_end_of_word = False


class WordDictionary(object):

  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    """
    :type word: str
    :rtype: None
    """
    node = self.root
    for char in word:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.is_end_of_word = True

  def search(self, word):
    """
    :type word: str
    :rtype: bool
    """

    def dfs(index, node):
      curr = node
      for i in range(index, len(word)):
        char = word[i]

        if char == ".":
          # If wildcard, explore all existing child branches
          for child in curr.children.values():
            if dfs(i + 1, child):
              return True
          return False
        else:
          if char not in curr.children:
            return False
          curr = curr.children[char]

      return curr.is_end_of_word

    return dfs(0, self.root)