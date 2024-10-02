# 병합 정렬

arr = [int(x) for x in input().split()]

def merge_sort(arr, step_count=[0]):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    
    low_arr = merge_sort(arr[:mid], step_count)
    print(f"\n재귀 직전의 배열: {arr}")
    print(f"재귀 후 반환 low 배열: {low_arr}")
    high_arr = merge_sort(arr[mid:], step_count)
    
    step_count[0] += 1
    current_step = step_count[0]
    
    merged_arr = []
    low = high = 0
    
    print(f"\n Step {current_step}:")
    
    while low < len(low_arr) and high < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else :
            merged_arr.append(high_arr[h])
            h += 1
            
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    return merged_arr

# 퀵 정렬

def quick_sort(arr):
    # 예외 상황. len이 1일 때 종료
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
            
    return quick_sort(leser_arr) + equal_arr + quick_sort(greater_arr)