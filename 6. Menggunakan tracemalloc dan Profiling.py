import tracemalloc

def intensive_calculation():
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

tracemalloc.start()
intensive_calculation()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Top Memory Allocation During Calculation]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Melacak memori yang digunakan saat melakukan perhitungan intensif.
# Kondisi: Ketika ingin menganalisis penggunaan sumber daya memori dari operasi berat.