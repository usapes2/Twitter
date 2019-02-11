class Twitter:
    def __init__(self):
        """
        Initialize data structure.
        """
        self.users = {}  # All users.  key -> UserId, val -> Following List
        self.tweets = {} # All tweets. key -> UserId, val -> Tweets List
        self.time = 0


    def pr(self):
        """
        Helper function
        """
        print("Number of accounts: " + str(len(self.users)))
        print("Number of tweets: " + str(len(self.tweets)))


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
        Compose a new ***Time Stamped Tweet ***
        """
        self.time = self.time + 1 # Time Stamp for tweet
        if not self.checkKey(self.users, userId):
            self.users[userId] = [] # User doesn't follow anyone yet
            self.tweets[userId] = [(self.time,tweetId)]
        else:
            self.tweets[userId].append((self.time,tweetId))
        # Add fix to No More than 10 tweets per Acc

        if self.isOverLimit(userId):
            del self.tweets[userId][0]
            


    def follow(self, followerId: 'int', followeedId: 'int') -> 'None':
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if not self.checkKey(self.users, followeedId):
            self.users[followeedId] = []

        if not self.checkKey(self.users, followerId):
            self.users[followerId] = [] 

        if not self.isFollow(followerId,followeedId):
            self.users[followerId].append(followeedId)
            

    def unfollow(self, followerId: 'int', followeeId: 'int') -> 'None':
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if (self.checkKey(self.users, followeedId) ) and (self.checkKey(self.users, followerId)):
            for idx, val in enumerate(self.users[followerId]):
                if (val == followeeId):
                    del self.users[followerId][idx]
                    break

        
t = Twitter()

t.follow(1,2)
t.follow(1,3)
t.follow(1,4)
t.follow(5,6)

print(len(t.tweets[3]))
    
print("Ok")
