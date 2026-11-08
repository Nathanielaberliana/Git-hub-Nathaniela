print("Kalkulator penjumlahan. Ketik 'q' kapan saja untuk keluar.")

while True:
    first_number = input("\nMasukkan angka pertama: ")
    if first_number == 'q':
        break

    second_number = input("Masukkan angka kedua: ")
    if second_number == 'q':
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Mohon maaf, kamu harus memasukkan angka, bukan teks.")
    else:
        print(f"Hasil penjumlahan: {total}")
        