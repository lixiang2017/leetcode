'''
You are here!
Your runtime beats 30.43 % of python submissions.
'''

class RecentCounter(object):

    def __init__(self):
        self.ping_list = []
        self.past_index = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if not t:
            return None
        else:
            self.ping_list.append(t)
        
        n = len(self.ping_list)
        former_index = self.past_index
        for i in xrange(former_index, n):
            if t - self.ping_list[i] > 3000:
                self.past_index += 1
            else:
                return n - self.past_index
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
