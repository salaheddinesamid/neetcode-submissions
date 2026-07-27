class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0

        for left in range(0, len(heights)):
            for right in range(left + 1, len(heights)):

                width = right - left
                height = min(heights[left], heights[right])

                area = width * height

                if area > max:
                    max = area

        return max

        
