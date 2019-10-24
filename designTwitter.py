import collections
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.userFollowList = collections.defaultdict(list)
        self.count = 0
        # self.allTweetList = [] # collections.defaultdict(list)
        self.userTweetList = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.userTweetList[userId].append({"tid": tweetId,"index":self.count})
        self.count += 1
        # self.allTweetList.append({"uid":userId,"tid":tweetId})

    def getNewsFeed(self, userId: int) -> [int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        checkList = [userId]
        checkList.extend(set(self.userFollowList[userId]))
        ret = []
        # index = len(self.allTweetList)-1
        # while len(ret) < 10 and index >= 0:
        #     tempD = self.allTweetList[index]
        #     if tempD["uid"] in checkList:
        #         ret.append(tempD["tid"])
        #     index -= 1
        for tempUid in checkList:
            ret.extend(self.userTweetList[tempUid][-10:])
        ret.sort(reverse = True,key = lambda temp: temp["index"])
        ret = ret[:10]
        result = []
        for tempD in ret:
            result.append(tempD["tid"])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId and followeeId not in self.userFollowList[followerId]:
            self.userFollowList[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        tempL = self.userFollowList[followerId]
        while followeeId in tempL:
            tempL.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.follow(1, 2)
obj.postTweet(2, 6)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.unfollow(1,2)
param_2 = obj.getNewsFeed(1)
print(param_2)

