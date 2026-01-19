import tracemalloc

tracemalloc.start()

def get_memory_intensive_data():
    return [i for i in range(1000000)]

get_memory_intensive_data()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Memory Source Analysis]")
for stat in top_stats[:10]:
    print(stat)  # Menampilkan baris mana yang menjadi sumber alokasi memori terbanyak
# Fungsi: Mencari tahu dari mana alokasi memori berasal.
# Kondisi: Ketika Anda ingin memahami sumber penggunaan memori dalam aplikasi.