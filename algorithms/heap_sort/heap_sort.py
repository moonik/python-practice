class HeapSort:

    def sort(self, values):
        n = len(values)
        i = n // 2

        while i >= 1:
            self.__sink(values, i, n)
            i -= 1

        while n > 1:
            tmp = values[n-1]
            values[n-1] = values[0]
            values[0] = tmp
            n -= 1
            self.__sink(values, 1, n)

    def __sink(self, values, k, n):
        while 2*k <= n:
            j = 2*k

            if j < n and values[j-1] < values[j]:
                j += 1

            if not values[k-1] < values[j-1]:
                break

            tmp = values[k-1]
            values[k-1] = values[j-1]
            values[j-1] = tmp

            k = j

