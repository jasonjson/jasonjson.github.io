---
layout: post
title: 355 - Design Twitter
date: 2017-05-06
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:**

* postTweet(userId, tweetId): Compose a new tweet.
* getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
* follow(followerId, followeeId): Follower follows a followee.
* unfollow(followerId, followeeId): Follower unfollows a followee.

[Use * to unpack arguments lists](https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists)

```python
import collections
import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        #key: user_id val: post_id
        self.tweets = collections.defaultdict(collections.deque)
        #key: follower val: followee
        self.users = collections.defaultdict(set)
        #give all tweets a time stamp for sorting
        self.time = 0


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        #user is follwing himself
        self.users[userId].add(userId)
        self.tweets[userId].append(Tweet(self.time, tweetId))
        self.time += 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        #heapq.merge - merge multiple sorted list from each followee
        #use * to unpack argument lists
        news = heapq.merge(*(sorted(self.tweets[followee]) for followee in self.users[userId]))
        ret = [tweet.id for tweet in news]
        return ret if len(ret) <= 10 else ret[:10]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.users[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.users[followerId].discard(followeeId)

class Tweet(object):
    def __init__(self, time, id):
        self.time = time
        self.id = id


    #user defined method for sorting Tweet object
    #self.time < other.time if accending
    #other.time < self.time if descending
    def __lt__(self, other):
        return other.time < self.time

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```
