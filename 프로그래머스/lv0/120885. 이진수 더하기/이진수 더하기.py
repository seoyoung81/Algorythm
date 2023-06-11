def solution(bin1, bin2):
    answer = ''
    bin_1 = '0b' + bin1
    bin_2 = '0b' + bin2
    a = int(bin_1, 2)
    b = int(bin_2, 2)
    answer = str(bin(a + b))[2:]
    return answer