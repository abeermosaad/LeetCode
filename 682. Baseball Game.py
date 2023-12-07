class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li = [0]
        for s in operations:
            if s == "C":
                li.pop()
            elif s == "D":
                li.append(li[-1] * 2)
            elif s == "+":
                li.append(li[-1] + li[-2])
            else:
                li.append(int(s))
        return sum(li)
