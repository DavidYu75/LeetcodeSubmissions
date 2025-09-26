class Solution:
    def expand(self, s: str) -> List[str]:
        # parse the s string into a list of options
        # after we have the group of options, we dfs to generate all possible combinations
        # time O(n) total number of possible resulting strings * number of groups (length of each resulting string)
        # R = product of options count, L = length of each resulting string O(n * R * L)
        # space: O(R * L)

        groups = []
        i, n = 0, len(s)

        while i < n:
            if s[i] == '{':
                j = i + 1
                while j < n and s[j] != '}':
                    j += 1

                options = s[i+1:j].split(',')
                options.sort()
                groups.append(options)
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1
        
        print(groups)

        result = []
        path = []

        def dfs(index):
            if index == len(groups):
                result.append(''.join(path))
                return 
            
            for ch in groups[index]:
                path.append(ch)
                dfs(index + 1)
                path.pop()

        dfs(0)

        return result