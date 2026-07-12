class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        count = 0
        for n in nums:
            res[n] += 1
        out = list(res.items())
        out.sort(key = lambda x : x[1],reverse = True)
        output = []
        for i in range(k):
            output.append(out[i][0])
        return output

        




        
        