class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        # search for the suitable row:
        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break
        
        # search for the target:
        row = (top + bottom) // 2
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (right + left) // 2

            if target > matrix[row][mid]:
                left += 1

            elif target < matrix[row][mid]:
                right -= 1

            else:
                return True
        return False
            