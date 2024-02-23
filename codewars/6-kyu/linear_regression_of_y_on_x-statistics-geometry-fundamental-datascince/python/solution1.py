def regression_line(x: list, y: list) -> tuple:
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    intercept = (sum([i*i for i in x]) * sum(y) - sum(x) * sum([x[i]*y[i] for i in range(0, len(x))])) / (len(x) * sum([i*i for i in x]) - (sum(x)**2))

    slope = (len(x) * sum([x[i]*y[i] for i in range(0, len(x))]) - sum(x) * sum(y)) / (len(x) * sum([i*i for i in x]) - (sum(x)**2))
    
    return (round(intercept, 4), round(slope, 4))
