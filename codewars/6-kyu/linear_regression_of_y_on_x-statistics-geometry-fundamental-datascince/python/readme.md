# Background:
![linear regression](http://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/438px-Linear_regression.svg.png)

A linear regression line has an equation in the form $Y = a + bX$, where $X$ is the explanatory variable and $Y$ is the dependent variable. The parameter $b$ represents the *slope* of the line, while $a$ is called the *intercept* (the value of $y$ when $x$ = 0).
For more details visit the related [wikipedia page](http://en.wikipedia.org/wiki/Simple_linear_regression).

## Task:
The function that you have to write accepts two list/array, $x$ and $y$, representing the coordinates of the points to regress (so that, for example, the first point has coordinates (`x[0], y[0]`)).

Your function should return a tuple (in Python) or an array (any other language) of two elements: `a` (intercept) and `b` (slope) in this order.

You must round your result to the first 4 decimal digits

## Formula:
$x_i$ and $y_i$ is $x$ and $y$ co-ordinate of $i$-th point;
$n$ is length of input.

$a = \frac{{n\sum x_i^2 ⋅ \sum y_i - \sum x_i ⋅ \sum x_i y_i}}{{n\sum x_i^2 - (\sum x_i)^2}}$

$b = \frac{{n\sum x_i y_i - \sum x_i ⋅ (\sum y_i)}}{{n\sum x_i^2 - (\sum x_i)^2}}$

## Examples:
```
regressionLine([25,30,35,40,45,50], [78,70,65,58,48,42]) == (114.381, -1.4457)

regressionLine([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155]) == (80.7777, 1.138)
```
