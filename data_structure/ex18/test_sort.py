import quick_sort, merge_sort, sorting
from ex14 import DLL
from random import randint

max_numbers = 900

def random_list(count):
    numbers = DLL()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers

def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value: 
            return False
        else:
            node = node.next
    return True

def test_bubble_sort():
    numbers = random_list(max_numbers)
    sorting.bubble_sort(numbers)
    assert is_sorted(numbers)

def test_merge_sort():
    numbers = random_list(max_numbers)
    merge_sort.merge_sort(numbers)
    assert is_sorted(numbers)

def test_quick_sort():
    numbers = random_list(max_numbers)
    quick_sort.quick_sort(numbers, 0, numbers.count() - 1)

if __name__ == "__main__":
    for i in range(0, 10):
        test_bubble_sort()
        test_merge_sort()
        test_quick_sort()
