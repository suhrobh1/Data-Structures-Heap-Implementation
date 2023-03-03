# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:

from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:

    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """

        if self._heap.is_empty():
            self._heap.append(node)
            return

        self._heap.append(node)
        node_index = self._heap.length() - 1
        parent_index = (node_index - 1) // 2
        # new_node = self._heap[node_index]
        parent = self._heap[parent_index]

        while parent > node:
            temp = parent
            self._heap[parent_index] = node
            self._heap[node_index] = temp
            node_index = parent_index

            if node_index == 0:
                return
            else:
                parent_index = (node_index - 1) // 2
                parent = self._heap[parent_index]

    def is_empty(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self._heap.length():
            return False
        else:
            return True

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """

        if self._heap.length():
            return self._heap[0]
        else:
            raise MinHeapException

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """

        if self._heap.is_empty():
            raise MinHeapException

        return_value = self._heap[0]

        if self._heap.length() == 1:
            self._heap.remove_at_index(0)
            return return_value

        # last is now first

        self._heap[0] = self._heap[self._heap.length() - 1]
        self._heap.remove_at_index(self._heap.length() - 1)

        if self._heap.length() == 2:
            if self._heap[0] > self._heap[1]:
                temp = self._heap[0]
                self._heap[0] = self._heap[1]
                self._heap[1] = temp
                return return_value

        _percolate_down(self._heap, 0)

        return return_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """

        print("Printing DA------------------", da)

        # Create new Dynamic Array
        # Copy over the values that are in the provided dynamic array
        # Heap process on values in the new array
        # Set the new array to be self._heap
        # print("da length: ", da.length())
        heap_length = self._heap.length()
        counter = 0
        # print(heap_length)
        for i in range(0, da.length()):
            # print("i", i)
            if counter < heap_length:
                self._heap[i] = da[i]
                counter += 1
            else:
                self._heap.append(da[i])

        print("The heap", self._heap)

        if self._heap.length() == 2:
            if self._heap[0] > self._heap[1]:
                self._heap[0], self._heap[1] = self._heap[1], self._heap[0]
                return

        node_to_check_index = (self._heap.length() // 2) - 1

        while node_to_check_index >= 0:
            # establishing variables
            node_to_check = self._heap[node_to_check_index]
            child_1_index = 2 * node_to_check_index + 1
            child_2_index = 2 * node_to_check_index + 2
            child_1 = self._heap[child_1_index]
            child_2 = self._heap[child_2_index]

            # determining smaller of the children
            if child_1 == child_2:
                smaller_child = child_2
            else:
                smaller_child = min(child_1, child_2)

            # getting the index of the smaller child
            if smaller_child == child_1:
                smaller_child_index = child_1_index
            else:
                smaller_child_index = child_2_index

            # Swap node with smaller child if node is greater than child
            if node_to_check > smaller_child:
                # temp = self._heap[node_to_check_index]
                self._heap[node_to_check_index] = self._heap[smaller_child_index]
                self._heap[smaller_child_index] = node_to_check
                print("booome---------")

            node_to_check_index = node_to_check_index - 1

            print("node to check index", node_to_check_index)

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        if self._heap.length():
            return self._heap.length()
        else:
            return 0

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """

        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    pass


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #


def _percolate_down(da: DynamicArray, node_to_check_index: int) -> None:
    """
        TODO: Write your implementation
        """
    length = da.length()
    # node_to_check_index = parent
    node_to_check = da[node_to_check_index]
    child_1_index = 2 * node_to_check_index + 1
    child_2_index = 2 * node_to_check_index + 2

    while child_2_index < length:
        child_1 = da[child_1_index]
        child_2 = da[child_2_index]

        # determining smaller of the children
        if child_1 == child_2:
            smaller_child = child_2
        else:
            smaller_child = min(child_1, child_2)

        # getting the index of the smaller child
        if smaller_child == child_1:
            smaller_child_index = child_1_index
        else:
            smaller_child_index = child_2_index

        if node_to_check > smaller_child:
            # temp = da[node_to_check_index]
            # da[node_to_check_index] = smaller_child
            # da[smaller_child_index] = temp

            da[node_to_check_index], da[smaller_child_index] = da[
                smaller_child_index], da[node_to_check_index]

            node_to_check_index = smaller_child_index
            node_to_check = da[node_to_check_index]
            child_1_index = 2 * node_to_check_index + 1
            child_2_index = 2 * node_to_check_index + 2

            # Inside while loop
            # if child_1_index == length - 1:
            #     # print()
            #     if node_to_check > da[child_1_index]:
            #         print("Woof")
            #         da[node_to_check_index] = da[child_1_index]
            #         da[child_1_index] = node_to_check

        # Outside of while loop
        # if child_1_index == length - 1:
        #     # print()
        #     if node_to_check > da[child_1_index]:
        #         print("Woof")
        #         da[node_to_check_index] = da[child_1_index]
        #         da[child_1_index] = node_to_check


# def _percolate_down(da: DynamicArray, parent: int) -> None:
#     """
#     TODO: Write your implementation
#     """
#     pass

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)

    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)

    # print("\nPDF - is_empty example 1")
    # print("-------------------")
    # h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    # print(h.is_empty())

    # print("\nPDF - is_empty example 2")
    # print("-------------------")
    # h = MinHeap()
    # print(h.is_empty())

    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([-7284, 5470, 82852, 82852, 88135])
    # print(h, end=' ')
    # print(h.remove_min())
    # print(h, end=' ')

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap(['NoMYY', 'QHDqUDE', 'kQ', 'Rh_ESJQK', 'fkxT'])
    # print(h, end=' ')
    # print(h.remove_min())
    # print(h, end=' ')

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty() and h.is_empty() is not None:
    #     print(h, end=' ')
    #     print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    # print("--------------------------")
    # print("Inserting 500 into input DA:")
    # da[0] = 500
    # print(da)

    # print("Your MinHeap:")
    # print(h)
    # if h.get_min() == 500:
    #     print(
    #         "Error: input array and heap's underlying DA reference same object in memory"
    #     )

    # print("\nPDF - heapsort example 1")
    # print("------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # print(f"Before: {da}")
    # heapsort(da)
    # print(f"After:  {da}")

    # print("\nPDF - heapsort example 2")
    # print("------------------------")
    # da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    # print(f"Before: {da}")
    # heapsort(da)
    # print(f"After:  {da}")

    # print("\nPDF - size example 1")
    # print("--------------------")
    # h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    # print(h.size())

    # print("\nPDF - size example 2")
    # print("--------------------")
    # h = MinHeap([])
    # print(h.size())

    # print("\nPDF - clear example 1")
    # print("---------------------")
    # h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    # print(h)
    # print(h.clear())
    # print(h)
