class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        if not time:
            return ""

        num_set = set(time)
        hour, minute = time.split(":")
        hour, minute = int(hour), int(minute)
        while True:
            minute += 1
            if minute == 60:
                hour += 1
                minute = 0
                hour %= 24
            str_hour = "0" + str(hour) if hour <= 9 else str(hour)
            str_min = "0" + str(minute) if minute <= 9 else str(minute)
            print str_hour, str_min
            if set(str_hour) <= num_set and set(str_min) <= num_set:
                return str_hour + ":" + str_min
        return ""


if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.nextClosestTime("23:59"))
