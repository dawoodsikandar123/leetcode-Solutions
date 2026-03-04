"""
LeetCode 14: Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Strategy:
Sort the array alphabetically, after sorting, the most "different" strings
move to the two ends of the array. So the longest common prefix of the entire
array must also be the common prefix between the first and last string.

Compare characters of first and last string one by one; stop at first mismatch.

Time Complexity: O(N log N + M)
  - O(N log N) for sorting the array (N = number of strings)
  - O(M) for the character comparison loop (M = length of shortest string)
  
Space Complexity: O(1)
  - Only a few variables used, prefix string grows up to M chars (output space)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()              # Sort list alphabetically

        if not strs:             # Edge case: empty list
            return ""

        prefix = ""
        first_word = strs[0]            # Smallest string
        last_word  = strs[-1]           # Largest string

        for i in range(len(first_word)):          # Iterate over first string beacuase we compare smallest and largest string
            if first_word[i] == last_word[i]:     # Characters match
                prefix += first_word[i]           # Add to prefix reference variable
            
            else:
                break          # Mismatch, so stop the loop with break

        return prefix
