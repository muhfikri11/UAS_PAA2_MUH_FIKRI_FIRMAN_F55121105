import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return arr, execution_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    
    for i in range(1, n):
        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return arr, execution_time

def print_iterations(arr):
    print("5 Iterasi Pertama:")
    for i in range(5):
        print(arr[i], end=" ")
    print("\n")
    
    print("5 Iterasi Terakhir:")
    for i in range(len(arr)-5, len(arr)):
        print(arr[i], end=" ")
    print("\n")

def print_execution_time(execution_time):
    print("Waktu Komputasi Pengurutan: %.6f detik\n" % execution_time)

def print_before_after(arr, sorted_arr):
    print("Sebelum Pengurutan:")
    print(arr)
    print("\nSetelah Pengurutan:")
    print(sorted_arr)
    print("\n")

def bubble_sort_analysis():
    print("Bubble Sort Analysis:")
    print("1. Worst Case: O(n^2)")
    print("   - Terjadi ketika array terurut secara terbalik. Setiap elemen harus ditukar di setiap iterasi.")
    print("2. Best Case: O(n)")
    print("   - Terjadi ketika array sudah terurut secara membesar. Tidak ada pertukaran elemen yang dilakukan.")
    print("3. Average Case: O(n^2)")
    print("   - Memiliki kompleksitas yang sama dengan worst case karena algoritma bubble sort selalu melakukan perbandingan dan pertukaran pada setiap elemen.\n")

def insertion_sort_analysis():
    print("Insertion Sort Analysis:")
    print("1. Worst Case: O(n^2)")
    print("   - Terjadi ketika array terurut secara terbalik. Pada setiap iterasi, semua elemen sebelum elemen saat ini harus digeser.")
    print("2. Best Case: O(n)")
    print("   - Terjadi ketika array sudah terurut secara membesar. Tidak ada pergeseran elemen yang dilakukan.")
    print("3. Average Case: O(n^2)")
    print("   - Pada kasus rata-rata, setiap elemen perlu digeser sekitar setengah jarak ke kanan.\n")

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]
    
    print("Sebelum pengurutan:")
    print(arr)
    print("\n")
    
    choice = input("Pilih metode pengurutan (bubble/insertion): ")
    
    if choice.lower() == "bubble":
        sorted_arr, execution_time = bubble_sort(arr.copy())
        print_iterations(sorted_arr)
        print_execution_time(execution_time)
        print_before_after(arr, sorted_arr)
        bubble_sort_analysis()
    elif choice.lower() == "insertion":
        sorted_arr, execution_time = insertion_sort(arr.copy())
        print_iterations(sorted_arr)
        print_execution_time(execution_time)
        print_before_after(arr, sorted_arr)
        insertion_sort_analysis()
    else:
        print("Pilihan tidak valid. Silakan pilih 'bubble' atau 'insertion'.")
    
if __name__ == '__main__':
    main()
