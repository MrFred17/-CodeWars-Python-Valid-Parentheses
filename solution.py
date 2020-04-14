def valid_parentheses(string):
    # your code here

    stack = []
    for s in string:
        if(s == '('):
            stack.append(s)
        elif(s == ')'):
            try:
                stack.pop()
            except:
                return False

    if(len(stack) == 0):
        return True
    else:
        return False

# this is a pretty similar solution but a bit shorter with less runtime
def valid_parentheses_v2(string): 
    counter = 0
    for char in string:
        if char == '(': total += 1
        if char == ')': total -= 1
        if counter < 0: return False
    return True if counter == 0 else False
