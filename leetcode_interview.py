# leetcode interview of Kiet Phan 22/07/2024
input_list = [1,2,3,4]

def product_ex_index(input_list):
    output = []
    for i in range(len(input_list)):
        prod = 1
        cal_list = input_list[:]
        cal_list.pop(i)
        for j in cal_list:
            prod *= j
        output.append(prod)
    return print(output)
product_ex_index(input_list)
# [1,2,3,4]




