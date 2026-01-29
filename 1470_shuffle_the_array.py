class Solution(object):
    def shuffle(self, nums, n):
        first = nums[:n]
        second = nums[n:]
        result = []

        for i in range(n):
            result += [first[i], second[i]]

        return result
