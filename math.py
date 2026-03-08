# math leetcode questions in top 150

class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2: return x

        left,right = 1,x

        while left<=right :
            mid = (right+left)//2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid+1
            else:
                right = mid-1

        return right
    
obj = Solution()
print(obj.mySqrt(4))