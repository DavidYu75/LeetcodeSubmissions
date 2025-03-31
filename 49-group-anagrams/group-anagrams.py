class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_pairs = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            anagram_pairs.setdefault(sorted_word, []).append(word)
        
        return list(anagram_pairs.values())
