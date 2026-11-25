class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                low = 0
                high = len(matrix[row])
                while low <= high:
                    mid = low + (high - low) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        low = mid + 1
                    elif matrix[row][mid] > target:
                        high = mid - 1
                return False
        return False