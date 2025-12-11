price = int(input("Enter price:\n"))
discount = int(input("Enter discount(%):\n"))

final_price = price * (1 - discount / 100)

print(f"Final price: {final_price}")
