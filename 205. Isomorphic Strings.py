class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dic = {}
        if len(s) != len(t):
            return False
        for a, b in zip(s, t):
            if a in dic:
                if dic[a] != b:
                    return False
            elif b in dic.values():
                return False
            else:
                dic[a] = b
        return True
