class Solution(object):
    def rotate(self, matrix):
        
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        return matrix

    def spiralOrder(self, mat):
      
        m = len(mat)
        n = len(mat[0])
        left , right = 0 , n-1
        top , bottom = 0 , m-1
        ans = []

        while top<=bottom and left <= right:
            for i in range(left,right+1):
                ans.append(mat[top][i])

            top+=1
            for i in range(top,bottom+1):
                ans.append(mat[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(mat[bottom][i])
            bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(mat[i][left])
            
            left+=1

        return ans


obj = Solution()
print(obj.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))