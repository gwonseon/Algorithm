def merge(B, low, mid1, mid2, high, C):
    i = low
    j = mid1
    k = mid2
    l = low

    while ((i < mid1) and (j < mid2) and (k < high)):
        if (B[i] < B[j]):
            if (B[i] < B[k]):
                C[l] = B[i]
                l += 1
                i += 1
            else:
                C[l] = B[k]
                l += 1
                k += 1
        else:
            if (B[j] < B[k]):
                C[l] = B[j]
                l += 1
                j += 1
            else:
                C[l] = B[k]
                l += 1
                k += 1

    while ((i < mid1) and (j < mid2)):
        if (B[i] < B[j]):
            C[l] = B[i]
            l += 1
            i += 1
        else:
            C[l] = B[j]
            l += 1
            j += 1

    while ((j < mid2) and (k < high)):
        if (B[j] < B[k]):
            C[l] = B[j]
            l += 1
            j += 1
        else:
            C[l] = B[k]
            l += 1
            k += 1

    while ((i < mid1) and (k < high)):
        if (B[i] < B[k]):
            C[l] = B[i]
            l += 1
            i += 1
        else:
            C[l] = B[k]
            l += 1
            k += 1

    while (i < mid1):
        C[l] = B[i]
        l += 1
        i += 1

    while (j < mid2):
        C[l] = B[j]
        l += 1
        j += 1

    while (k < high):
        C[l] = B[k]
        l += 1
        k += 1


def merge_sort(A, low, high, C):
    if (high - low < 2):
        return

    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1

    merge_sort(C, low, mid1, A)
    merge_sort(C, mid1, mid2, A)
    merge_sort(C, mid2, high, A)
    merge(C, low, mid1, mid2, high, A)


def rev(A):
    n = len(A)
    D = []
    for i in range(n):
        D.append(A[i])
    return D


def m_sort(A, first, last):
    if ((last - 2) == 0):
        return
    else:

        D = []
        B = []
        B = A.copy()
        merge_sort(B, 0, last + 1, A)
        D = B.copy()
        A.clear()
        for i in range(len(B)):
            A.append(D[i])
        return A

# T(n) = 3T(3/n) + cn = O(n log n)
