nilai = 82
kehadiran = 90 

print("--- Data Awal (Nilai: 82, Kehadiran: 90) ---")

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("Apakah nilai >= 75?", syarat_nilai)
print("Apakah kehadiran >= 80%?", syarat_kehadiran)

status_lulus = syarat_nilai and syarat_kehadiran
print("Status kelulusan (AND):", status_lulus)


print("\n--- Setelah Nilai Diubah Menjadi 70 ---")
nilai = 70

syarat_nilai = nilai >= 75 
status_lulus_baru = syarat_nilai and syarat_kehadiran

print("Apakah nilai baru >= 75?", syarat_nilai)
print("Status kelulusan baru (AND):", status_lulus_baru)

status_lulus_or = syarat_nilai or syarat_kehadiran
print("Status kelulusan dengan OR:", status_lulus_or)