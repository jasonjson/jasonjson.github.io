class Solution(object):
    def reOrder(self, s):
        if not s:
            return ""
        counter = collections.Counter(s)
        pq = []
        ret = []
        for k, v in counter.iteritems():
            heapq.heappush(pq, (-v, k))
        while pq:
            count1, char1 = heapq.heappop(pq)
            ret.append(char1)
            if not pq:
                break
            count2, char2 = heapq.heappop(pq)
            ret.append(char2)
            count1 += 1
            count2 += 1
            if count1 < 0:
                heapq.heappush(pq, (count1, char1))
            if count2 < 0:
                heapq.heappush(pq, (count2, char2))
        return "".join(ret)
