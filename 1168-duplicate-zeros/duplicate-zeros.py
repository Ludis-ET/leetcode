class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        tmp = []
        i = 0
        for val in arr:
            tmp.append([i, val])
            if val == 0:
                i += 1
                tmp.append([i, 0])
            i += 1
            
        for t in range(len(arr)):
            i, v = tmp[t]
            arr[i] = v