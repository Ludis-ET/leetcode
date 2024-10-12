class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = defaultdict(set)
        n = len(parents)
        for i, val in enumerate(parents):
            if val > -1:
                graph[val].add(i)
        children = [0] * n
        
        def dfs(i=0):
            count = []
            for j in graph[i]:
                count.append(sum(dfs(j)) + 1)
            children[i] = count
            return count

        def product(arr):
            ans = 1
            for i in arr:
                ans *= i
            return ans

        dfs()
        ans = []
        for i in range(n):
            pr = product(children[i])
            if i == 0:
                heapq.heappush(ans, -pr)
            else:
                x = n - sum(children[i])
                heapq.heappush(ans, -(pr * (x - 1)))
                
        tmp = heapq.heappop(ans)
        res = 1
        while ans and heapq.heappop(ans) == tmp:
            res += 1
        return res