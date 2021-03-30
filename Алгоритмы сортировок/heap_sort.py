def heapify(nums, heap_size, root_index):
    # Предположим, что индекс самого большого элемента является корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня является допустимым индексом, а элемент больше
    # чем текущий самый большой элемент, то обновляем самый большой элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Делайте то же самое для right_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если самый большой элемент больше не является корневым элементом, меняем их местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Создаем Max Heap из списка
    # Второй аргумент означает, что мы останавливаемся на элементе перед -1, то есть на первом элементе списка.
    # Третий аргумент означает, что мы повторяем в обратном направлении, уменьшая количество i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень max hea в конец
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


# Проверяем, что все работает
random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)