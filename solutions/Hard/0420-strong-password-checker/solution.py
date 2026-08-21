# ──────────────────────────────────────────────────
# Problem  : 420. Strong Password Checker
# Difficulty: Hard
# Tags     : String, Greedy, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/strong-password-checker/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12332000 (beats 59%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        n = len(password)

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)

        missing_types = (
            (0 if has_lower else 1)
            + (0 if has_upper else 1)
            + (0 if has_digit else 1)
        )

        # Count consecutive repeating characters
        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                repeats.append(length)
            else:
                i += 1

        # Case 1: Length < 6
        if n < 6:
            return max(6 - n, missing_types)

        # Case 2: Length 6 to 20
        elif n <= 20:
            replace_count = sum(length // 3 for length in repeats)
            return max(replace_count, missing_types)

        # Case 3: Length > 20
        else:
            deletions_needed = n - 20
            d = deletions_needed

            # Prioritize deleting from repeat sequences where mod 3 == 0 (1 deletion saves 1 replacement)
            for k in range(len(repeats)):
                if d > 0 and repeats[k] % 3 == 0:
                    repeats[k] -= 1
                    d -= 1

            # Prioritize deleting from repeat sequences where mod 3 == 1 (2 deletions save 1 replacement)
            for k in range(len(repeats)):
                if d > 1 and repeats[k] % 3 == 1:
                    repeats[k] -= 2
                    d -= 2

            # Use remaining deletions on larger sequences (3 deletions save 1 replacement)
            for k in range(len(repeats)):
                if d > 0 and repeats[k] >= 3:
                    reduce_by = min(d, repeats[k] - 2)
                    repeats[k] -= reduce_by
                    d -= reduce_by

            replace_count = sum(length // 3 for length in repeats if length >= 3)
            return deletions_needed + max(replace_count, missing_types)