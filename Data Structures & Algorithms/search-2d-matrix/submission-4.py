class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = low + (high - low)//2
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                lower = 0
                higher = len(matrix[mid]) - 1
                while lower <= higher:
                    middle = lower + (higher - lower) // 2
                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] < target:
                        lower = middle + 1
                    elif matrix[mid][middle] > target:
                        higher = middle - 1
                return False
        return False
        

