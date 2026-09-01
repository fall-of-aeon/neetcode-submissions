from sortedcontainers import SortedDict
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        freq=SortedDict()
        i=0
        ans=0
        for j in range(len(nums)):
            freq[nums[j]]=freq.get(nums[j],0)+1
            
            while freq.peekitem(-1)[0]-freq.peekitem(0)[0]>limit:
                freq[nums[i]]-=1
                if freq[nums[i]]==0:
                    del freq[nums[i]]
                i+=1
                
            ans=max(ans,j-i+1)
        return ans

                
        