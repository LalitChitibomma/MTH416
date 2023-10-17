def huffman(prob):
    prob_sort = sorted(prob)
    min_1 = 1
    min_2 = 1
    values = []
    binary = []
    result = {}
    for i in range(prob_sort):
        if prob_sort < min_1:
            min_1 = i
    for i in prob_sort:
        if i != min_1:
            min_2 = i

    def huffman_inner(prob, min_1, min_2, values, binary):
        prob_sort = sorted(prob)
        min_sum = round((float(prob_sort[0]) + float(prob_sort[1])), 2)
        if len(prob_sort) == 2:
            min_1 = prob_sort[0]
            min_2 = prob_sort[1]
            values.append(min_1)
            binary.append('0')
            values.append(min_2)
            binary.append('1')
            return values, binary
        else:
            min_1 = prob_sort[0]
            min_2 = prob_sort[1]
            prob_sort = prob_sort[2:] + [min_sum]
            prob_sort = sorted(prob_sort)
            code = huffman_inner(prob_sort, min_1, min_2, values, binary)
            if min_sum in code[0]:
                i = code[0].index(min_sum)
                values.append(min_1)
                binary.append(code[1][i] + '1')
                values.append(min_2)
                binary.append(code[1][i] + '0')
                return code
            
    huffman_inner(prob_sort, min_1, min_2, values, binary)
    for item in prob[::-1]:
        if item in values:
            i = (len(values) - 1) - values[::-1].index(item)
            if item in list(result.values()):
                result[binary[i-1]] = item
            else:
                result[binary[i]] = item
    return list(result.keys())[::-1]

    

prob = [0.3, 0.2, 0.2, 0.15, 0.1, 0.05]
print(sorted(huffman(prob)))

prob = [0.4, 0.3, 0.1, 0.1, 0.06, 0.04]
print(sorted(huffman(prob)))