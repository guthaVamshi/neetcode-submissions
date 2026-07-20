class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for c in s1:
            map1[c] += 1
        l = 0
        r = len(s1)
        while l < len(s2):
            for i in range(l , min(r, len(s2))):
                map2[s2[i]] += 1
            if map1 == map2:
                return True
            l += 1
            r += 1
            map2.clear()

        return False

            


            



            
            



        
        