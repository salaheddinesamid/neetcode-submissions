class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen  = set()

        longest = ""
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            current = s[left: right + 1]
            if len(current) > len(longest):
                longest = current

        return len(longest)
