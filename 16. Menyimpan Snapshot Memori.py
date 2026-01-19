import tracemalloc
import pickle

tracemalloc.start()

def allocate_memory():
    return [i for i in range(300000)]

allocate_memory()
snapshot = tracemalloc.take_snapshot()

# Menyimpan snapshot ke file
with open("snapshot.pkl", "wb") as f:
    pickle.dump(snapshot, f)

print("Snapshot telah disimpan ke snapshot.pkl")
# Fungsi: Menyimpan snapshot penggunaan memori untuk analisis lebih jauh.
# Kondisi: Ketika Anda ingin menyelamatkan keadaan penggunaan memori untuk diteliti nanti.