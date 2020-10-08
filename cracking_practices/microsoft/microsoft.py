def solution(N):

    my_num = str(N)
    symbol = ''

    if my_num[0] =="-" :
        symbol = '-'
        my_num = my_num[1:]


    if int(my_num[0]) < 5:
        result = '5' + str(my_num)
    else:
        result = my_num[:-1] + '5' + my_num[-1]


    if not symbol == '':
        result = symbol + result

    return int(result)


print(solution(-999))
