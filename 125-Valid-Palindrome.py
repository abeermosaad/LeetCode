class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for char in s:
            if char.lower() >='a' and char <='z' or char >= '0' and char <= '9':
                string += char.lower()
        reversed_str = ''
        for i in range(len(string) -1, -1, -1):
            reversed_str += string[i]
             

        return reversed_str == string 

        