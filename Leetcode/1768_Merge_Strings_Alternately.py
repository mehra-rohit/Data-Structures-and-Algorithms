class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        word3 = ''
        for i,j in zip(word1,word2):
            word3 += i + j
        
        if len(word1)>len(word2):
            word3 += word1[len(word2):]
        else :
             word3 += word2[len(word1):]

        return word3
