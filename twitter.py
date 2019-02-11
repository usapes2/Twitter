class Twitter:
    def __init__(self):
        """
        Initialize data structure.
        """
        self.users = {}  # All users.  key -> UserId, val -> Following List
        self.tweets = {} # All tweets. key -> UserId, val -> Tweets List
        self.time = 0


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





t = Twitter()
t.postTweet(999,123)
t.postTweet(99,13)
t.postTweet(99,3)
t.postTweet(99,0)
print(t.time)

print("Ok")
