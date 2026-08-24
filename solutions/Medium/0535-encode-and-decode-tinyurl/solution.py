# ──────────────────────────────────────────────────
# Problem  : 535. Encode and Decode TinyURL
# Difficulty: Medium
# Tags     : Hash Table, String, Design, Hash Function
# Link     : https://leetcode.com/problems/encode-and-decode-tinyurl/
# Runtime  : 26 ms (beats 0%)
# Memory   : 12332000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random
import string

class Codec:

    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits
        self.base_url = "http://tinyurl.com/"
        self.long_to_short = {}
        self.short_to_long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long_to_short:
            return self.base_url + self.long_to_short[longUrl]
        
        while True:
            # Generate a 6-character random token
            key = "".join(random.choice(self.alphabet) for _ in range(6))
            if key not in self.short_to_long:
                break
                
        self.long_to_short[longUrl] = key
        self.short_to_long[key] = longUrl
        return self.base_url + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        # Extract the 6-character key from the end
        key = shortUrl.replace(self.base_url, "")
        return self.short_to_long.get(key, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))