"""
    In this program, we will select the longest subarray
    of 01 of 10
"""
def longest_subarray(array):
    """
        This will return the counter of all 01 and 01 sequence
    """
    maximum_counter_sub = 0
    counter_subarray = 0
    for compare in range(len(array) - 1):
        if array[compare] != array[compare + 1]:
            counter_subarray += 1
            if counter_subarray > maximum_counter_sub:
                maximum_counter_sub = counter_subarray
        else:
            counter_subarray = 0
    return maximum_counter_sub + 1
SUBARRAY = longest_subarray([0,1,1,1,1,0,0,0,1,0,1])
print(SUBARRAY)
