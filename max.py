def find_max(a_list):
    if a_list == []:
        max_num = 0
    else:
        max_num = a_list[0]
        for num in a_list:
            if num > max_num:
                max_num = num    
    return max_num        


def main():
    a_list = input("Please insert numbers and seperate by space : ")
    numbers = a_list.split()
    numbers[:] = [int(x) for x in numbers] # 轉換整個list內的資料型態string to int
    max_num = find_max(numbers)
    print("The maximun number is: ", max_num)


main() 