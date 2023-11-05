import math

def huffman(prob):
    values = []
    binary = []
    result = {}
    min_1 = sorted(prob)[0]
    min_2 = sorted(prob)[1]

    def huffman_inner(min_1, min_2, values, binary):
        if len(prob) == 2:
            min_1 = prob[0]
            min_2 = prob[1]
            result['0'] = min_1
            result['1'] = min_2
            return result
        else:
            min_sum = round(min_1 + min_2, 2)
            prob.remove(min_1)
            prob.remove(min_2)
            prob.append(min_sum)
            min_1 = sorted(prob)[0]
            min_2 = sorted(prob)[1]
            code = huffman_inner(min_1, min_2, values, binary)
            min_sum = min_1 + min_2
            nums = set(code.values())
            if min_sum in nums:
                result[min_1] = result[min_sum] + '1'
                result[min_2] = result[min_sum] + '0'
            return code
            
    huffman_inner(min_1, min_2, values, binary)
    for item in prob[::-1]:
        if item in values:
            i = (len(values) - 1) - values[::-1].index(item)
            if item in list(result.values()):
                result[binary[i-1]] = item
            else:
                result[binary[i]] = item
    return list(result.keys())[::-1]

def arithmatic(alphabet, prob):
    code = {}
    alpha = 0

    for i in range(len(prob)):
        z = ''
        p = prob[i]
        if i > 0:
            alpha += prob[i-1]
            alpha = round(alpha, 2)
        n = (math.ceil(math.log(1/p, 2))) + 1
        c = bin(math.ceil(pow(2, n) * alpha))
        for j in range(n - len(c[2:])):
            z += '0'
        code[alphabet[i]] = z + c[2:]

    return code

def LZW(alphabet, word, encoding=True):
    code = ''
    if encoding:
        dictionary = {alphabet[i]:(i+1) for i in range(len(alphabet))}
    else:
        dictionary = {(i+1):alphabet[i] for i in range(len(alphabet))}

    n = len(alphabet)
    i = 0
    l = 2
    x = False
    d = word

    while encoding and d:
        d = word[i:]

        if x:
            l += 1

        for j in range(l):
            if d[:l-j] in dictionary:
                code += f'{dictionary[d[:l-j]]}.'
                if len(d[:l-j]) == l:
                    x = True
                else:
                    x = False
                break

        n += 1
        if x:
            dictionary[d[:l+1]] = n
            i += l
        else:
            dictionary[d[:l]] = n
            i += l-1

    if not encoding:
        nums = word.split('.')
        z = dictionary[int(nums[0])] + dictionary[int(nums[1])]
        n += 1
        dictionary[n] = z
        code += z[0]
        for j in range(1, len(nums)):
            i = nums[j]
            if int(i) in dictionary:
                code += dictionary[int(i)]
            n += 1

            if j == len(nums)-1:
                break

            if int(nums[j+1]) in dictionary:
                z = dictionary[int(nums[j+1])][0]
            else:
                z = dictionary[int(i)][0]

            dictionary[n] = dictionary[int(i)] + z
            

    return code
        
            

# prob = [0.3, 0.2, 0.2, 0.15, 0.1, 0.05]
# print(huffman(prob))

# prob = [0.4, 0.3, 0.1, 0.1, 0.06, 0.04]
# print(huffman(prob))

alphabet = ['a', 'd', 'e', 'b', 'c']
prob = [0.1, 0.3, 0.2, 0.15, 0.25]
print(arithmatic(alphabet, prob))

alphabet = ['αα', 'αβ', 'αγ', 'αω', 
            'βα', 'ββ', 'βγ', 'βω', 
            'γα', 'γβ', 'γγ', 'γω', 
            'ωα', 'ωβ', 'ωγ', 'ωω']
prob = [0.31, 0.13, 0.04, 0.02, 
        0.13, 0.15, 0.01, 0.01, 
        0.04, 0.01, 0.03, 0.02, 
        0.02, 0.01, 0.02, 0.05]
print(arithmatic(alphabet, prob))

prob = [0.5*0.5, 0.5*0.3, 0.5*0.1, 0.5*0.1, 
        0.3*0.5, 0.3*0.3, 0.3*0.1, 0.3*0.1, 
        0.1*0.5, 0.1*0.3, 0.1*0.1, 0.1*0.1, 
        0.1*0.5, 0.1*0.3, 0.1*0.1, 0.1*0.1]
code = arithmatic(alphabet, prob)
L = 0
for i in range(len(alphabet)):
    L += len(code[alphabet[i]]) * prob[i]

print(f'L: {L}\n')

alphabet = ['bb', 'ba', 'ab', 'aa']
prob = [0.4, 0.3, 0.2, 0.1]
code = arithmatic(alphabet, prob)['ba']
print(f'HW: {code}')

alphabet = ['aa', 'ab', 'ac', 'ad', 
            'ba', 'bb', 'bc', 'bd', 
            'ca', 'cb', 'cc', 'cd', 
            'da', 'db', 'dc', 'dd']
prob = [0.16, 0.12, 0.08, 0.04,
        0.12, 0.09, 0.06, 0.03, 
        0.08, 0.06, 0.04, 0.02, 
        0.04, 0.03, 0.02, 0.01]
code = arithmatic(alphabet, prob)
L = 0

for i in range(len(alphabet)):
    L += len(code[alphabet[i]]) * prob[i]

print(f'HW: {code}\n{L}\n')

alphabet = ['a', 'b', 'c', 'd', 'e']
word = 'bdddaadda'
print(LZW(alphabet, word))

alphabet = ['B', 'A', 'D', 'E', 'F']
word = '3.4.6.7.9.10.8'
print(LZW(alphabet, word, False))

alphabet = ['A', 'B', 'C', 'D', 'R']
word = '1.2.5.1.3.1.4.6.8'
print(LZW(alphabet, word, False))

alphabet = ['B', 'D', 'E', 'N', 'O', 'R', 'T', ' ']
word = '1.3.7.8.5.4.8.7.3.14.5.6.8.9.11.13.12.4.3.12.20.2.25.5.11.22'
print(LZW(alphabet, word, False))

alphabet = ['B', 'D', 'E', 'N', 'O', 'R', 'T', ' ']
word = 'BET ON TEN OR BET ON ONE OR DO NOT BET'
print(LZW(alphabet, word))

alphabet = ['B', 'D', 'E', 'N', 'O', 'R', 'T', ' ']
word = '1.3.7.8.5.4.8.7.3.14.5.8.10.12.18.4.19.2.4.20.7'
print(LZW(alphabet, word, False)+'\n')

alphabet = ['I', 'M', 'P', 'S']
word = 'MISSISSIPPI'
print(f'HW: {LZW(alphabet, word)}')
word = '2.1.4.4.6.8.3.3.1'
print(f'HW: {LZW(alphabet, word, False)}')

alphabet = [' ', 'B', 'D', 'E', 'N', 'O', 'P', 'R', 'S', 'T']
word = '10.6.1.2.4.1.6.8.1.5.6.10.1.11.13.4'
print(f'HW: {LZW(alphabet, word, False)}')

alphabet = [' ', 'B', 'D', 'E', 'N', 'O', 'P', 'R', 'S', 'T']
word = 'TO BE OR NOT TO BE'
print(f'HW: {LZW(alphabet, word)}')
print(f'HW: {LZW(alphabet, LZW(alphabet, word)[:-1], False)}')

def generatebits(total_size, number_of_bits):
    nums = []
    for i in range(pow(2, total_size)):
        n = bin(i)
        if n.count('1') == number_of_bits:
            nums.append(n[2:])
    return nums

print(generatebits(5, 3))

def extend_error_correcting_code(codewords, r_value):
    nums = []
    correct = 0
    for i in range(pow(2, len(codewords[0]))):
        for codeword in codewords:
            w = int('0b' + codeword, base=0)
            if bin(w ^ i).count('1') >= 2*r_value + 1:
                correct += 1
            else:
                break
        if correct == len(codewords):
            n = bin(i)
            nums.append(n[2:])
    return nums

extend_error_correcting_code(['00000', '11100', '10011'], 1)