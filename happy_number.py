<<<<<<< HEAD
class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while count < 400:
            n = str(n)
            n = list(map(int, n))
            n = self.squared(n)
            n = sum(n)
            if n == 1:
                return True
            else:
                count += 1
        return False

    def squared(self,n):
        for i in range(len(n)):
            n[i] = n[i]**2
=======
class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while count < 400:
            n = str(n)
            n = list(map(int, n))
            n = self.squared(n)
            n = sum(n)
            if n == 1:
                return True
            else:
                count += 1
        return False

    def squared(self,n):
        for i in range(len(n)):
            n[i] = n[i]**2
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return n