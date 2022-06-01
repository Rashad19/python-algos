import math

"""
A low level implementation of binary search.
The class takes in a list of integers sorted in ascending order
and the search key.
"""

class BinarySearch():

    def __init__(self, orderedList, keyItem):
        self.list, self.key = orderedList, keyItem

    def binary_search(self):

        # initialize variables to use in computation

        list, key = self.list, self.key

        # This is the left array index used in divide and conquer-
        # it is initialized to zero (first index)
        l = 0

        # right array index which is initialized to the last index
        r = len(list) - 1

        while l <= r:

            # The middle index is set
            mid = math.floor((l+r)/2.0)

            # base case is when the middle-
            # index stores the key
            if key == list[mid] :
                return mid

            # if not, we perform a reduction-
            # by dividing the search space accordingly below.

            # case 1: key is smaller than the value stored-
            # at middle index, therefore we shift the search space left

            # case 2: key is larger the value stored at middle index
            # hence shift search space right.

            else :
                if key < list[mid] :
                    r = mid - 1
                else :
                    l = mid + 1
        return -1



if __name__ == "__main__":

    """
    Here we test the implemenation of binary search
    using an arbitray list and search key.
    """

    test_list = [1, 3, 8, 9, 12, 14, 15]

    test_key = 2
    
    tester_instance = BinarySearch(test_list, test_key)

    
    if tester_instance.binary_search() != -1:
        print(f'The index of this element is: {tester_instance.binary_search()}')
    else:
        print('This element is not in the array')
    

