import tracemalloc

tracemalloc.start()

def memory_intensive_function():
    large_list = [i for i in range(10**6)]
    return large_list

memory_intensive_function()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('function')

print("[Top Memory Usage by Function]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Mengukur penggunaan memori dan membandingkan penggunaan berdasarkan fungsi.
# Kondisi: Ketika ingin mengetahui fungsi mana yang paling besar mempengaruhi memori.