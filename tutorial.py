def bubble_sort(data):
  n = len(data)

  for i in range(n):
    swapped = False

#loop untuk membandingkan dan menukar elemen
    for j in range(n - 1 - i):
      if data[j] > data[j ++ 1]:
        data[j], data[j+1] = data[j+1], data[j]
        swapped = True

    if not swapped:
      break # perulangan akan berhenti jika data sudah terurut

# Contoh Pengurutan Bilangan
data = [10, 9, 8, 7, 100.000, 5, 4, 3, 2, 1]
print("data sebelum di urutkan:", data)

bubble_sort(data)
print("Data setelah diurutkan:", data)