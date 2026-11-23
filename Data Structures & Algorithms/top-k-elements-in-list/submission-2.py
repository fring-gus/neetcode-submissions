class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        
        freq=dict(sorted(freq.items(),key=lambda item: item[1],reverse=True))
        new_list=[x for x,y in freq.items()]
        return new_list[0:k]
