def luas_persegi_panjang(p, l):
    return p * l
def luas_segitiga(a, t):
    return 0.5 * a * t
def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil
def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA MODULAR ===")
    print("1. Luas Persegi Panjang")
    print("2. Luas Segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
def utama():
    tampilkan_menu()
    pilihan = input("Pilihan menu (1-4): ")
    if pilihan == "1":
        p = float(input("Panjang: "))
        l = float(input("Lebar  : "))
        print("Luas =", luas_persegi_panjang(p, l))
    elif pilihan == "2":
        a = float(input("Alas  : "))
        t = float(input("Tinggi: "))
        print("Luas =", luas_segitiga(a, t))
    elif pilihan == "3":
        n = int(input("Nilai n: "))
        if n >= 0:
            print("Jumlah 1..n =", jumlah_n(n))
        else:
            print("n harus nonnegatif!")
    elif pilihan == "4":
        n = int(input("Nilai n: "))
        if n >= 0:
            print("Faktorial =", faktorial(n))
        else:
            print("n harus nonnegatif!")
    else:
        print("Pilihan tidak valid.")
if __name__ == "__main__":
    utama()