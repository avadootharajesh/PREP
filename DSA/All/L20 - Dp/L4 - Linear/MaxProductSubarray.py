# Problem : Find the maximum product of a contiguous subarray in an array of integers.

def max_product_subarray(arr): # can conatin negatives
    if not arr:
        return 0

    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for num in arr[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result

# kadanes
def max_product_subarray_kadanes(arr):
    prod1 = prod2 = arr[0]
    res = arr[0]
    
    for i in range(1, len(arr)):
        temp = max(arr[i], arr[i] * prod1, arr[i] * prod2)
        prod2 = min(arr[i], arr[i] * prod1, arr[i] * prod2)
        prod1 = temp
        res = max(res, prod1)
        
    return res