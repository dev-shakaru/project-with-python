menu = {"popcorn": 20.000,
        "air mineral": 5.000,
        "air lemon": 7.000, }
cart = []
total = 0

print("---------------- MENU ----------------")
for key, value in menu.items():
    print(f"{key:20}: {value:.3f}")
print("--------------------------------------")

while True:
    food = input(
        "Silahkan Pilih Item Yang Kamu Mau (q untuk Keluar): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------------- ORDERAN KAMU ----------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total Belanjaan = Rp.{total:.3f}")
