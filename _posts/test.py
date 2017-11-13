import collections
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []
        self.index = collections.defaultdict(list)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        index_list = self.index[val]
        self.num.append(val)
        index_list.append(len(self.num) - 1)
        return True if len(index_list) == 1 else False


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        __import__('pdb').set_trace()
        index_list = self.index[val]
        if index_list:
            index, last = index_list[-1], self.num[-1]
            self.num[index] = last
            if index != len(self.num) - 1:
                self.index[last].append(index)
            self.num.pop()
            index_list.pop()
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.num[random.randint(0, len(self.num) - 1)]
if __name__ == "__main__":
    ran = RandomizedCollection()
    ran.insert(4)
    ran.insert(3)
    ran.insert(4)
    ran.insert(2)
    ran.insert(4)
    ran.remove(4)
    ran.remove(4)
    ran.remove(3)
    ran.remove(4)
    ran.remove(4)

