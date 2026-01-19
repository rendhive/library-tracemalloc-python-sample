import tracemalloc

def create_large_list():
    return [i for i in range(100000)]

tracemalloc.start()
create_large_list()
snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()

top_stats = snapshot.statistics('lineno')

print("[Top 10 Memory Usage]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Mulai dan hentikan pelacakan untuk mengukur penggunaan memori.
# Kondisi: Ketika Anda ingin mengontrol jadwal pelacakan penggunaan memori.