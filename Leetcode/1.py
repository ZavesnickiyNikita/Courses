class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ls, result = [], []
        for letter in s:
            ls.append(letter)
        for letter in ls:
            result.append(dct.get(letter))
        return sum(result)


a = Solution()
print(a.romanToInt(s="III"))
print(a.romanToInt(s="LVIII"))
print(a.romanToInt(s="MCMXCIV"))


