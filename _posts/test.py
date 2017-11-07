class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        if not tickets:
            return []

        destinations = {}
        for start, end in tickets:
            destinations.setdefault(end, [])
            destinations.setdefault(start, [])
            destinations[start].append(end)

        ret = ["JFK"]
        self.helper(destinations, "JFK", ret, len(tickets) + 1)
        return ret

    def helper(self, destinations, last_stop, ret, total_stops):
        if len(ret) == total_stops:
            return True
        potential_stops = destinations.get(last_stop).sort()
        __import__('pdb').set_trace()
        for i in xrange(len(potential_stops)):
            next_stop = potential_stops.pop(i)
            ret.append(next_stop)
            if self.helper(destinations, next_stop, ret, total_stops):
                return True
            potential_stops.append(ret.pop())
        return False

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
