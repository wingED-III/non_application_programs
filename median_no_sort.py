def find_med(data):
    print('input:', data)

    # get rid of 0
    data = [i for i in data if i != 0]
    if data == []:
        return None

    copy_data = data.copy()
    copy_data.sort()
    print('Python_builted_in_sort:', copy_data)

    # print('dfiltered_zero:',data)
    median = find_median_frequency_table(data)

    return median


def find_median_frequency_table(data):

    minimum = 0
    # offset to positive
    if min(data) < 0:
        minimum = -1*min(data)
        print("Offset:", minimum)
        data = [minimum+i for i in data]

    print(data)

    # create array store frequency of numbers
    # print('max:', max(data))
    table = [0 for i in range(max(data)+1)]
    for number in data:
        table[number] += 1
    # print(table)

    n = len(data)
    print('n:', n)

    # print('number:frequency')
    # for i, value in enumerate(table):
    #     print(i, ':', value)

    # find median
    if n % 2 == 1:
        median_position1 = len(data)//2+1
        median_position2 = 0
        # print('Case:1 median postition:', median_position1)
    else:
        median_position1 = len(data)//2
        median_position2 = median_position1+1
        # print('Case:2 median postition:', median_position1,median_position2)

    # print('index,frequency,median_pos1,median_pos2')
    median1 = None
    for index, frequency in enumerate(table):
        median_position1 -= frequency
        median_position2 -= frequency
        # print(index, frequency, median_position1,median_position2)

        if median_position1 <= 0:
            if median1 is None:
                median1 = index - minimum
                if n % 2 == 1:
                    median = median1
                    break
            if median_position2 <= 0:
                print('med=(', median1, '+', index - minimum, ')/2')
                median = (median1+index - minimum)/2
                break
    return median


print('-------------Positive-------------')
data = [1, 2, 4, 5, 6, 9, 12, 14]
print('test1 median=', find_med(data), 'expect: 5.5', '\n')
data = [2, 3, 6, 8, 9]
print('test2 median=', find_med(data), 'expect: 6', '\n')

data = [11, 6, 9, 9, 18, 14, 5]
print('test3 median=', find_med(data), 'expect: 9', '\n')
data = [11, 6, 9, 9, 18, 14]
print('test4 median=', find_med(data), 'expect: 10', '\n')

data = [6, 6, 6]
print('test3 median=', find_med(data), 'expect: 6', '\n')
data = [24, 24, 24, 24, 6, 6, 6, 18]
print('test4 median=', find_med(data), 'expect: 21', '\n')


print('-------------with Zero-------------')
data = []
print('test5 median=', find_med(data), 'expect: None', '\n')
data = [0]
print('test6 median=', find_med(data), 'expect: None', '\n')

data = [0, 1]
print('test7 median=', find_med(data), 'expect: 1', '\n')
data = [0, 5]
print('test8 median=', find_med(data), 'expect: 5', '\n')

print('-------------Negative-------------')
data = [-14, -1, -2, -4, -6, -5,  -9, -12]
print('test9 median=', find_med(data), 'expect: -5.5', '\n')
data = [-2, -8, -3, -9, -6]
print('test10 median=', find_med(data), 'expect: -6', '\n')

data = [-6, -6, -6]
print('test10 median=', find_med(data), 'expect: -6', '\n')
data = [-6, -6, -6, -6]
print('test10 median=', find_med(data), 'expect: -6', '\n')

data = [0, -1]
print('test7 median=', find_med(data), 'expect: -1', '\n')
data = [0, -5]
print('test8 median=', find_med(data), 'expect: -5', '\n')

print('-------------Mix-------------')

data = [14, -1, -2, 4, -6, -5,  9, 12]
print('test9 median=', find_med(data), 'expect: -5.5', '\n')

data = [2, 8, -3, -9, -6]
print('test10 median=', find_med(data), 'expect: -3', '\n')


data = [2, -20, -3, 18, -1, 0]
print('test11 median=', find_med(data), 'expect: -1', '\n')

data = [2, -20, -3, 18, -1, 0, 4]
print('test12 median=', find_med(data), 'expect: -0.5', '\n')
