import copy
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_map = {}
        self.tweet_map = {}
        self.time_order = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

        user_tweets = self.tweet_map.setdefault(userId, [])
        user_tweets.append((tweetId, self.time_order))
        self.time_order += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweet_list = copy.deepcopy(self.tweet_map.get(userId, []))
        for followee in self.user_map.get(userId, []):
            tweet_list.extend(self.tweet_map.get(followee, []))
        tweet_list.sort(key = lambda tweet: tweet[1], reverse = True)
        return [tweet[0] for tweet in tweet_list[:10]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        user_follows = self.user_map.setdefault(followerId, [])
        user_follows.append(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        user_follows = self.user_map.setdefault(followerId, [])
        try:
            user_follows.remove(followeeId)
        except:
            pass

if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.getNewsFeed(1)
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print twitter.getNewsFeed(1)
    twitter.unfollow(1, 2)
    print twitter.getNewsFeed(1)
