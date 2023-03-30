class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        chars = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        for i in range(len(s)):
            ex = s[i - 1:i] + s[i]
            if ex in chars and len(ex) == 2:
                number += chars[ex]
                number -= chars[s[i - 1]]
            else:
                number += chars[s[i]]
        return number


exemple = Solution()
res = exemple.romanToInt('MCMXCIV')

print(res)
