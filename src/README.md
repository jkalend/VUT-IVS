# SUPERGUIDE TO MATEMATICKÁ KNIŽNICA

### functions:
- basic math (+, -, *, /)
- exponent (^)
- root (√)
- modulo (%)
- factorial (!)
- modification of operator priority using (, )

### operator priority:
 implemented in following order
> ["(", ")"] > ["!"] > ["^", "√"] > ["-x"] > ["%", "/", "*"] > ["-", "+"]

## OVERVIEW:
all functionality within the library is available through the function eval_str:
> #### input: 
> a string representing the expression to solve
> #### output:
> a single numeric value equal to the result of the mathematical expression

## USAGE:
#### basic math operators:
> ##### examples:
> - ``` eval_str("3 + 4") == 7```
> - ``` eval_str("3 + -4") == -1```
> - ``` eval_str("3*4 + 4") == 16```
> - ``` eval_str("3*-4 - 4") == -12```
> - ``` eval_str("8/-4 - 4*1") == -6```

#### exponent:
> ##### examples:
> - ``` eval_str("3^4") == 81```
> - ``` eval_str("2^-2") == 0.25```
> - ``` eval_str("0^0") == 1```
> - ``` eval_str("0^-9") == MA error```

#### root:
> ##### examples:
> - ``` eval_str("3√27") == 3```
> - ``` eval_str("3√-27") == -3```
> - ``` eval_str("4√81") == 3```
> - ``` eval_str("√4") == 2```
> - ``` eval_str("√-4") == MA error```

#### modulo:
> ##### examples:
> - ``` eval_str("4%5") == 4```
> - ``` eval_str("5%4") == 1```
> - ``` eval_str("-4%5") == 1```
> - ``` eval_str("4%-5") == -1```
> - ``` eval_str("-4%-5") == -4```


#### factorial:
> ##### examples:
> - ``` eval_str("5!") == 120```
> - ``` eval_str("-5!") == -120```
> - ``` eval_str("(-5)!") == MA error```
> - ``` eval_str("0.25!") == MA_error```

#### modification of operator priority:
> ##### examples:
> - ``` eval_str("(4 - 5) * 3") == -3```
> - ``` eval_str("3 / (4 - 3)") == 3```
> - ``` eval_str("(8 - 5)!") == 6```
> - ``` eval_str("√(3*3)") == 3```
> - ``` eval_str("√(3*3") == MA error```