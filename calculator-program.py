# Simple Calculator Program

operasiMatematika = input(
    "Operasi Matematika Apa Yang Mau Kamu Lakukan? (+, -, *, /): ")

numA = float(input("Masukkan Angka Pertama: "))
numB = float(input("Masukkan Angka Kedua: "))

if operasiMatematika == "+":
    hasil = numA + numB
    print(f"Hasil penjumlahannya adalah: {hasil}")
elif operasiMatematika == "-":
    hasil = numA - numB
    print(f"Hasil pengurangannya adalah: {hasil}")
elif operasiMatematika == "*":
    hasil = numA * numB
    print(f"Hasil perkaliannya adalah: {hasil}")
elif operasiMatematika == "/":
    hasil = numA / numB
    print(f"Hasil pembagiannya adalah: {hasil}")
else:
    print("Mohon Masukkan Operasi Matematika Berikut: (Penjumalahan +) (Pengurangan -) (Perkalian *) (Pembagian /)")
