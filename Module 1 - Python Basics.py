import random
import statistics

def f_print_avg(lst, txt):
    if len(lst) == 0:
        print(f"avg of {txt} can\'t be found")
    else:
        print(f"avg of {txt} = {str(statistics.mean(lst))}")

numbers = range(0, 1000)
random_numbers = random.sample(numbers, 100)
even = []
odd = []
# for each element in array do - print
for i in random_numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# for each i element in range from 0 to the length of b list
for i in range(0, len(random_numbers)):
    # set index of min value in the list
    min_index = i
    # for each j element in the range from i+1 to the length of b list
    for j in range(i + 1, len(random_numbers)):
        # if if element with index j from the list b less than element with min_index from the list b
        if random_numbers[j] < random_numbers[min_index]:
            # set min_index equal j
            min_index = j
    # if we changed min_index to j value and it's not equal i value
    if min_index != i:
        # then we change value of element with index i and element with min_index in the b list
        random_numbers[i], random_numbers[min_index] = random_numbers[min_index], random_numbers[i]

print(random_numbers)
f_print_avg(even, 'even numbers')
f_print_avg(odd, 'odd numbers')
