def longest_sub_no_repeat(s: str) -> int:
    """
    LeetCode: Longest Substring Without Repeating Characters
    Pattern: Sliding Window with last-seen index map

    Invariant: the window s[left..i] always has all unique characters.
    When we see a duplicate char that's still inside the window, we move
    'left' just past its previous occurrence to restore the invariant.

    Time:  O(n)  — each index enters/leaves the window at most once
    Space: O(min(n, Σ)) — map of last-seen positions (Σ = alphabet size)

    Examples:
      - "abba" -> 2   ("ab" or "ba")
      - "abcabcbb" -> 3  ("abc")
      - "bbbbb" -> 1  ("b")
    """
    last = {}               # char -> last index where it was seen
    left = result = 0       # left = start of current window; result = best length found

    for i, x in enumerate(s):
        # If we've seen x and its last occurrence lies inside the current window,
        # shrink the window start to just past that old occurrence.
        if x in last and last[x] >= left:
            left = last[x] + 1

        # Update last-seen position of x to the current index.
        last[x] = i

        # Window length is i - left + 1; update the best.
        result = max(result, i - left + 1)

    return result