def isValid(str):
    openLast = []
    for character in str:
        if character == '(' or character == '{' or character == '[':
            openLast.append(character)
            continue
        if character == ')' or character == '}' or character == ']':
            if len(openLast) == 0:
                return False
            lastParenthesis = openLast.pop()
            if character == ')' and lastParenthesis != '(':
                return False
            if character == ']' and lastParenthesis != '[':
                return False
            if character == '}' and lastParenthesis != '{':
                return False
    return len(openLast) == 0





print("res is %s" % isValid("(()"))
