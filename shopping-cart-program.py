foods = []
prices = []
total = 0

while True:
    food = input("Ketikkan makanan yang kamu beli (q untuk keluar): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Ketikkan harga dari {food} Rp."))
        foods.append(food)
        prices.append(price)

print("---------------- MAKANAN YANG KAMU BELI ----------------")

for food in foods:
    print(food)

print()

for price in prices:
    total += price

print(f"Total Belanjaan Kamu adalah Rp.{total:,.0f}")
