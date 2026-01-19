import tracemalloc

tracemalloc.start()

# Fungsi sederhana untuk mengalokasikan memori.
def allocate_memory():
    return [i for i in range(1000)]

# Mengalokasikan memori pada fungsi
allocate_memory()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Top 10 Memory Usage]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Menampilkan 10 lokasi yang menghabiskan memori paling banyak.
# Kondisi: Ketika Anda ingin menganalisis penggunaan memori setelah pemanggilan fungsi.