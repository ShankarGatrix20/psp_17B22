def linear_search(myl,token):
    found = False
    for number in myl:
        if number == token:
            found = True
            break
        return found


L = [3,45,56,78,90]
print(linear_search(L,45))


def binary_search(myl, token):
    found = False

    left  = 0
    right = len(myl)-1

    while left <= right and not found:
        mid = (right+left)//2
        if myl[mid] == token:
            found = True

        if myl[mid] > token:
            right = mid - 1
        else:
            left  = mid + 1       
    return found

L = [3,4,5,67]
print(binary_search(L,5))
