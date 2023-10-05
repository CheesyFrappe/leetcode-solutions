class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []

        for j in range(numRows):
            if j == 0:
                l.append([1])
            elif j == 1:
                l.append([1, 1])
            else:
                temp = [1]
                for i in range(1,j):
                    temp.append(l[j - 1][i - 1] + l[j - 1][i])
                temp.append(1)
                l.append(temp)
        return l