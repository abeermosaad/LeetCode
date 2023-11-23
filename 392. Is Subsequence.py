def isSubsequence(s: str, t: str) -> bool:
    for i in s:
        if i in t:
            t = t[t.index(i)+1:]
        else:
            return False
    return True
print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("acb", "ahbgdc"))
