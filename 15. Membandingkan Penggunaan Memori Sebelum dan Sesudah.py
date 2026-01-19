import tracemalloc

tracemalloc.start()

def process_step_one():
    return [i for i in range(100000)]

process_step_one()
snapshot_before = tracemalloc.take_snapshot()

def process_step_two():
    return [i for i in range(200000)]

process_step_two()
snapshot_after = tracemalloc.take_snapshot()

diff = snapshot_after.compare_to(snapshot_before, 'lineno')
print("[Memory Usage Difference]")
for stat in diff[:10]:
    print(stat)
# Fungsi: Membandingkan penggunaan memori sebelum dan sesudah fungsi.
# Kondisi: Ketika ingin melihat perubahan penggunaan memori setelah langkah penting dalam proses.