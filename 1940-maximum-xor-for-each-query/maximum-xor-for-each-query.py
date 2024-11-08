class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(pre[-1] ^ nums[i])

        n = pow(2, maximumBit)
        for i in range(len(nums)):
            tmp, j = 0, 0
            while tmp | 1 << j < n:
                if (pre[i] & 1 << j) == 0:
                    tmp |= 1 << j
                j += 1
            pre[i] = tmp
        pre.reverse()
        return pre
    
                