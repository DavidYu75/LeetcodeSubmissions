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

        # s_characters = list(s)
        # sorted_s_characters = sorted(s_characters)
        # sorted_s_string = "".join(sorted_s_characters)

        # t_characters = list(t)
        # sorted_t_characters = sorted(t_characters)
        # sorted_t_string = "".join(sorted_t_characters)

        while slow < len(s):
            if s[slow] in t:
                t = t.split(s[slow],1)[1]
            else:
                return False

            slow += 1

        return True