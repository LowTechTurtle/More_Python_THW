from ex14 import * 
def count(begin):
    i = 1
    while begin.next:
        begin = begin.next
        i += 1
    return i

def merge_sort(numbers):
#we need to set numbers.begin because if not, number.begins will still be the begin node of the first list
    numbers.begin = merge_node(numbers.begin)

    node = numbers.begin
    while node.next:
        node = node.next
    numbers.end = node

def merge_node(begin):
    if begin.next == None:
        return begin
    mid = count(begin) // 2
    mid_node = begin
    for i in range(0, mid):
        mid_node = mid_node.next
    mid_node.prev.next = None
    mid_node.prev = None
    
    merge_left = merge_node(begin)
    merge_right = merge_node(mid_node)
    
    return merge(merge_left, merge_right)

def merge(left, right):
    result = None
    #there might be an error cant return an undefined var
    if left == None:
        return right
    if right == None:
        return left
    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)
    result.next.prev = result

    return result
