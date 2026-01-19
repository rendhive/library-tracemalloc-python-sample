import tracemalloc

tracemalloc.start()

def allocate_first():
    return [i for i in range(10000)]

def allocate_second():
    return [i for i in range(5000)]

allocate_first()
allocate_second()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Top 10 Memory Usage for Multiple Functions]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Melacak penggunaan memori selama pemanggilan beberapa fungsi.
# Kondisi: Ketika Anda ingin mendapatkan gambaran yang lebih lengkap tentang alokasi memori.