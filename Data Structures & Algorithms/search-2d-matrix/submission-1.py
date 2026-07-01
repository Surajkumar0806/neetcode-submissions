class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bottom=len(matrix)-1
        while top<=bottom:
            row=top+(bottom-top)//2
            if target<matrix[row][0]:
                bottom= row-1
            elif target>matrix[row][-1]:
                top= row+1
            else:
                low=0
                high=len(matrix[row])-1
                while low<=high:
                    mid=low+(high-low)//2
                    if target==matrix[row][mid]:
                        return True
                    elif target<matrix[row][mid]:
                        high=mid-1
                    elif target>matrix[row][mid]:
                        low=mid+1
                return False
        return False
