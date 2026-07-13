class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lis in matrix:
            if lis[-1] < target:
                continue
            else:
                l ,r = 0,len(lis) - 1
                while l <=r:
                    m = (l + r)//2
                    if lis[m] < target:
                        l = m + 1
                    elif lis[m] > target:
                        r = m -1
                    else:
                        return True
        return False

        