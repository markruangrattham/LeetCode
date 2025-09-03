import sys

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        LeetCode: 209. Minimum Size Subarray Sum
        Pattern: Sliding Window on positive integers

        Goal: Find the minimal length of a contiguous subarray of which the sum is >= target.

        Invariant: The window nums[left..i] always has sum stored in window_sum.
        - We expand the right end to increase the sum.
        - While the sum is >= target, we contract from the left to find the minimal window ending at i.

        Time:  O(n) — each index enters/leaves the window at most once
        Space: O(1) — constant extra space

        Examples:
          - target=7, nums=[2,3,1,2,4,3] -> 2   (subarray [4,3])
          - target=4, nums=[1,4,4] -> 1   ([4])
          - target=11, nums=[1,1,1,1,1,1,1,1] -> 0   (no such subarray)
        """
        # Sliding window: expand right to increase sum, shrink left to keep it minimal
        window_sum = 0
        left = 0
        # Initialize answer to a large value; will store minimal window length
        ans = sys.maxsize
        for i, num in enumerate(nums):
            # Expand window by including nums[i]
            window_sum += num
            # While the current window satisfies the target, try shrinking from the left
            while window_sum >= target:
                # Update minimal length
                ans = min(ans, i - left + 1)
                # Shrink from the left and update the running sum
                window_sum -= nums[left]
                left += 1
        # If not updated, no valid subarray was found
        if ans == sys.maxsize:
            return 0
        return ans
        