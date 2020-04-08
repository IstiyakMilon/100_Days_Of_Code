def solve(meal_cost, tip_percent, tax_percent):
    tip=meal_cost * (tip_percent/100)
    tax=meal_cost * (tax_percent/100)
    totalCost= meal_cost+tip+tax
    return round(totalCost)



meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

print(solve(meal_cost, tip_percent, tax_percent))