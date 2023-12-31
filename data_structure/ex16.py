from ex14 import *
def count(node):
    count = 0

    while node:
        node = node.next
        count += 1

    return count


def merge_sort(numbers):
    numbers.begin = merge_node(numbers.begin)

    # horrible way to get the end
    node = numbers.begin
    while node.next:
        node = node.next
    numbers.end = node


def merge_node(start):
    """Sorts a list of numbers using merge sort."""
    if start.next == None:
        return start

    mid = count(start) // 2

    # scan to the middle
    scanner = start
    for i in range(0, mid-1):
        scanner = scanner.next

    # set mid node right after the scan point
    mid_node = scanner.next
    # break at the mid point
    scanner.next = None
    mid_node.prev = None
   
    merged_left = merge_node(start)
    merged_right = merge_node(mid_node)

    return merge(merged_left, merged_right)

def merge(left, right):
    """Performs the merge of two lists."""
    result = None

    if left == None: return right
    if right == None: return left

    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)

    result.next.prev = result
    return result

from random import randint
dll = DLL()
for i in range(0, randint(10, 16)):
    num = randint(1, 1000)
    dll.push(num)

print('Unsorted list:')
node = dll.begin
i = 1
while node:
    print(f'{i} {node.value}')
    node = node.next
    i += 1
merge_sort(dll)

node = dll.begin

print('Sorted list:')
i = 1
while node:
    print(f'{i} {node.value}')
    print(node)
    node = node.next
    i += 1




