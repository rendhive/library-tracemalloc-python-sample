import tracemalloc

tracemalloc.start()

def leak_memory():
    leaked_data = []
    for i in range(100000):
        leaked_data.append(str(i) * 100)

leak_memory()
snapshot = tracemalloc.take_snapshot()

print("[Possible Memory Leak Stats]")
top_stats = snapshot.statistics('traceback')
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Untuk mengidentifikasi jejak panggilan yang mungkin menunjukkan kebocoran memori.
# Kondisi: Ketika Anda ingin mendiagnosis bagian dari kode yang menyebabkan penggunaan memori berlarut.