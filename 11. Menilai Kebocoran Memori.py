import tracemalloc

tracemalloc.start()

def memory_leak():
    leak = []
    for i in range(100000):
        leak.append((i, [0] * (i + 1)))

memory_leak()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Possible Memory Leak Detected]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Mendeteksi kemungkinan kebocoran memori akibat akumulasi objek.
# Kondisi: Saat Anda ingin memeriksa dan mendiagnosis kebocoran memori.