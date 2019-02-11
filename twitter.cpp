#include<iostream>
#include<map>
#include<set>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

typedef vector< pair<int,int> > vp;
typedef vector< int> vi;
typedef std::map<int, vp>::iterator Tweets_iter ;
typedef std::map<int, vi>::iterator Users_iter;

class Twitter {

public:
	/** Initialize your data structure here. */
	int count;
	std::map<int, vp> Tweets ;
	std::map<int, vi> Users; // Users ( userId, users he follows )


	Twitter() {
		count = 0 ;
	}

	/** Compose a new tweet. */
	void postTweet(int userId, int tweetId) {
//	cout << twitts[1][0].second << endl;
		//count=count+1;

		Users_iter itr = Users.find(userId) ;
		if(itr == Users.end() ) {// add userId to the Users
			pair<int,vi> p;
			p.first = userId; // initializing the User 
			vi v;
			p.second = v; // initializing the list for the User
			Users.insert(p);
		}
		
		pair<int,vp	
		

	}

	/** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
	vector<int> getNewsFeed(int userId) {

	}

	/** Follower follows a followee. If the operation is invalid, it should be a no-op. */
	void follow(int followerId, int followeeId) {

	}

	/** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
	void unfollow(int followerId, int followeeId) {

	}

};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
int main(int argc, const char *argv[])
{


//	cout << twitts[1][0].second << endl;


	return 0;
}
