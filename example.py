import random
import time
import string

import sort_module

def random_list (min, max, num_of_elements):
    list = random.sample(range(min, max), num_of_elements)
    return list

def print_list(L):
    print("List: ", L)

def dictionaryList(x):
    A = []
    for i in range(0, x):
        random_characters = ''.join(random.choices(string.ascii_lowercase, k=5))
        random_int = random.randint(0, 99)
        B = {'ime': random_characters , 'index': random_int}
        A.append(B)
    return A


### main
if __name__ == "__main__":


    # list_10 = dictionaryList(10)
    # print(list_10)
    # start_time = time.perf_counter();
    # print(sort_module.bucket_sort(list_10))
    # end_time = time.perf_counter();
    # print("vreme izvrsavanja bucket sort-a za 10 el: ", end_time - start_time)
    #
    # list_100 = dictionaryList(100)
    # start_time = time.perf_counter();
    # sort_module.bucket_sort(list_100)
    # end_time = time.perf_counter();
    # print("vreme izvrsavanja bucket sort-a za 100 el: ", end_time - start_time)
    #
    # list_1000= dictionaryList(1000)
    # start_time = time.perf_counter();
    # sort_module.bucket_sort(list_1000)
    # end_time = time.perf_counter();
    # print("vreme izvrsavanja bucket sort-a za 1 000 el: ", end_time - start_time)
    # print("\n")
    #
    #
    # list_10000 = dictionaryList(10000)
    # start_time = time.perf_counter();
    # sort_module.bucket_sort(list_10000)
    # end_time = time.perf_counter();
    # print("vreme izvrsavanja bucket sort-a za 10 000 el: ", end_time - start_time)
    #
    # randomlist1 = random_list(0, 100000, 10000)
    # start_time = time.perf_counter();
    # sort_module.insertion_sort(randomlist1)
    # end_time = time.perf_counter();
    # print("vreme izvrsavanja insertion sort-a za 10 000 el: ", end_time - start_time)
    #
    # randomlist2 = random_list(0, 100000, 10000)
    # start_time = time.perf_counter();
    # sort_module.merge_sort(randomlist2, 0, len(randomlist2) - 1)
    # end_time = time.perf_counter();
    # print("vreme izvrsavanja merge sort-a za 10 000 el: ", end_time - start_time)
    # print("\n")
    #
    # list_100000 = dictionaryList(100000)
    # start_time = time.perf_counter();
    # sort_module.bucket_sort(list_100000)
    # end_time = time.perf_counter();
    # print("vreme izvrsavanja bucket sort-a za 100 000 el: ", end_time - start_time)


    # start_time = time.perf_counter()
    # do some processing...
    # end_time = time.perf_counter()

    # print('Execution time is', end_time - start_time)

    # start_time = time.perf_counter();
    # sort_module.insertion_sort(list_10)
    # print("vreme izvrsavanja insertion sort-a za 10 el: ", time.perf_counter() - start_time)
    #
    # start_time = time.perf_counter();
    # sort_module.insertion_sort(list_100)
    # print("vreme izvrsavanja insertion sort-a za 100 el: ", time.perf_counter() - start_time)
    #
    # start_time = time.perf_counter();
    # sort_module.insertion_sort(list_1000)
    # print("vreme izvrsavanja insertion sort-a za 1000 el: ", time.perf_counter() - start_time)
    #
    # start_time = time.perf_counter();
    # sort_module.insertion_sort(list_10000)
    # print("vreme izvrsavanja insertion sort-a za 10000 el: ", time.perf_counter() - start_time)
    #
    # start_time = time.perf_counter();
    # sort_module.insertion_sort(list_100000)
    # print("vreme izvrsavanja insertion sort-a za 100000 el: ", time.perf_counter() - start_time)

    # start_time = time.perf_counter();
    # sort_module.bubble_sort(list_10000)
    # print("vreme izvrsavanja bubble sort-a za 100000 el: ", time.perf_counter() - start_time)

    # print(list_10)
    # print(sort_module.linear_search(list_10, 5))

    # print(list_10)
    # print(sort_module.binary_search(list_10, 5))

    # print(list_10)
    # sort_module.merge_sort(list_10, 0, len(list_10)-1)
    # print(list_10)

    # print(list_10)
    # sort_module.quick_sort(list_10, 0, len(list_10)-1)
    # print(list_10)

    # lista = [12, 13, 64, 8, 39, 24, 38, 56, 2]
    # print("pre   ", lista)
    # sort_module.heap_sort(lista)
    # print("posle ", lista)

