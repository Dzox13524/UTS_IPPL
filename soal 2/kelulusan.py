def evaluasi_kelulusan(kehadiran, nilai, pembayaran):
    if not (0 <= kehadiran <= 100) or not (0 <= nilai <= 100):
        return "Error: Input nilai/kehadiran harus 0-100"
    
    status_pembayaran = pembayaran.strip().lower()
    
    if kehadiran >= 75 and nilai >= 60 and status_pembayaran == "lunas":
        return "LULUS"
    else:
        return "TIDAK LULUS"

test_cases = [
    (80, 85, "Lunas"),
    (80, 85, "Belum Lunas"),
    (80, 50, "Lunas"),
    (60, 90, "Lunas"),
    (60, 50, "Belum Lunas"),
    (75, 60, "Lunas")
]

print("--- HASIL PENGUJIAN ---")
for i, (k, n, p) in enumerate(test_cases, 1):
    hasil = evaluasi_kelulusan(k, n, p)
    print(f"T-0{i}: {hasil}")
