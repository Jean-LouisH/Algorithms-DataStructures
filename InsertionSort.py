def insertionSort(array):
    j = 1
    for j in range(len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key

def main():
    array = [12, 98, 2, 77, 89, 80]
    print("\tInsertion Sort")
    print("Input:", array)
    insertionSort(array)
    print("Output:", array)
    pass

if __name__ == '__main__':
    main()
    input()
