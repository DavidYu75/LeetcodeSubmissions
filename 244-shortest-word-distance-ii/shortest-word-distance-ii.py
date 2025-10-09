class WordDistance:

    # brute force approach
    # go through the list and find the index of the first word we want to look for
    # go through the list again and find the index of the second word
    # compare the distance

    # optimized approach
    # we can have a hashmap, where the key is the word and the value of that key is the index where that word shows up
    # so once we have the indexes of each key, we can then compare and find the shortest indexes between the two target words

    # "practice": [0]
    # "coding": [1, 9]
    # 3 and 0, take the absolute value
    # "makes": [3, 4]
    # 3 - 1 = 2
    # 4 - 3 = 1


    def __init__(self, wordsDict: List[str]):
        self.hashmap = defaultdict(list)

        for i in range(len(wordsDict)):
            self.hashmap[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.hashmap[word1], self.hashmap[word2]

        i = j = 0
        result = float('inf')

        while i < len(l1) and j < len(l2):
            result = min(result, abs(l1[i] - l2[j]))

            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        
        return result


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)