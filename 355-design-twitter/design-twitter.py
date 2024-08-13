class Twitter:
    def __init__(self):
        self.post = deque()
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        count, ans = 0, []
        for u, t in self.post:
            if count < 10 and (u == userId or u in self.following[userId]):
                ans.append(t)
                count += 1
            if count >= 10: break
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)