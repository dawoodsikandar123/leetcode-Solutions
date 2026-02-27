"""
LeetCode 13: Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/

Strategy:
Iterate through the string and compare the current character's value with the next one.
If current < next, subtract it (e.g., IV = -1 + 5). Otherwise, add it.

Time Complexity: O(n) - where n is the length of the string.
Space Complexity: O(1) - constant space used for the dictionary.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        
        for i in range(len(s) - 1):
            # If current value is less than the next, we subtract it
            if roman_map[s[i]] < roman_map[s[i+1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        
        # Always add the last character
        result += roman_map[s[-1]]
        return result
