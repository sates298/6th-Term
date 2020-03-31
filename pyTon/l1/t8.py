def rzym_arab(roman):
    order = ['M', 'CM', 'D', 'CD', 'C', 'XC',
             'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    xx01 = ['M', 'C', 'X', 'I']
    # xx9 = ['CM', 'XC', 'IX']
    # xx5 = ['D', 'L', 'V']
    xx4 = ['CD', 'XL', 'IV']
    xx1 = ['C', 'X', 'I']
    xx1_rep = 0
    actual = 0
    i = 0
    result = 0
    size = len(roman)
    while i < size:
        if actual >= len(order):
            return -1
        if xx1_rep >= 3:
            return -1
        slice_ = roman[i:i+2] if i+1 < size else roman[i]
        if slice_ == order[actual]:
            result += values[actual]
            i += 2
            actual += 2 if slice_ in xx4 else 4
            xx1_rep = 0
        elif slice_[0] == order[actual]:
            result += values[actual]
            if slice_[0] in xx1:
                xx1_rep += 1
                if i-1 >= 0 and roman[i-1] != slice_[0]:
                    xx1_rep = 0
            else:
                xx1_rep = 0
            i += 1
            actual += 0 if slice_[0] in xx01 else 2
        else:
            actual += 1
    return result


tests = [('MMMMMCCCXXXIII', 5333), ('III', 3), ('MMDCD', -1),
         ('MMCDXXIX', 2429), ('DX', 510), ('XD', -1), ('MMXX', 2020),
         ('IXI', -1), ('IIII', -1), ('CDCD', -1), ('CDXLIVI', -1),
         ('CDXLIV', 444)]

tested = list(
    map(lambda x: print('result = ', rzym_arab(x[0]), ' expected = ', x[1]),
        tests))
