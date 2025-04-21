import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Selamat Datang di Permainan Tebak Angka!")
print(f"Pilih Angka di antara {lowest_num} dan {highest_num}")

while is_running:
    guess = input("Ketikkan Tebakan Kamu: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("Angka Tersebut Melebihi Batas!")
            print(
                f"Tolong Pilih Angka di antara {lowest_num} dan {highest_num}.")
        elif guess < answer:
            print("Terlalu Rendah! Coba Lagi.")
        elif guess > answer:
            print("Terlalu Tinggi! Coba Lagi.")
        else:
            print(f"Benar! Jawabannya adalah {answer}!")
            print(f"Berhasil Setelah Percoban ke-{guesses}")
            is_running = False
    else:
        print("Tebakan Yang Tidak Sah!")
        print(f"Tolong Pilih Angka di antara {lowest_num} dan {highest_num}.")
