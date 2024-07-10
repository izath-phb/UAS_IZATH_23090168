import pandas as pd
data = {
    'Nama': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma dan Struktur Data 2': [90, 50, 70],
    'Matematika Numerik': [80, 60, 90]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

avg_subjects = df.mean(axis=0, numeric_only=True)
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(avg_subjects)

avg_students = df.mean(axis=1)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(avg_students)