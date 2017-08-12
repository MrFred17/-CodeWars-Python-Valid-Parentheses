def valid_parentheses(string):
    # your code here

    queue = []
    for s in string:
        if(s == '('):
            queue.append(s)
        elif(s == ')'):
            try:
                queue.pop()
            except:
                return False

    if(len(queue) == 0):
        return True
    else:
        return False
