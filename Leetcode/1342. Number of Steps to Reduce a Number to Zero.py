class Solution(object):
    def numberOfSteps(self, num, count=0):
        """
        :type num: int
        :rtype: int
        """
        #base case
        if num==0:
            return count
        elif num%2==0:
            count += 1
            return self.numberOfSteps(num//2,count)
        else:
            count += 1
            return self.numberOfSteps(num-1,count)
