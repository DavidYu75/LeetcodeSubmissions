class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_pairs = {}

        for word in strs:
            sorted_word = list(word)
            sorted_word.sort()
            sorted_word = "".join(sorted_word)

            if sorted_word in anagram_pairs:
                anagram_pairs[sorted_word].append(word)
            else:
                anagram_pairs[sorted_word] = [word]
        
        pairs = []

        for anagram in anagram_pairs:
            pairs.append(anagram_pairs[anagram])

        return pairs
