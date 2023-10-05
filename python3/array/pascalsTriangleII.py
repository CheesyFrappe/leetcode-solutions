class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # [1, 4, 6, 4, 1]
        # [1, 5, 10, 10, ,5 ,1]
        l = []

        for i in range(rowIndex + 1):
            if i == 0:
                l.append([1])
            elif i == 1:
                l.append([1, 1])
            else:
                temp = [1]
                for j in range(1,i):
                    temp.append(l[i - 1][j - 1] + l[i - 1][j])
                temp.append(1)
                l.append(temp)

        print(l)
        return l[rowIndex]
                
