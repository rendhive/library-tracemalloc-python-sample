import tracemalloc

tracemalloc.start()

def failed_allocation():
    # Menggunakan list comprehension yang membutuhkan memori beberapa kali
    _ = [i ** 2 for i in range(10**7)]

try:
    failed_allocation()
except MemoryError:
    snapshot = tracemalloc.take_snapshot()
    print("[Memory Allocation Failure]")
    top_stats = snapshot.statistics('lineno')
    for stat in top_stats[:10]:
        print(stat)
# Fungsi: Mendeteksi penggunaan memori yang tidak berhasil.
# Kondisi: Ketika Anda ingin menganalisis kegagalan alokasi memori.