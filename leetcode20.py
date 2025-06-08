class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if (ch == '}'and top!='{')or(ch == ')'and top!='(')or(ch == ']'and top != '['):
                    return False
        return len(stack) == 0
