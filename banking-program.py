# Python Banking Program

def show_balance(balance):
    print(f"Jumlah Saldo Kamu Adalah Rp.{balance:.3f}")


def deposit():
    amount = float(input("Ketikkan Jumlah Uang Yang Ingin Di Deposito: "))

    if amount < 0:
        print("Jumlah Yang Tidak Valid!")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Ketikkan Jumlah Uang Yang Ingin di Tarik: "))

    if amount > balance:
        print("Saldo Tidak Cukup")
        return 0
    elif amount < 0:
        print("Jumlah Saldo Harus Lebih Dari 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------------------------------------------------------")
        print("Python Banking Program")
        print("---------------------------------------------------------")
        print("Silahkan pilih salah satu dari 4 opsi berikut :")
        print("1. Tampilkan Saldo")
        print("2. Deposit")
        print("3. Tarik Saldo")
        print("4. Keluar")

        choice = int(input("Ketikkan Pilihan Anda (1-4): "))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("Input Yang Diberikan Tidak Valid!")

    print("Terimakasih Telah Menggunakan Program Ini!")


if __name__ == '__main__':
    main()
