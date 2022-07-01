class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        profit=0
        for i in range(len(boxTypes)):
            if truckSize>=boxTypes[i][0]:
                profit+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            elif boxTypes[i][0]>truckSize>0:
                profit+=truckSize*boxTypes[i][1]
                truckSize=0
        return profit
         
        