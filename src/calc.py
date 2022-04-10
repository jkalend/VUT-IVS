def mult(a, b):
    return a * b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        raise ValueError("MA ERROR: zero division")
    return a / b

def factorial(a):
    if a < 0 or int(a) != a:
        raise ValueError("MA ERROR: invalid factorial")
    res = 1
    while a:
        res *= a
        a -= 1
    return res

def mod(a, b):
    if int(a) != a or int(b) != b or b == 0:
        raise ValueError("MA error: invalid operands")
    return a % b

def root(n, x):
    if n == 0:
        raise ValueError("MA ERROR: zero division")
    if n % 2 == 0:
        if x < 0:
            raise ValueError("MA ERROR: negative even root")
        else:
            return x ** (1.0 / n)
    else:
        if x < 0:
            return -((-x) ** (1.0 / n))
        else:
            return x ** (1.0 / n)

def exp(x, n):
    if x == 0 and n < 0:
        raise ValueError("MA ERROR: zero division")
    return x ** n

def split_expression(expr):
    parsed = []
    operators = ["^", "√", "!", "/", "*", "-", "+", "(", ")", "%"]
    neg = False
    for x in expr:
        if x.isspace():
            continue

        elif x.isdigit():
            if not len(parsed):
                parsed.append(x)
            elif parsed[-1][-1].isdigit() or '.' in parsed[-1]:
                parsed[-1] += x
            else:
                parsed.append(x)

        elif x == '.':
            if not len(parsed):
                raise ValueError("MA error: invalid operator")
            elif parsed[-1][-1].isdigit() and '.' not in parsed[-1]:
                parsed[-1] += x
            else:
                raise ValueError("MA error: invalid sequence")

        elif x in operators or x == '(' or x == ')':
            if x == '√' and (len(parsed) == 0 or parsed[-1] in operators and parsed[-1] != ')'):
                parsed.append("2") # default is square root
            parsed.append(x) 

        else:
            raise ValueError("MA error: unrecognized symbol")
        neg = False
    return parsed

def eval_substr(parsed, in_expr = False):
    priority = [["("], ["!"],["^", "√"], ['-'], ["%", "/", "*"], ["-", "+"], [")"]] 
    funcs = {"^":exp, "/": div, "*": mult, "-": sub, "+": add, "√" : root, "%": mod}

    for operator in priority:
        i = 0
        while i < len(parsed):
            func = None
            x = parsed[i]

            # start of nested expression, do a recursive call to solve whats inside
            if x == '(':
                parsed[i:] = eval_substr(parsed[i + 1:], True)

            # solve only until nearest closing brace
            if x == ')':
                if not in_expr: # no opening brace
                    raise ValueError("MA error: missing brace")
                # if we are at the end of solving the current sub-expression, remove the closing brace 
                if operator == priority[-1]:
                    parsed[i:] = parsed[i + 1:]
                    in_expr = False
                break

            if x == '-' and len(operator) == 1 and x in operator: # sign invert
                if i - 1 < 0 or parsed[i - 1] in [k for j in priority for k in j]:
                    if i + 1 < len(parsed) and str(parsed[i + 1])[-1].isdigit():
                        parsed[i] = -float(parsed[i + 1])
                        parsed[i + 1:] = parsed[i + 2:]
                        i -= 1
                    else:
                        raise ValueError("MA error: invalid operand")

            elif x == '!' and x in operator:
                if i - 1 < 0 or parsed[i - 1] in [k for j in priority for k in j]:
                    raise ValueError("MA error: invalid sequence")

                parsed[i - 1] = factorial(float(parsed[i - 1]))
                parsed[i:] = parsed[i + 1:]
                i -= 1

            elif x in operator and x in funcs.keys():
                func = funcs[x]

            if func != None:
                if i + 1 >= len(parsed) or i - 1 < 0 or parsed[i - 1] in [k for j in priority for k in j]:
                    raise ValueError("MA error: invalid sequences")

                if parsed[i + 1] == '-':
                    if i + 2 >= len(parsed) or parsed[i + 2] in [k for j in priority for k in j]:
                        raise ValueError("MA error: invalid sequence")

                    parsed[i + 1] += str(parsed[i + 2])
                    parsed[i + 2:] = parsed[i + 3:]
                
                elif parsed[i + 1] in [k for j in priority for k in j]:
                    raise ValueError("MA error: invalid sequence")

                parsed[i - 1] = func(float(parsed[i - 1]), float(parsed[i + 1]))
                parsed[i:] = parsed[i + 2:]
                i -= 1
            i += 1
    if in_expr: #no closing brace
        raise ValueError("MA error: missing brace")

    return parsed

def eval_str(expr):
    return round(eval_substr(split_expression(expr))[0], 10)

print(eval_str("3 / (4 - 3)"))
print(eval_str("(4 - 5) * 3"))