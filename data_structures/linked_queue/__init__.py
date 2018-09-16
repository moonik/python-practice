from data_structures.linked_queue.queue import Queue


def main():
    stack = Queue()

    assert stack.is_empty()

    stack.enqueue(1)
    stack.enqueue(2)

    print(stack.dequeue())


if __name__ == "__main__":
    main()
