import tracemalloc

tracemalloc.start()

def my_function():
    _ = [i for i in range(100000)]

my_function()
snapshot = tracemalloc.take_snapshot()

for stat in snapshot.statistics('lineno'):
    print(stat)
# Fungsi: Menampilkan semua alokasi memori berdasarkan posisi baris.
# Kondisi: Ketika ingin mendapatkan gambaran menyeluruh tentang alokasi memori pada suatu titik.