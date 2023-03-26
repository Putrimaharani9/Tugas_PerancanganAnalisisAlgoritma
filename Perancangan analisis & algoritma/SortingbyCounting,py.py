def pengurutan_jumlah_kemunculan(arr):
    n = len(arr)
    maksimal = max(arr)
    frekuensi = [0] * (maksimal+1)
    urutkan = [0] * n

    # menghitung frekuensi kemunculan setiap nilai pada array
    for i in range(n):
        frekuensi[arr[i]] += 1

    # menjumlahkan frekuensi nilai-nilai sebelumnya pada array frekuensi
    for i in range(1, maksimal+1):
        frekuensi[i] += frekuensi[i-1]

    # memindahkan nilai dari arr ke urutkan secara terurut
    for i in range(n-1, -1, -1):
        urutkan[frekuensi[arr[i]]-1] = arr[i]
        frekuensi[arr[i]] -= 1

    return urutkan

# contoh penggunaan
data = [4, 2, 1, 4, 6, 5, 2]
urutan = pengurutan_jumlah_kemunculan(data)
print("Urutan dari data tersebuat adalah",urutan) # Output: [1, 2, 2, 4, 4, 5, 6]
