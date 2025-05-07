def straight_line_method(cost, residue, life):
    annualdep = (cost - residue)/ life
    return [round(annualdep)] * life

def double_declining_method(cost, residue, life):
    rate = 2 / life
    values = []
    for year in range(1, life + 1):
        depreciation = cost * rate
        if cost - depreciation < residue:
            depreciation = cost - residue
        values.append(round(depreciation, 2))
        cost -= depreciation
    return(values)

def sum_of_the_year_method(cost, residue, life):
    total = life * (life + 1) / 2
    values = []
    for year in range(life):
        factor = (life - year) / total
        depreciation = (cost - residue) * factor
        values.append(round(depreciation, 2))
    return values