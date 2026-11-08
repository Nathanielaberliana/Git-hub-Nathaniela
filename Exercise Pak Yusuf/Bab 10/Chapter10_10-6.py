first_number = input("Masukkan angka pertama: ")
second_number = input("Masukkan angka kedua: ")

try:
    total = int(first_number) + int(second_number)
except ValueError:
    print("Mohon maaf, kamu harus memasukkan angka, bukan teks.")
else:
    print(f"Hasil penjumlahan: {total}")
    