<<<<<<< HEAD
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        
        mergedIntervals = [] 
        
        for interval in intervals:
            if len(mergedIntervals) == 0:
                mergedIntervals.append(cur)
            else:
                prev = mergedIntervals[-1]
                if prev[-1] >= cur[0]: 
                    prev[-1] = max(prev[-1], cur[-1])
                else:
                    mergedIntervals.append(cur)
                    
=======
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        
        mergedIntervals = [] 
        
        for interval in intervals:
            if len(mergedIntervals) == 0:
                mergedIntervals.append(cur)
            else:
                prev = mergedIntervals[-1]
                if prev[-1] >= cur[0]: 
                    prev[-1] = max(prev[-1], cur[-1])
                else:
                    mergedIntervals.append(cur)
                    
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return mergedIntervals