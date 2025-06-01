class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        
        for i in range(len(s)):
            if i % 2 == 0:
                result += s[i]
            else:
                
                shifted_char = chr(ord(s[i - 1]) + int(s[i]))
                result += shifted_char
                
        return result
