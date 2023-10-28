def quicksort(nums, begin, end): #when run on the whole list, we do end = len(nums)
    if  begin >= end or begin < 0:
        return None

    p = partition(nums, begin, end)

    quicksort(nums, begin, p - 1)
    quicksort(nums, p + 1 , end)

def partition(nums, begin, end):
    pivot = nums[end]
    i = begin - 1
    j = begin
    while j <= end-1:
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    i += 1
    nums[i], nums[end] = nums[end], nums[i]
    return i



x = [32, 65, 21, 56 ,12 ,685 ,3245, 2, 12]
quicksort(x, 0, len(x) - 1)
print(x)

