class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in dic:
                dic[sorted_s].append(s)
            else:
                dic[sorted_s] = [s]
        return list(dic.values())
            