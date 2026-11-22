pizza = int(input( "how many pizzas do you want?"))
price = int(input( "what is the cost of one?"))
total = pizza * price
tax = total / 100 * 8
print(" your price is £,", tax + total)

