<<<<<<< HEAD
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        
        pascal = [1,1]
        while rowIndex > 1:
            temp = []
            for i in range(1,len(pascal)):
                temp.append(pascal[i]+pascal[i-1])
                
            pascal[1:-1] = temp
            rowIndex -= 1
        
=======
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        
        pascal = [1,1]
        while rowIndex > 1:
            temp = []
            for i in range(1,len(pascal)):
                temp.append(pascal[i]+pascal[i-1])
                
            pascal[1:-1] = temp
            rowIndex -= 1
        
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return pascal