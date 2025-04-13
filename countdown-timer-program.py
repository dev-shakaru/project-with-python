# Countdown Timer Program
import time
setTimer = int(input("Ketikkan Waktu: "))

# Awalnya dari setTimer, akhirnya sampai 0 dan dimulai dari setTimer karena stepnya -1
for n in range(setTimer, 0, -1):
    seconds = n % 60
    minutes = int(n/60) % 60
    hours = int(n/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # Berfungsi untuk membuat delay 1 detik di setiap iterasi
    time.sleep(1)
