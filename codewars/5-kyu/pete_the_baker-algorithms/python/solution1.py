def cakes(recipe, available):
    result = list()
    
    for key, value in recipe.items():
        if key not in available:
            return 0
        else:
            result.append(available[key] // value)
    
    return min(result)
