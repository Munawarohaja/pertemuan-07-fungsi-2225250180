def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("Jumlah 1..10 :", jumlah_n(10))
print("Jumlah 1..100:", jumlah_n(100))