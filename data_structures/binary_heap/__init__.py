from data_structures.binary_heap.binary_heap import BinaryHeap


def main():
    original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824,
                4, -2650, 9, 662, 3928, -170, 45358, 395,
                842, 7697, 110, 14, 99, 221]

    sorted_ = [-2650, -170, -93, 3, 4, 9, 14, 42, 45, 99, 110,
               123, 184, 184, 221, 395, 597, 662, 824, 842,
               989, 2409, 3928, 5042, 7506, 7697,
               45358, 189019, 325432, 547510]

    heap = BinaryHeap()

    n = len(original)
    i = 0

    while i < n:
        heap.insert(original[i])
        i += 1

    i = 0
    sorted_.reverse()
    while i < n:
        assert heap.del_max() == sorted_[i]
        i += 1


if __name__ == "__main__":
    main()
