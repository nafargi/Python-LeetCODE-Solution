# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution(object):
    def imageSmoother(self, img):
        

        m,n = len(img),len(img[0])

        res = []

        for i in range(m):
            res_temp = []
            for j in range(n):

                start_row,end_row,start_col,end_col = i-1,i+1,j-1,j+1

                if (i==0):
                    start_row = 0
                
                if (j == 0):
                    start_col = 0

                if (i == m - 1):
                    end_row = m-1
                
                if (j == n - 1):
                    end_col = n-1

                sum1 = 0
                for k in range(start_row,end_row + 1):
                    sum1 += sum(img[k][start_col:end_col+1])
                
                num_elem = (end_row + 1 - start_row ) * (end_col + 1 - start_col ) 

                res_temp.append(sum1//num_elem)
            res.append(res_temp)

        return res

        