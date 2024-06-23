'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        mem_o= []
        o = ['(','[','{']
        c = [')',']','}']
        if len(s) > 1 and len(s)%2 == 0: #if more than 1 & items in s both in o & c 
            if s[0] in c: #fist item should not be a CLOSED
                return False
            else:
                for i in range(len(s)): 
                    if s[i] in o: #OPENED
                        mem_o.append(s[i])
                    else: #CLOSED
                        if not any(mem_o):
                            return False                  
                        elif o.index(mem_o[-1])== c.index(s[i]):
                            mem_o.pop() #matched pair remove last item 
                        else:
                            return False
                if any(mem_o): #any leftovers after pops 
                    return False
                return True     
        else:
            return False

~~
