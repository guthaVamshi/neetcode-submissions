class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in matrix:
            nl , nr = 0 , len(n) - 1
            if target <= n[nr]:
                l , r = 0,len(n)-1
                m = ( l + r) //2
                while l <= r:
                    m = (l + r) // 2
                    if n[m] < target:
                        l = m + 1
                    elif n[m] > target:
                        r = m -1
                    else:
                        return True
            else:
                continue
        return False
        