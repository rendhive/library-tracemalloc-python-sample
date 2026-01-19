import tracemalloc

tracemalloc.start()

def create_large_structure():
    return {i: [j for j in range(2000)] for i in range(100)}

create_large_structure()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

print("[Top Memory Usage with Traceback]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Melacak penggunaan memori dengan menunjukkan jejak panggilan.
# Kondisi: Ketika Anda ingin mengetahui jejak penggunaan memori secara terperinci.