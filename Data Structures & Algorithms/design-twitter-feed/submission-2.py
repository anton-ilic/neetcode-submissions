class Twitter:

    def __init__(self):
        self.user_tweets = {} # userId, tweet array ==>(tweetId, time)
        self.user_is_following = {} # userId, following users set
        # for this simplified version, maybe time could just be an integer value
        self.current_time = 0 
        
        # modeling time as an integer for sequential events;
        # could actually use current time in a real scenerio that may have ties, etc
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        post_time = self.current_time
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append((tweetId, post_time))
        self.current_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get last 10 for each self.user_is_following's tweets and self.user_tweets, then sort on post_time (second field)
        feed_tweets = []
        # can use a max heap here with size 10 aswell

        for user in self.user_is_following.get(userId, []):
            users_tweets = self.user_tweets.get(user, [])
            feed_tweets = feed_tweets + users_tweets[-10:]
        feed_tweets = feed_tweets + self.user_tweets.get(userId, [])[-10:]
        
        # get the highest 10
        feed_tweets.sort(key = lambda x : x[1], reverse = True)
        feed_tweets = feed_tweets[:10]
        ans = []
        for tweet in feed_tweets:
            ans.append(tweet[0])
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        # You shouldn't be able to follow yourself; exit gracefully or raise error
        if followerId == followeeId:
            return 
        
        if followerId not in self.user_is_following:
            self.user_is_following[followerId] = set()
        self.user_is_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if self.user_is_following.get(followerId, None) == None:
        #     return
        # could raise Error above;

        if followeeId in self.user_is_following.get(followerId, set()):
            self.user_is_following[followerId].remove(followeeId)

