price = int(input("Enter price:\n"))
discount = int(input("Enter discount(%):\n"))

final_price = price - price*discount/100

print("Final price: " + str(final_price))
