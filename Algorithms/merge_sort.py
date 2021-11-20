

def merge(myList, left, right):
    #two iterators for the 2 halves
    i = 0
    j = 0

    #iterator for main list
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            myList[k] = left[i]
            i += 1
        else:
            myList[k] = right[j]
            j += 1
        
        k += 1

    #for all remaining elements
    while i < len(left):
        myList[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        myList[k] = right[j]
        j += 1
        k +=  1

    
def merge_sort(myList):
    if len(myList) > 1:
        #break up list into two halves
        middle = len(myList)//2
        left = myList[:middle]
        right = myList[middle:]

        #recursively mergeSort each half
        merge_sort(left)
        merge_sort(right)
        merge(myList, left, right)
    
    else:
        return myList
    




lst = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)


print("List before sorting: ", lst)
merge_sort(lst)
print("List after sorting: ", lst)

