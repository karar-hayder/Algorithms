

def merge_sort(array : list):
    if len(array) > 1:
        ## Split the array in half
        mid = int(len(array) / 2)
        left_half = array[:mid]
        right_half = array[mid:]

        ## Do the same function for each half (recursive)
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        ## Define the Left,Right pointer and the array index
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            ## If the left pointer points to a number less than the right one put in the array at this index
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else: ## If not do the oppoisite 
                array[k] = right_half[j]
                j += 1
            k += 1
        ### If the number is the same in both sides then put them all in the array
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

if __name__ == "__main__":
    import time,random
    list_to_sort = [random.randint(1,99999) for i in range(2000000)]
    st = time.time()
    rs = merge_sort(list_to_sort)
    # print(rs)
    print(time.time() - st)