class Solution:
    def isValid(self, s):
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            # 如果栈内有元素，且当前元素对应着字典中的key
            if stack and i in dic:
                # 如果栈内最后一个元素等于字典中i对应的value
                if stack[-1] == dic[i]:
                    # value出栈
                    stack.pop()
                else:
                    # 字符串内没有有效括号
                    return False
            else:
                # value入栈
                stack.append(i)
        # 栈中无元素，返回True，有元素，返回False
        return not stack

if __name__ == "__main__":
    s = Solution()
    strs = "()[]{}"
    res = s.isValid(strs)
    strs = "{([])}"
    res = s.isValid(strs)
    strs = "{]"
    res = s.isValid(strs)