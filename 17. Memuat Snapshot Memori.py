import tracemalloc
import pickle

# Memuat snapshot dari file
with open("snapshot.pkl", "rb") as f:
    loaded_snapshot = pickle.load(f)

print("[Restoring Memory Snapshot]")
for stat in loaded_snapshot.statistics('lineno')[:10]:
    print(stat)
# Fungsi: Memuat snapshot memori dari file yang sudah disimpan.
# Kondisi: Ketika Anda ingin menganalisis memori dalam konteks yang disimpan.