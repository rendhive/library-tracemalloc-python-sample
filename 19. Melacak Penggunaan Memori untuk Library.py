import tracemalloc
import numpy as np

tracemalloc.start()

def allocate_numpy_array():
    return np.zeros((1000, 1000))

allocate_numpy_array()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[Memory Usage for Numpy Allocation]")
for stat in top_stats[:10]:
    print(stat)
# Fungsi: Melacak penggunaan memori dalam pustaka eksternal seperti NumPy.
# Kondisi: Ketika Anda ingin menganalisis dampak pustaka eksternal pada penggunaan memori.