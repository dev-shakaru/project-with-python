import random

options = ("Batu", "Gunting", "Kertas")
berjalan = True

print("Selamat Datang di Permainan Batu, Gunting, Kertas yang Dibuat Menggunakan Python")
print("Ketikkan Pilihanmu di antara Batu, Gunting, Kertas, atau ketik 'Keluar' untuk berhenti bermain.")

while berjalan:
    # Pilihan komputer diperbarui setiap iterasi
    computer = random.choice(options)
    choices = input(
        "Ketikkan Pilihanmu Disini (Batu, Gunting, Kertas, Keluar): ").capitalize()

    if choices == "Keluar":
        print("Terima kasih telah bermain! Sampai jumpa.")
        break
    # Memvalidasi agar user hanya dapat mengetikkan Batu, Gunting atau Kertas
    elif choices in options:
        print(
            f"Pilihanmu adalah {choices} sedangkan lawanmu adalah {computer}")
        if choices == computer:
            print("SERI!")
        elif (choices == "Batu" and computer == "Gunting") or \
             (choices == "Gunting" and computer == "Kertas") or \
             (choices == "Kertas" and computer == "Batu"):
            print("KAMU MENANG!")
            berjalan = False
        else:
            print("KAMU KALAH!")
    else:
        print("Tidak Valid! Ketikkan Batu, Gunting, atau Kertas.")
