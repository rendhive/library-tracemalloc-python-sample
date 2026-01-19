import tracemalloc

tracemalloc.start()

def function_a():
    return [i for i in range(25000)]

def function_b():
    return [i for i in range(12500)]

function_a()
snap_a = tracemalloc.take_snapshot()

function_b()
snap_b = tracemalloc.take_snapshot()

stats_a = snap_a.statistics('lineno')
stats_b = snap_b.statistics('lineno')

print("[Memory Usage Function A]")
for stat in stats_a[:10]:
    print(stat)

print("[Memory Usage Function B]")
for stat in stats_b[:10]:
    print(stat)
# Fungsi: Pelacakan penggunaan memori untuk setiap fungsi secara terpisah.
# Kondisi: Ketika ingin mengetahui dampak dari fungsi tertentu secara lebih mendalam.