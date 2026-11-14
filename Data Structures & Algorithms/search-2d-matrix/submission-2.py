class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) -1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target not in matrix[mid] and target > matrix[mid][0]:
                top = mid + 1

            elif target not in matrix[mid] and target < matrix[mid][0]:
                bottom = mid - 1

            else:
                return True

        return False