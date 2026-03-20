class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # 1. Store the sign and work with absolute value
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        
        while x != 0:
            # 2. Get the last digit
            digit = x % 10
            x //= 10
            
            # 3. Check for overflow BEFORE updating result
            # Since we work with positive 'result', we only check against INT_MAX
            if result > (INT_MAX - digit) / 10:
                return 0
            
            result = result * 10 + digit
            
        # 4. Re-apply the sign
        result *= sign
        
        # 5. Final check for the negative boundary
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result