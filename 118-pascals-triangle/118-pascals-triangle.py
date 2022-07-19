class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1],[1,1]] #Initialise first 2 rows
        if numRows <= 2:
            return pascal[:numRows]
        for i in range(2,numRows): # for the rest of the rows
            t = pascal[i-1] #fetch previous row
            newRow = [1] #add 1st element since it'll always be 1 for each row
            for i in range(len(t) - 1):
                newRow.append(t[i] + t[i+1]) #sum of previous 2 elements
            newRow.append(1) #add last element which will always be 1
            pascal.append(newRow)
        return pascal
        