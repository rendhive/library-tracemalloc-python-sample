import tracemalloc

def scale_operation(size):
    return [i for i in range(size)]

tracemalloc.start()
scale_operation(10000)
scale_operation(50000)

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Top Memory Usage by Scale]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Mengukur penggunaan memori saat scaling operasi.
# Kondisi: Saat Anda ingin menilai dampak ukuran data pada memori.