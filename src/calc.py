
def mult(a, b):
    """Multiply two numbers.
    Return their product"""
    return a * b


def add(a, b):
    """Add two numbers.
    Return their sum."""
    return a + b


def sub(a, b):
    """Subtract two numbers.
    First number is minuend, second is subtrahend.
    Return their difference."""
    return a - b


def div(a, b):
    """Divide two numbers.
    First number is dividend, second is divisor.
    Return quotient.
    Raise an error if divisor is zero.
    """
    if b == 0:
        raise ValueError("MA ERROR: zero division")
    return a / b


def factorial(a):
    """Take a single number and return its factorial.
    Raise an error if the number is negative or not an integer."""
    if a < 0 or a > 170 or int(a) != a:
        raise ValueError("MA ERROR: invalid factorial")
    res = 1
    while a:
        res *= a
        a -= 1
    return res


def mod(a, b):
    """Divide two numbers.
    First number is dividend, second is divisor.
    Return residue of division.
    Raise an error if divisor is zero or any of the numbers is not an integer.
    """
    if int(a) != a or int(b) != b or b == 0:
        raise ValueError("MA error: invalid operands")
    return a % b


def root(n, x):
    """Take two numbers, first one is the index, second is the radicand.
    Return x^{1/n}.
    Raise an error if index is zero.
    Raise an error if index is even while radicand is negative"""
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
    """Take two numbers, first is base, second is exponent.
    Return x^n.
    Raise an error if the base is zero while the exponent is negative."""
    if x == 0 and n < 0:
        raise ValueError("MA ERROR: zero division")
    return x ** n


def split_expression(expr):
    """Split the string representing the mathematical expression to a format required by eval_substr.
    Raise an error if the string contains operators not recognized by the library."""
    parsed = []
    operators = ["^", "√", "!", "/", "*", "-", "+", "(", ")", "%"]
    digits = [str(x) for x in range(10)]
    for x in expr:
        if x.isspace():
            continue

        elif x in digits:
            if not len(parsed):
                parsed.append(x)
            elif parsed[-1][-1] in digits or '.' in parsed[-1]:
                parsed[-1] += x
            else:
                parsed.append(x)

        elif x == '.':
            if not len(parsed):
                raise ValueError("MA error: invalid operator")
            elif parsed[-1][-1] in digits and '.' not in parsed[-1]:
                parsed[-1] += x
            else:
                raise ValueError("MA error: invalid sequence")

        elif x in operators:
            if x == '√' and (len(parsed) == 0 or parsed[-1] in operators and parsed[-1] != ')' and parsed[-1] != '√'):
                parsed.append("2")    # default is square root
            parsed.append(x) 

        else:
            raise TypeError("MA error: unrecognized symbol")
    return parsed


def eval_substr(parsed, in_expr=False):
    """Evaluate parsed representation of input string.
    Return the result of solving the mathematical expression.
    Raise an error if the expression cannot be solved."""
    
    priority = [["("], ["!"], ["^", "√"], ['-'], ["%", "/", "*"], ["-", "+"], [")"]]
    funcs = {"^": exp, "/": div, "*": mult, "-": sub, "+": add, "√": root, "%": mod}

    for operator in priority:
        i = 0
        while i < len(parsed):
            func = None
            x = parsed[i]

            # start of nested expression, do a recursive call to solve what's inside
            if x == '(':
                parsed[i:] = eval_substr(parsed[i + 1:], True)

            # solve only until nearest closing brace
            if x == ')':
                if not in_expr:    # no opening brace
                    raise ValueError("MA error: missing brace")
                # if we are at the end of solving the current sub-expression, remove the closing brace 
                if operator == priority[-1]:
                    parsed[i:] = parsed[i + 1:]
                    in_expr = False
                break

            if x == '-' and len(operator) == 1 and x in operator:    # sign invert
                if i - 1 < 0 or parsed[i - 1] in [k for j in priority for k in j] and str(parsed[i + 1])[-1].isdigit():
                    parsed[i] = -float(parsed[i + 1])
                    parsed[i + 1:] = parsed[i + 2:]
                    i -= 1

            elif x == '!' and x in operator: 
                parsed[i - 1] = factorial(float(parsed[i - 1]))
                parsed[i:] = parsed[i + 1:]
                i -= 1

            elif x in operator and x in funcs.keys():
                func = funcs[x]

            if func is not None:
                if parsed[i + 1] == '-':
                    parsed[i + 1] += str(parsed[i + 2])
                    parsed[i + 2:] = parsed[i + 3:]

                parsed[i - 1] = func(float(parsed[i - 1]), float(parsed[i + 1]))
                parsed[i:] = parsed[i + 2:]
                i -= 1
            i += 1
    if in_expr:    # no closing brace
        raise ValueError("MA error: missing brace")

    return parsed


def eval_str(expr):
    """Return the final result rounded to 10 decimal places."""
    return round(float(eval_substr(split_expression(expr))[0]), 10)
