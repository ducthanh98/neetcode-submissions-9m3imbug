import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.followMap = {} # userId -> SET of followeeIds
        self.tweetMap = {}  # userId -> list of [count, tweetId]
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        tweets = self.tweetMap.get(userId, [])
        tweets.append([self.count, tweetId])
        self.tweetMap[userId] = tweets
        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        # Lấy set follow, nếu không có thì lấy set rỗng set()
        # Dùng toán tử hợp | để gộp thêm chính userId vào mà không làm sửa set gốc
        followee = self.followMap.get(userId, set()) | {userId}
        res = []

        for v in followee:
            tweets = self.tweetMap.get(v, [])

            if len(tweets) > 0:
                idx = len(tweets) - 1
                tweet = tweets[idx]
                heapq.heappush(max_heap, (-tweet[0], tweet[1], idx, v))

        while len(res) < 10 and len(max_heap) > 0:
            pop_value = heapq.heappop(max_heap)
            next_idx = pop_value[2] - 1 
            res.append(pop_value[1])
            if next_idx >= 0:
                tweet = self.tweetMap[pop_value[3]][next_idx]
                heapq.heappush(max_heap, (-tweet[0], tweet[1], next_idx, pop_value[3]))

        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        # Dùng .add() của set để chống trùng lặp vĩnh viễn
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Kiểm tra an toàn trước khi xóa để không bị crash lỗi ValueError
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)