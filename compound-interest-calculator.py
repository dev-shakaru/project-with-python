# Perhitungan Bunga Majemuk pada Python

n = 0
modal_awal = 0
besar_bunga = 0

while modal_awal <= 0:
    modal_awal = float(input("Ketikkan Modal Awal: "))
    if modal_awal <= 0:
        print("modal awal tidak dapat nol dan kurang dari nol.")
print(f"Modal Awalnya adalah Rp.{modal_awal:,.0f}")

while besar_bunga <= 0:
    besar_bunga = float(input("Ketikkan Presentase Besaran Bunga: "))
    if besar_bunga <= 0:
        print("presentase besaran bunga tidak boleh nol dan kurang dari nol")
print(f"Besaran Bunga Dalam Presentasenya Adalah {besar_bunga:.0f}%")

while n <= 0:
    n = int(input("Ketikkan Waktu Yang Mau Dihitung (Dalam Tahun): "))
    if n <= 0:
        print("Waktu Yang Mau Dihitung (Dalam Tahun) tidak boleh nol dan kurang dari nol")
print(f"Waktu Yang Mau Kamu Hitung Adalah (Dalam Tahun) {n}")

hasil = modal_awal * pow((1 + (besar_bunga/100)), n)

print(
    f"Hasil Perhitungan Bunga Majemuknya dalam kurun waktu {n} tahun adalah Rp.{hasil:,.0f}")
