class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        last = None
        y = x
        while x != 0:
            last = x % 10
            x = int(x / 10)
            temp = rev * 10 + last
            rev = temp
        if y - rev == 0:
            return True
        else:
            return False

