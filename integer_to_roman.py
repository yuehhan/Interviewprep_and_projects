<<<<<<< HEAD
class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k in dictionary:
            while num >= k:
                res += dictionary[k]
                num -= k
=======
class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k in dictionary:
            while num >= k:
                res += dictionary[k]
                num -= k
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return res