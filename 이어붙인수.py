def solution(num_list):
    num_1 = []
    num_2 = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            num_1.append(num_list[i])
        else:
            num_2.append(num_list[i])
    num_1_str = ""
    num_2_str = ""
    for i in range(len(num_1)):
        num_1_str += str(num_1[i])
        
    for i in range(len(num_2)):
        num_2_str += str(num_2[i])
    return int(num_1_str) + int(num_2_str)    
