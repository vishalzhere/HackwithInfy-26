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

    def isPalindrome(self, x):

        if x < 0:
            return False

        rev = 0
        original = x

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        return rev == original

    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits

            else:
                digits[i] = 0

        return [1] + digits

    def trailingZeroes(self, n):

        count = 0

        while n > 0:
            n //= 5
            count += n

        return count

    def maxPoints(self, points):
        
        if len(points) <= 2:
            return len(points)

        result = 0

        for i in range(len(points)):
            slopes = {}

            for j in range(i+1,len(points)):

                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx ==0 :
                    slope = 'inf'
                else:
                    slope = float(dy)/dx

                slopes[slope]  = slopes.get(slope,1) + 1
                result = max(result, slopes[slope])

        return result

    def myPow(self, x, n):
        return x**n
        
    
obj = Solution()
print(obj.maxPoints([[1,1],[2,2],[3,3]]))
print(obj.myPow(9,8))