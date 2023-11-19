class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        for (a, b) in zip(word1, word2):
            string += (a + b)     
        return string + word1[len(word2):] + word2[len(word1):]
