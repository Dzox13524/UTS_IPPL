def hitung_akademik(tugas, uts, uas):
    if tugas is None or uts is None or uas is None:
        return "Error: Input tidak boleh kosong"

    for nilai, nama in [(tugas, "Tugas"), (uts, "UTS"), (uas, "UAS")]:
        if isinstance(nilai, bool) or not isinstance(nilai, (int, float)):
            return "Error: Input harus bertipe numerik"

    if not (0 <= tugas <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
        return "Error: Input harus berada dalam rentang 0-100"

    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    if nilai_akhir >= 85:
        grade = 'A'
    elif nilai_akhir >= 75:
        grade = 'B'
    elif nilai_akhir >= 65:
        grade = 'C'
    elif nilai_akhir >= 50:
        grade = 'D'
    else:
        grade = 'E'

    return {"score": round(nilai_akhir, 2), "grade": grade}

def main():
    try:
        raw_tugas = input("Masukkan Nilai Tugas: ")
        raw_uts   = input("Masukkan Nilai UTS  : ")
        raw_uas   = input("Masukkan Nilai UAS  : ")

        def proses_input(val):
            if val == "":
                return None
            if val.isspace():
                return "Spasi"
            try:
                if val.lower() in ["true", "false"]:
                    return bool(val)
                return float(val)
            except ValueError:
                return val

        tugas = proses_input(raw_tugas)
        uts   = proses_input(raw_uts)
        uas   = proses_input(raw_uas)

        hasil = hitung_akademik(tugas, uts, uas)

        if isinstance(hasil, dict):
            print("\n--- HASIL BERHASIL ---")
            print(f"Nilai Akhir : {hasil['score']}")
            print(f"Grade       : {hasil['grade']}")
        else:
            print(f"\n{hasil}")

    except Exception:
        print("\nError: Format input tidak valid")

if __name__ == "__main__":
    main()
