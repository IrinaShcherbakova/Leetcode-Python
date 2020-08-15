class Tweet:
    
    def __init__(self, user_id: int, tweet_id: int):
        self.owner = user_id
        self.id = tweet_id
        

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.all_tweets = []
        # self.all_users = {}
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.all_tweets.append(Tweet(userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        users = (self.followers[userId] if userId in self.followers else set())
        count = 0
        tweets = []
        for tweet in reversed(self.all_tweets):
            if count == 10:
                return tweets
            if tweet.owner == userId or tweet.owner in users:
                count += 1
                tweets.append(tweet.id)
        return tweets
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.followers:
            self.followers[followerId] = {followeeId}
        else:
            self.followers[followerId].add(followeeId)
        return

    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.followers:
            all_followees = self.followers[followerId]
            all_followees.discard(followeeId)
        return
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
