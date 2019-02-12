class Twitter:
    def __init__(self):
        """
        Initialize data structure.
        """
        self.users = {}  # All users.  key -> UserId, val -> Following List
        self.tweets = {} # All tweets. key -> UserId, val -> Tweets List
        self.time = -10000


    def pr(self):
        """
        Helper function
        """
        print("Number of accounts: " + str(len(self.users)))
        print("Number of tweets: " + str(len(self.tweets)))


    def prUserFollow(self,userId):
        """
        Helper function
        """
        print("User " + str(userId) + " follows: " + str(len(self.users[userId])))
        for each in self.users[userId]:
            print(each)


    def isFollow(self,userId,target):
        """
        Helper function
        """
        for each in self.users[userId]:
            if target == each:
                return True
        return False


    def isOverLimit(self,userId):
        """
        Helper function
        """
        if (len(self.tweets[userId]) > 10):
            return True
        else:
            return False


    def checkKey(self,dict_, key):
        """
        Helper function
        """
        if key in dict_.keys():
          #  print("Present, ", end = ' ')
          #  print("value =", dict_[key])
            return True
        else:
          #  print("Not present")
            return False


    def postTweet(self, userId: 'int', tweetId: 'int') -> 'None':
        """
        Compose a new ***Tweet*** with a time stamp
        """
        self.time = self.time + 1 # Time Stamp for tweet
        
        if not self.checkKey(self.users, userId):
            self.users[userId] = [] # User doesn't follow anyone yet
            self.tweets[userId] = [(self.time,tweetId)]
        elif not self.checkKey(self.tweets, userId):
            self.tweets[userId] = [(self.time,tweetId)]
        else: 
            self.tweets[userId].append((self.time,tweetId))

        if self.isOverLimit(userId):
            del self.tweets[userId][0]
            


    def follow(self, followerId: 'int', followeedId: 'int') -> 'None':
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if not self.checkKey(self.users, followeedId):
            self.users[followeedId] = []
            self.tweets[followeedId] = []

        if not self.checkKey(self.users, followerId):
            self.users[followerId] = [] 
            self.tweets[followerId] = []

        if not self.isFollow(followerId,followeedId):
            self.users[followerId].append(followeedId)
            

    def unfollow(self, followerId: 'int', followeedId: 'int') -> 'None':
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if (self.checkKey(self.users, followeedId) ) and (self.checkKey(self.users, followerId)):
            for idx, val in enumerate(self.users[followerId]):
                if (val == followeedId):
                    del self.users[followerId][idx]
                    break

    def getNewsFeed(self, userId: 'int') -> 'List[int]':
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        # Go to userId retrieve all tweets from his/her followee list, sort, return
        if not self.checkKey(self.users, userId):
            return []
        li = []
       # li = self.tweets[userId]

        for each in self.users[userId]:
            if each == userId:
                break
            if not self.tweets[each]:
                break
            for item in self.tweets[each]:
                li.append(item)
                
        if self.tweets[userId]:        
            for item in self.tweets[userId]:
                li.append(item)

        sorted(li, key = lambda each: each[0])
        li.sort(reverse = True)

        return ( [x[1] for x in li ][:10])




