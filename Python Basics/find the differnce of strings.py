class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        # now XOR the ASCII values in s and t
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
 # now the remaining result is the  ASCII value of added letter
     
        return chr(result)

sol = Solution()
s = "abcd"
t = "abcde"

added_letter = sol.findTheDifference(s, t)
print(added_letter)
            



    