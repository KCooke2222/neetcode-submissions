class User:
    def __init__(self):
        self.tweets = []
        self.following = set()

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def confirmUser(self, userId: int) -> None:
        if not userId in self.users:
            self.users[userId] = User()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.confirmUser(userId)

        self.users[userId].tweets.append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.confirmUser(userId)
        newsFeed = []

        recentTweets = []
        user = self.users[userId]

        for u in list(user.following) + [userId]:
            u = self.users[u]
            if abs(-1) <= len(u.tweets):
                time, tweet = u.tweets[-1]
                tweetData = (time, tweet, u, -2)
                heapq.heappush(recentTweets, tweetData)

        for i in range(10):
            if not recentTweets:
                break

            # append to newsfeed
            time, tweet, u, tweetIndex = heapq.heappop(recentTweets)
            newsFeed.append(tweet)

            # adding next tweet from this user
            if abs(tweetIndex) <= len(u.tweets):
                time, tweet = u.tweets[tweetIndex]
                tweetData = (time, tweet, u, tweetIndex-1)
                heapq.heappush(recentTweets, tweetData)

        return newsFeed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.confirmUser(followerId)

        if followerId == followeeId:
            return

        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.confirmUser(followerId)

        self.users[followerId].following.discard(followeeId)
