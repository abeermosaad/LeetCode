class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        temp = ""
        s = s.replace("-", "").upper()
        s = s[::-1]

        for i in range(0, len(s), k):
            temp += s[i:i+k]
            temp += "-"
        res = temp[::-1]

        res = res.replace("-", "", 1)
        return res
