class Solution:
    # abc   ahbgdc
    # a     hbgdc
    # b     gdc
    # c     c

    # axc   ahbdc
    # a     hbdc
    # x     false

    # acb   ahbgdc
    # a     hbgdc
    # c     
    # b     false
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0

        while slow < len(s):
            if s[slow] in t:
                t = t.split(s[slow],1)[1]
            else:
                return False

            slow += 1

        return True