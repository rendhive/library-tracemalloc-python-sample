import tracemalloc

tracemalloc.start()

def test_usage():
    data = [i for i in range(100000)]
    return data

test_usage()
snapshot = tracemalloc.take_snapshot()
print("[Diagnostic Memory Usage]")
top_stats = snapshot.statistics('traceback')
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Menggunakan tracemalloc untuk diagnostic tracing dari pelacakan penggunaan memori.
# Kondisi: Ketika Anda perlu melakukan analisis mendalam tentang penggunaan memori dalam aplikasi besar.