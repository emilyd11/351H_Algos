''' modify merge sort to calculate the number of inversions in an array
    where an inversion is a pair of elements where the larger element has a smaller index than the smaller element'''

#GPT code 
def merge_sort(arr):
    if len(arr) > 1:

        # split array in half 
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls for each half
        inv_count_left = merge_sort(left_half)
        inv_count_right = merge_sort(right_half)
        inv_count = inv_count_left + inv_count_right

        # Merging the two halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            print("comparing " + str(left_half[i]) + " from " + str(left_half) + " to " + str(right_half[j]) + " from " + str(right_half))
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                # Increment inversion count by number of elements remaining in left_half
                inv_count += len(left_half) - i
                print("inversion!")
                j += 1
            k += 1
            print("arr is now " + str(arr))

        # Copy remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return inv_count
    else:
        return 0

# Example usage
arr = [1, 2, 5, 3, 4]

