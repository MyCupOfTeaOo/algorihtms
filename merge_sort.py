test = [1, 3, 5, 1, 4, 5, 3, 7, 9, 4]


def sort(array1: list, array2: list):
    if (array1 and array2):
        yield array1.pop(0) if array1[0] < array2[0] else array2.pop(0)
        for i in sort(array1, array2):
            yield i
    else:
        for i in (array1 or array2):
            yield i


def merge(array: list):
    if len(array) < 2:
        return array
    m_index = int(len(array) / 2)
    return list(sort(merge(array[:m_index]), merge(array[m_index:])))


print(merge(test))
