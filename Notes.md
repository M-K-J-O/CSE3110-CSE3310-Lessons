CSE3110, CSE3310 - Notes

# Iterative Algorithms

Iterative algorithms are algorithms that use loops to process large sets of data. This includes while loops and for
loops, in contrast recursive algorithms are algorithms that call the same algorithm over and over again to process large
sets of data.

Iterative algorithms tend to be easier to design, but may increase in efficiency when using recursive algorithms

Iterative and recursive algorithms are commonly shown through various search and sort algorithms

## Linear search

Linear search is the easiest to program, but least efficient method of search. It processes the data line by line,
similar to brute force decryption algorithms when cracking passwords.

```python
FOUND = False
for i in range(len(LIST)):
    if VALUE == LIST[i]:
        FOUND = True
        break
```

Linear search processing time is dependent on the length of the array and the value's placement within the array. Arrays
that are 10000 indices or higher can have a noticeable time requirement to process.

### Advantages and Disadvantages

### Advantages

* Easy to implement/low creativity
* Versatile
* Data does not need to be sorted
* Guaranteed to work

### Disadvantages

* Time inefficient

### Measuring Time

To measure the processing time within python the ```time.perf_counter()``` will measure the approximate seconds it takes
to run the program.

For more accurate results. we use the average of at least 30 trials and then use ```statistics.mean()```
or ```statistics.fmean``` to find the average.

## Binary Search

Binary Search follows the _divide and conquer_ technique of finding a value. It takes an __ordered__ set of data and
tests the midpoint value. Then it cuts the list in half and reruns the process until the value is found

### Steps for Binary Search

1. Determine midpoint of the list
2. Test if the midpoint value is being searched.
    1. if the midpoint is the searched value, end.
    2. if the value is larger than the midpoint, redefine the lowest- index of the list to be one above the midpoint and
       rerun the search.
3. Repeat 1 and 2 until the value is found

### Advantages and Disadvantages

#### Advantage

* One of the fastest searches

#### Disadvantages

* List must be fully sorted

## Sorting Data

Just like searching algorithms, sorting algorithms have varying levels of efficiency. There are several types of sort
algorithms including, bubble selection, insertion, and merge. (Python uses Timsort, which is a hybrid of merge and
insertion sort design by Tim Peters in 2002).

### Bubble Sort

Bubble sort compares 2 adjacent values on the list and arranges them from lowest to highest.Then it moves to the next
index pair and repeats the 2 value sort until it reaches the end of the unsorted list. The final index is the value that
is sorted anf the algorithm repeats until each index (traversed tailed-to-head) is sorted.

### Advantages and Disadvantages

#### Advantage

* This algorithm requires the smallest amount of memory to operate

#### Disadvantage

* The slowest sorting algorithm

| 5 | 1 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 5 | 11 | 17 | 7 | 13 | __19__ |
| 1 | 3 | 5 | 11 | 7 | 13 | __17__ | 19 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 | 19 |
| 1 | 3 | 5 | 7 | __11__ | 13 | 17 | 19 | 
| 1 | 3 | 5 | __7__ | 11 | 13 | 17 | 19 | 
| 1 | 3 | __5__ | 7 | 11 | 13 | 17 | 19 | 
| __1__ | __3__ | 5 | 7 | 11 | 13 | 17 | 19 |

### Selection Sort

Selection sort compares the current index value with the rest of the unsorted part of the list it will find the lowest
value in the list and switch with its position with the lowest index position of the unsorted half od the list. As it
runs through the data se, it will select the lowest values and place them in the lower positions on the list.

### Advantages and Disadvantages

__Advantages__

* Data is moved less
* Sorts faster than bubble sort
  __Disadvantages__
* The algorithm must scan through the entire unsorted list.
    * same number of processes as bubble sort
    * dependent on the length of the list

| 5 | 1 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __1__ | _5_ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | __*5*__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1 | 3 | 5 | 7 | __*11*__ | 17 | 19 | 13 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 19 | _17_ |
| 1 | 3 | 5 | 7 | 11 | 13 | __17__ | _19_ |

### Insertion Sort

Insertion sort splits the listi nto the sections: sorted and unsorted. As it progresses through the list, tit takes a
value from the unsorted section and places it into its relative position in the sorted section. It is the relative sort
position because it is not necessary in the correct index value, but the value is beside the correct values in the
sorted section.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | __*5*__ | 19 | 3 | 11 | 17 | 7 | 13 |
| 1 | _3_ | __5__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 5 | __*19*__ | 3 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | _11_ | __19__ | 17 | 7 | 13 |
| 1 | 3 | 5 | 11 | _17_ | __19__ | 7 | 13 |
| 1 | 3 | 5 | _7_ | 11 | 17 | __19__ | 13 |
| 1 | 3 | 5 | 7 | 11 | _13_ | 17 | __19__ |

NOTE: Insertion sort starts at index 1, not 0.

NOTE: Insertion sort and selection sort are relatively the same speed for fully random data sets. Hoever, for partially
sorted data sets (i.e a list of names is grouped for the first letter) insertion sort with be faster

# CSE3310 Recursive Algorithms 1

A __recursive algorithm__ calls itself with smaller or simpler input values. Recursive algorithms have a base case,
which received the simplest input value. Then there are subprocesses that simplifies the input values and returns teh
simplified values until it reaches the base case.

All iterative algorithms can be written recursively and vice verse; however, certain algorithms are easer to write in
one form over the other.

## Example: Testing for the correct input data

```python
# def recurisveFunction(INPUT:int):
"""
param INPUT: int
return: int
"""
# test if the base case is met
# return some value
# process to simplify the input
# return recursiveFunction(INPUT) # return the function with new input.
```

All iterative algorithms can be written recursively and all recursive algorithms can be written iteratively. However,
certain algorithms are easier to write one way over the other,

### Example 1: Testing for the correct input data

```python
def checkInt(VALUE):  # recursive
    if VALUE.isnumeric():  # base case
        return int(VALUE)
    else:
        print("You did not enter a number!")
        # modifies the Value and re-run the function
        VALUE = input('Enter a number: ')
        return checkInt(VALUE)  # call the function again


def checkInt2(VALUE):  # iterative
    while True:
        if VALUE.isnumeric():
            return int(VALUE)
        else:
            print("You did not enter a number!")
            VALUE = input('Enter a number ')
```

Recursion often replaces a while loop and reduces the number of variables required. The benefits of recursion are that
it can split data and process sections separately rather than iterative from head to tail.

# Iteratiation vs Recrusion

In general, iterative algorithms require more lines of code and more variables. It relies on while and for loops to
complete the process where data is intermittenly stored on variables. Whereas recursive algorithms do not use as many
variables and relu on return values that are re entered into the function, which replaces a loop. Recursion can use more
physical memory than iterative algorithms because each instance of the recursive function must stay in memory until the
base case is reaches, finally, iterative functions tend to be faster than exclusively recursive functions; however,
hybrid functions that contain both iterative and recursive aspects are even faster.

### Example 2: Factorials

#### Calculate 7!

```
7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1
BUT!
6! = 6 * 5 * 4 * 3 * 2 * 1 * 1
THEREFORE
7! = 7 * 6!
WHICH EXTENDS TO 
7! = 7 * (6 * (5 * ( 4 * (3 * (2 * (1 * (1)))))))
GENERALIZING
f(x) = x * f(x-1), x > 0 -> process that gives x to hte base case
f(x) 1, x = 9 -> base case
```

## Iteration vs Recursion

In general, iterative algorithms require more lines of code and more variables. It relies on while and for loops to
complete the process. Whereas, recursive algorithms do not use as many variables and rely on return values that are
re-entered into the functions to loop. Recursion can use more physical memory than iterative algorithms because each
instance of the recursive function must stay in memory until the base case is reaches. Finally, iterative functions tend
to be faster than exclusively recursive functions.

Hybrid iterative and recursive algorithms are often faster than exclusively iterative or exclusively recursive
algorithms.

### Linear and Binary Search (Recursive)

Linear and Binary Search algorithms in recursive form do not function or are slower than their iterative counterparts.

To view these algorithms switch to the recursive branch.

### Sorting

Recursive Sorting uses both recursive and iterative processes. In general these hybrid sorts are exponentially faster
with long lists. (They measure on a logarithmic scale).

### Merge Sort

Merge sort follows a divide and conquer method of sorting, where the array is split into its base length(len = 1) and
then rebuilt by combining progressively sorted lists together. The recursive portion is the splitting of the list and
the iterative portion is the recombination or merging of the two sorted lists.

Oftentimes, this function is separated into splitting and merging functions.

### Quick Sort 
Quick Sort is another divide and conquer method of sorting. Quick Sort uses an arbitrary value as its pivot. That value will be placed in its correct position within the array. It does this by comparing and placing smaller values on the left side of the array and larger values on the right side. Then it switches the pivot with the right-side pointer to properly place the pivot value. Within the two inserted values of the array, the algorithm recurs until all values are correctly placed.

For the purpose of the unit, Quick Sort is the fastest sort.

### Heap Sort 
Heap Sort uses a binary tree organization of an array to sort higher values to the top of the Binary tree. The process of moving larger values higher in the binary tree is called **heapifying** (or to heapify). A_max heap_ os when the entire binary tree has the larger value be the parent value of one or two child values.

to heapify the binary tree, the value of the parent index must be higher than the two children. Therefore, the process starts at the bottom of the tree and works its way to the top. Of the parent value is smaller than one of the child values, the two swap positions. As the process continues, higher values progressively move to the top of the binary tree (closer to the head of the array).

When the max heap is formed for the entire list, the highest value is at index 0. It swaps position with the highest index and that index is removed from the binary tree. Then the heapify algorithm runs through the binary tree again to reform the max heap. The index value can be calculated from the following.

```
[5, 17, 13, 11, 1, 7, 3]

//sample tree

            5[0]
          /      \
        17[1]   13[2]
      /     \   /     \
    11[3] 1[4] 7[5]  3[6]
    
// Calculate the index of a chuld index
left_child_index = 2 * parent_index + 1
right_child_index = 2 * parent_index + 2

```



















