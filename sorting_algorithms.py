import time
import random
from abc import ABCMeta, abstractclassmethod


class Algorithm(metaclass=ABCMeta):
    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name

    def update_display(self, swap1 = None, swap2 = None):
        import visualizer
        visualizer.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

##Add comments to explain your code,

#Selection_sort

class selectionsort(Algorithm):
    def __init__(self):
        super().__init__("selectionsort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.update_display(self.array[i], self.array[min_index])


#Bubble sort
class bubblesort(Algorithm):
    def __init__(self):
        super().__init__("bubblesort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self[j+1] = self[j+1], self[j]
            self.update_display(self.array[j], self.array[j+1])

#Insertion sort
class insertionsort(Algorithm):
    def __init__(self):
        super().__init__("insertionsort")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            index = i
            while index > 0 and self.array[index-1] > cursor:
                self.array[index] = self.array[index-1]
                index -= 1
            self.array[index] = cursor
            self.update_display(self.array[index], self.array[i])

# Merge sort.
class mergesort(Algorithm):
    def __init__(self):
        super().__init__("mergesort")    

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) //2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()

        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result


#quick sort / partition exchange sort.

class quicksort(Algorithm):
    def __init__(self):
        super().__init__("quicksort")

    def algorithm(self, array = [], start =0, end = 0):
        if array == []:
            array =  self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array, start , end)
            self.algorithm(array, start, pivot -1)
            self.algorithm(array, pivot+1, end)
        
        def partition(self, array, start, end):
            x = array[end]
            i = start - 1

            for j in range(start, end+1, 1):
                if array[j] <= x:
                    i += 1
                    if i < j:
                        array[i], array[j] = array[j], array[i]
                        self.update_display(array[i], array[j])
            return i

