def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input("Введите количество чисел: "))

numbers = []
for i in range(n):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

direction = input("Выберите направление сортировки (по возрастанию/по убыванию): ").strip().lower()
ascending = True if direction == "по возрастанию" else False
bubble_sort(numbers, ascending)
if ascending:
    print("Числа после сортировки по возрастанию:")
else:
    print("Числа после сортировки по убыванию:")
print(numbers)
