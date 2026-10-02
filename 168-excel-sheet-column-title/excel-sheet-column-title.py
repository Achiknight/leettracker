class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        values = range(0, 26)

        dic = dict(zip(values,chars))

        num = ""
        
        while columnNumber >0:
            dig = (columnNumber-1)%26
            num = dic[dig] + num 
            columnNumber = (columnNumber-1)//26
                
        return num