class Solution(object):
    def findAnagrams(self, s, p):
        """
        LeetCode: 438. Find All Anagrams in a String
        Pattern: Fixed-size sliding window with frequency matching

        Goal: Return starting indices of p's anagrams in s.

        Approach:
        - Maintain counts for p (need) and a window of length len(p) over s (win).
        - Track how many characters currently match exactly between need and win (matches).
        - Slide the window one step at a time, updating counts and matches in O(1).

        Time:  O(n) where n = len(s)
        Space: O(Σ) with Σ = 26 lowercase letters

        Examples:
          - s="cbaebabacd", p="abc" -> [0, 6]
          - s="abab", p="ab" -> [0, 1, 2]
        """
        n, m = len(p), len(s)
        if m < n:
            return []

        base = ord('a')
        need = [0] * 26           # counts for p
        win  = [0] * 26           # counts for current window in s

        # build target counts and initial window counts
        for ch in p:
            need[ord(ch) - base] += 1
        for ch in s[:n]:
            win[ord(ch) - base] += 1

        # how many letters match exactly between need and win
        matches = sum(1 for i in range(26) if need[i] == win[i])

        res = []
        if matches == 26:
            res.append(0)

        def bump(idx, delta):
            # update one letter in the window and keep matches correct
            nonlocal matches
            if win[idx] == need[idx]:
                matches -= 1
            win[idx] += delta
            if win[idx] == need[idx]:
                matches += 1

        # slide the fixed-size window one step at a time
        for r in range(n, m):
            in_idx  = ord(s[r]) - base        # incoming (right edge)
            out_idx = ord(s[r - n]) - base    # outgoing (left edge)
            bump(in_idx, +1)
            bump(out_idx, -1)
            if matches == 26:
                res.append(r - n + 1)

        return res