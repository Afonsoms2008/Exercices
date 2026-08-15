def taxes(tax,cost):
    cost_post_taxes = cost + (cost / 100 * tax)
    print(f"the cost post taxes is {cost_post_taxes}")
tax = int(input("Introduce the % that will be added to the cost of the product: "))
cost= int(input("Insert the cost of the product before taxes: "))
taxes(tax,cost)