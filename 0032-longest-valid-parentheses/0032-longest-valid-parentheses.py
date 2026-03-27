class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initial base index
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '('
                stack.append(i)
            else:
                # We found a ')', pop the matching '(' or the base
                stack.pop()
                
                if not stack:
                    # If stack is empty, this ')' is a new base
                    stack.append(i)
                else:
                    # Current length = current index - index of the last base/unmatched '('
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)
                    
        return max_length