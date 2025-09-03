class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        LeetCode: 567. Permutation in String
        Pattern: Brute-force window with frequency counts (no code changes, comments only)

        Goal: Return True if any permutation of s1 is a substring of s2.

        Approach in this implementation:
        - Build a frequency map (counter) for s1.
        - Slide a window of size len(s1) across s2.
        - For each window, build its frequency map (temp) and compare with counter.
        - If for every character the counts in the window are sufficient, return True.
        - This is a brute-force approach and has a time complexity of O(n * k) where n = len(s2), k = len(s1), as we rebuild the frequency map for each window.
        - another appprach for this is we just keep removing feq from our first map and if we see that there is no freq remaining we can return true

        Time:  O(n * k) where n = len(s2), k = len(s1) (rebuilds temp per window)
        Space: O(Σ) for frequency maps
        """
        # Quick check (as written): compares len(s2) to itself; keeps original behavior intact
        if len(s2)>len(s2):
            return False 

        # Build frequency map for s1
        counter = {}
        left = 0
        for char in s1:
            if char not in counter:
                counter[char]=1
            else:
                counter[char]+=1

        # Slide a window of length len(s1) across s2
        for i in range(len(s1), len(s2)+1):
            temp = {}
            notbreak = True

            # Build frequency map for current window s2[left:i]
            for char in s2[left:i]:
                if char not in temp:
                    temp[char]=1
                else:
                    temp[char]+=1

            # Verify window frequencies meet or exceed those required by counter
            for x in counter:
                if x in temp:
                    if temp[x]>= counter[x]:
                        continue
                    else:
                        notbreak=False
                        break
                else:
                    notbreak = False
                    break

            # If all required counts satisfied, we found a permutation
            if notbreak:
                return True

            # Move the window forward by one
            left+=1

        # No permutation found in any window
        return False
                    

        
        
        


        