class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        temp = 0
        neg = False
        if x < 0:
            x = abs(x)
            neg = True
        while x != 0:
            last = x % 10
            print(last)
            x = int(x / 10)
            temp = rev * 10 + last
            rev = temp
        if neg:
            rev = 0 - rev
        if rev > 2**31 - 1 or rev < 0 - (2)**31:
            return 0
        else:
            return rev

