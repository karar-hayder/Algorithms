import string
letters = 'ءاأبتثجحخدذرزسشصضطظعغفقكامنهوي' + '123456789' +string.punctuation

letters_indexes = {}

## Giving every letter, number and punctuation that are strings an index in order to sort it like a integer

for dx,i in enumerate(letters):
    letters_indexes[i] = dx

for dx,i in enumerate(string.ascii_lowercase):
    letters_indexes[i] = dx


# for dx,i in enumerate(string.ascii_uppercase):
#     letters_indexes[i] = dx


## for a list with numbers use quickSort([int,int,int])

## for a list with strings use quickSort([str,str,str],True)

def quickSort(arr:list,letters_indexing=False):
    if len(arr) <= 1:
        return arr    
    ## Getting the middle element of the list
    pivot_ind = int(len(arr) / 2)
   
    pivot = arr[pivot_ind]
    ## removing it for the list
    arr.pop(pivot_ind)

    right_list = []
    left_list = []
    ## if it's not a list of strings then it's a list of integers so we can compare them
    if not letters_indexing:
        for i in arr:
            if i < pivot:
                left_list.append(i)
            else:
                right_list.append(i)

    ## else if it's a list of strings then use the indexes to compare them
    else:
        ## lowering them because i only used lower case letters 
        ## if you want you can uncomment the for loop un line 15,16 to add upper case letters and delete the .lower() down here

        pivot = pivot.lower()
        for i in arr:
            ## count used to loop every letter in the word in case the two words are nearly or entirely similar
            letter_count = 0
            word :str = i.lower() 
            
            for n in range(len(word)):

                if letters_indexes[word[letter_count]] < letters_indexes[pivot[letter_count]]:

                    left_list.append(word)
                    break
                elif letters_indexes[word[letter_count]] > letters_indexes[pivot[letter_count]]:

                    right_list.append(word)
                    break
                else:
                    ## if the (n) letter of the word is not before or after the (n) letter of the pivot 
                    ## then go to the next letter
                    letter_count += 1
            else:
                ## if the word and the pivot are similiar then put the word before the pivot
                left_list.append(word)
                
    ## return the left list after sorting it using the same function and the right 
    ## and the pivot in between because we removed it for comparson
    return quickSort(left_list,letters_indexing) + [pivot] + quickSort(right_list,letters_indexing)

if __name__ == "__main__":
    ## a little demo using numbers
    import random

    test = []
    for i in range(30):
        test.append(random.randint(0,100))
    print(test)
    print(quickSort(test))