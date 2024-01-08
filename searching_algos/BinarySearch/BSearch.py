import string


letters = 'ءاأبتثجحخدذرزسشصضطظعغفقكامنهوي' + '0123456789' +string.punctuation

letters_indexes = {}
for dx,i in enumerate(letters):
    letters_indexes[i] = dx

for dx,i in enumerate(string.ascii_lowercase):
    letters_indexes[i] = dx


for dx,i in enumerate(string.ascii_uppercase):
    letters_indexes[i] = dx


def binery_search(arr:list,target,letters_indexing=False):
    if len(arr) <= 0:
        return False

    if len(arr) == 1 and target != arr[0]:
        return False

    
    if letters_indexing != False:
        target = target.lower()
    pivot_ind = int(len(arr) / 2)
    
    pivot = arr[pivot_ind]
    
    if letters_indexing:
        pivot = pivot.lower()
        if len(pivot) >=len(target):
            if target == pivot:
                return pivot

        ### Check if there is a different letter between the target and the pivot
        for letter in range(len(target)):    
            ### If the letter is different and it appears later in the alphabit than the pivot take the second half
            if letters_indexes[target[letter]] > letters_indexes[pivot[letter]]:
                return binery_search(arr[pivot_ind:],target,letters_indexing)
            ### The oppisit
            elif letters_indexes[target[letter]] < letters_indexes[pivot[letter]]:
                return binery_search(arr[:pivot_ind],target,letters_indexing)
            ### else it means they have the same letter at the same location so pass on it
        else:
            return False
    else:
        if pivot == target:
            return pivot
        
        if target > pivot:
            return binery_search(arr[pivot_ind:],target)
        else:
            return binery_search(arr[:pivot_ind],target)


if __name__ =="__main__":
    print(binery_search(
                        [1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 23, 35, 46, 52, 63, 423, 423, 463, 523]
                        ,4
                    ))