class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # print(A)
        for row in A:
            i = 0
            j = len(row)-1
            while i <= j:
                temp = row[i]
                if row[j] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
                if temp == 0:
                    row[j] = 1
                else:
                    row[j] = 0
                i += 1
                j -= 1
            # print(row)
            # if row[i] == 0:
            #     row[i] = 1
            # else:
            #     row[i] = 0
        # print(A)
        return A
