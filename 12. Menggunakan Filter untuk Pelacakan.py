import tracemalloc

tracemalloc.start()

def filter_memory():
    return [i for i in range(50000)]

filter_memory()
snapshot = tracemalloc.take_snapshot()
filtered_stats = snapshot.statistics('lineno')

# Hanya menampilkan lokasi alokasi memori di baris tertentu
print("[Memory Usage Filtered by Line]")
for stat in filtered_stats[:10]:
    if stat.size > 100000:  # Hanya menampilkan yang lebih besar dari 100KB
        print(stat)
# Fungsi: Menerapkan filter untuk memfokuskan pada penggunaan memori tertentu.
# Kondisi: Ketika ingin mempersempit analisis penggunaan memori berdasarkan kriteria.