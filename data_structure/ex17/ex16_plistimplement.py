def merge_sort(numlist):
    if len(numlist) == 1:
        return numlist
    mid = len(numlist) // 2
    left_list = numlist[:mid]
    right_list = numlist[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

def merge(left, right):
    result = []
    if left == []:
        return right
    elif right == []:
        return left
    while left != [] and right != []:
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)
    if left == [] and right != []:
        result = result + right
    if left != [] and right == []:
        result = result + left
    return result

x = [123, 33, 56, 234, 767, 123 ,564, 122, 567, 44, 324] 

print(x)
print(merge_sort(x))
