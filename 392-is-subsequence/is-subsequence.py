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
        # slow = 0

        # while slow < len(s):
        #     if s[slow] in t:
        #         t = t.split(s[slow],1)[1]
        #     else:
        #         return False

        #     slow += 1

        # return True

        if not s:
            return True

        s_pointer = 0

        for t_pointer in range(len(t)):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1

                if s_pointer == len(s):
                    return True

        return False