from ex14 import *
def node_at(numbers, i):
    count = 0
    node = numbers.begin
    while node and count < i:
        node = node.next
        count += 1
    return node

def quick_sort(numbers, lo, hi): # this should be better if it take the node instead of number
    if lo < hi:
        p = quick_sort_partition(numbers, lo, hi) # this should be better if it return a node
        quick_sort(numbers, lo, p - 1)
        quick_sort(numbers, p + 1, hi)

def quick_sort_partition(numbers, lo, hi):
    pivot = node_at(numbers, hi)
    i = lo - 1
    node_j = node_at(numbers, lo)
    if node_j.prev == None:
        numbers.shift('i_save')
        node_i = node_j.prev
        for j in range(lo, hi):
            if node_j.value < pivot.value:
                i += 1
                node_i = node_i.next
                node_i.value, node_j.value = node_j.value, node_i.value
            node_j = node_j.next
        numbers.detach_node(numbers.begin)
    else:
        node_i = node_j.prev
        for j in range(lo, hi):
            if node_j.value < pivot.value:
                i += 1
                node_i = node_i.next
                node_i.value, node_j.value = node_j.value, node_i.value
            node_j = node_j.next

    node_i = node_i.next

    if pivot.value < node_i.value:
        pivot.value, node_i.value = node_i.value, pivot.value

    return i + 1
