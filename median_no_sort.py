def find_med(data):
    data = [ i for i in data if i != 0]
    median = find_median_frequency_table(data)
    return

def find_median_frequency_table(data):
    # works only with postive numbers at the moment
    if data == []:
        return None

    print(data)
    # print('max:', max(data))
    table = [0 for i in range(max(data)+1)]
    for number in data:
        table[number] += 1
    table = table[1:]
    # print(table)

    n = len(data)
    print('n:', n)

    # print('number:frequency')
    # for i, value in enumerate(table):
    #     print(i, ':', value)

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
                median1 = index
                if n % 2 == 1:
                    median = median1
                    break;
            if median_position2 <= 0:
                print('med=(',median1,'+',index,')/2')
                median = (median1+index)/2
                break;
    return median


data = [1, 2, 4, 5, 6, 9, 12, 14]
print('test1 median=', find_med(data),'\n')
data = [2,3,6,8,9]
print('test2 median=', find_med(data),'\n')

data = [11, 6, 9, 9, 18, 14, 5]
print('test3 median=', find_med(data),'\n')
data = [11, 6, 9, 9, 18, 14]
print('test4 median=', find_med(data),'\n')

data = [6, 6, 6]
print('test3 median=', find_med(data),'\n')
data = [24,24,24,24,6, 6, 6, 18]
print('test4 median=', find_med(data),'\n')

data = []
print('test5 median=', find_med(data),'\n')

data = [0]
print('test6 median=', find_med(data),'\n')
data = [0,1]
print('test7 median=', find_med(data),'\n')

data = [0,5]
print('test8 median=', find_med(data),'\n')