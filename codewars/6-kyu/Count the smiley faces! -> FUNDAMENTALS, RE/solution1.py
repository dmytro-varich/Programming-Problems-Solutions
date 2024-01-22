def count_smileys(arr):
    count = 0
    noses = ['-', '~']
    smiles = [')', 'D']             
    
    for item in arr:
        if len(item) == 2:
            if item[1] in smiles:
                count += 1
        else:
            if item[1] in noses and item[2] in smiles:
                count += 1
                
    return count
