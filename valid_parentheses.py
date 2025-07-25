def validParentheses(s):
    stack = []
    openToClose = {")":"(","]":"[","}":"{"}
    for c in s:
        if c in openToClose:
            if stack and stack[-1] == openToClose[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
s = "([{()}])"
print(validParentheses(s))
