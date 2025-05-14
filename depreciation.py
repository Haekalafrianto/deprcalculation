# main function

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

# console


print("Welcome to Depreciation Calculation")
print("There list of depreciation method \n 1. Straight Line Method \n 2. Double Declining Method \n 3. Sum of the Year")

while True:

    depreciaton = int(input("Please input depreciation you want (1/2/3) "))
    cost = float(input("Please input price of the goods "))
    residue = float(input("Please input the residue of the goods "))
    life = int(input("Please input the ideal life of the goods "))

    if depreciaton == 1:
        print(straight_line_method(cost, residue, life))
    elif depreciaton == 2:
        print(double_declining_method(cost, residue, life))
    elif depreciaton == 3:
        print(sum_of_the_year_method(cost, residue, life))
    else:
        print("Invalid input, can't calculate")

    again = input("Do you want calculate again? (y/n) ")
    if again == "y":
        continue
    elif again == "n":
        print("exiting the programs...")
        break
    else:
        print("invalid input. exiting by default...")
        break 