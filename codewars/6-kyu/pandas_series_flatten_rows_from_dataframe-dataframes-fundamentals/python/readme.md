# Flatten Rows From DataFrame
## Input parameters
1. dataframe: `pandas.DataFrame` object
2. col: target column

## Task
Your function must return a new `pandas.DataFrame` object with the same columns as the original input. However, targeted column has in some of its cells a list instead of one single element.You must transform each element of a list-like cell to a row.

Input DataFrame will never be empty. You must not modify the original input. The target column will always be one of the dataframe columns.

## Examples
### Input
```
  A         B
0 [1, 2]    5
1 [a, b, c] 6
2 77        3      

col = "A"
```
### Output
```
   A  B
0  1  5
1  2  5
2  a  6
3  b  6
4  c  6
5  77 3
```
