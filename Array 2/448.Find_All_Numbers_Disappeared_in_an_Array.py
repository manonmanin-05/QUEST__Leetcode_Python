class Solution(object):
    def findDisappearedNumbers(self, nums):
        output=[]
        n=list(range(1,len(nums)+1))
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for y in n:
            if y not in freq:
                output.append(y)
        return output
