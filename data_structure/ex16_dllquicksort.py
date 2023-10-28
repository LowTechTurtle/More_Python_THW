from ex14 import *
def node_at(numbers, i):
    count = 0
    node = numbers.begin
    while node and count < i:
        node = node.next
        count += 1
    return node

def quick_sort(numbers, lo, hi):
    if lo < hi:
        p = quick_sort_partition(numbers, lo, hi)
        quick_sort(numbers, lo, p - 1)
        quick_sort(numbers, p + 1, hi)

def quick_sort_partition(numbers, lo, hi):
    pivot = node_at(numbers, hi)
    i = lo - 1

    for j in range(lo, hi):
        node_j = node_at(numbers, j)
        if node_j.value < pivot.value:
            i += 1
            if i != j:
                node_i = node_at(numbers, i)
                node_i.value, node_j.value = node_j.value, node_i.value

    node_hi = node_at(numbers, hi)
    node_i = node_at(numbers, i + 1)

    if node_hi.value < node_i.value:
        node_hi.value, node_i.value = node_i.value, node_hi.value

    return i + 1

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
quick_sort(dll, 0, dll.count() - 1)

node = dll.begin

print('Sorted list:')
i = 1
while node:
    print(f'{i} {node.value}')
    node = node.next
    i += 1
