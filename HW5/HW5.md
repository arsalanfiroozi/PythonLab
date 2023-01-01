# HW5

## Question 1

### Methods

```python
def find_str(string, i , j , i_previous , j_previous , table):
    char = string[0]
    n_row = len(table)
    n_col = len(table[0][0])
    if i+1 < n_row and i+1 != i_previous:
        if char == table[i+1][0][j]:
            if len(string) == 1:
                return True
            else:
                return find_str(string[1:], i+1 , j , i , j , table)
    if j+1 < n_col and j+1 != j_previous:
        if char == table[i][0][j+1]:
            if len(string) == 1:
                return True
            else:
                return find_str(string[1:], i , j+1 , i , j , table)
    if i-1 >= 0 and i-1 != i_previous:
        if char == table[i-1][0][j]:
            if len(string) == 1:
                return True
            else:
                return find_str(string[1:], i-1 , j , i , j , table)
    if j-1 >= 0 and j-1 != j_previous:
        if char == table[i][0][j-1]:
            if len(string) == 1:
                return True
            else:
                return find_str(string[1:], i , j-1 , i , j , table)
    return False

def str_check(table, string):
    n_row = len(table)
    n_col = len(table[0][0])
    flag = False
    for i in range(n_row):
        for j in range(n_col):
            if string[0] == table[i][0][j]:
                if find_str(string[1:], i , j , i , j , table):
                    flag = True
    return flag
```

### Test

```python
table = [['ABCE'], 
         ['SFCS'], 
         ['ADEE']]

print(str_check(table=table, string='ABCCED'))
print(str_check(table=table, string='SEE'))
print(str_check(table=table, string='ABCB'))
```

    True
    True
    False

## Question 2

### Recursive Programming

```python
def lev_recursive(s1, s2):
    if (len(s1) * len(s2)) == 0:
        return max(len(s1), len(s2))
    elif s1[0] == s2[0]:
        return lev_recursive(s1[1:], s2[1:])
    else:
        return 1 + min(lev_recursive(s1[1:], s2),
                       lev_recursive(s1,     s2[1:]),
                       lev_recursive(s1[1:], s2[1:]))
```

```python
s1 = input("First string = ")
s2 = input("Second string = ")

print(f"Levenshtein distance = {lev_recursive(s1, s2)}")
```

    First string = Hello
    Second string = Hi
    Levenshtein distance = 4

### Dynamic Programming

```python
def lev_dynamic(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    d = [[None for i in range(l2+1)] for i in range(l1+1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if i * j == 0 :
                d[i][j] = max(i, j)
            else:
                if s1[i-1] == s2[j-1]:
                    sub_cost = 0
                else:
                    sub_cost = 1
                d[i][j] = min (1+d[i-1][j], 1+d[i][j-1], sub_cost+d[i-1][j-1])
    return d[l1][l2]
```

```python
s1 = input("First string = ")
s2 = input("Second string = ")

print(f"Levenshtein distance = {lev_dynamic(s1, s2)}")
```

    First string = Hello
    Second string = Hi
    Levenshtein distance = 4

## Question 3

### Method

```python
def collatz(col):
    last = col[-1]
    if last == 1:
        return col
    if last % 2 == 0:
        col.append(last // 2)
        return collatz(col)
    col.append(3 * last + 1)
    return collatz(col)
```

### Test

```python
number = input("Number = ")
print(f"Collatz array = {collatz([int(number)])}")
```

    Number = 100
    Collatz array = [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

### Find Maximum Collatz Length for Integers Less Than 2000

```python
col_max = 0
col_max_len = 0
for i in range(1,2001):
    current_col = collatz([i])
    if len(current_col)>col_max_len:
        col_max = i
        col_max_len = len(current_col)

print(f'The answer = {col_max}')
print(f'Collats length = {col_max_len}')
print(f'Collats array = {collatz([col_max])}')
```

    The answer = 1161
    Collats length = 182
    Collats array = [1161, 3484, 1742, 871, 2614, 1307, 3922, 1961, 5884, 2942, 1471, 4414, 2207, 6622, 3311, 9934, 4967, 14902, 7451, 22354, 11177, 33532, 16766, 8383, 25150, 12575, 37726, 18863, 56590, 28295, 84886, 42443, 127330, 63665, 190996, 95498, 47749, 143248, 71624, 35812, 17906, 8953, 26860, 13430, 6715, 20146, 10073, 30220, 15110, 7555, 22666, 11333, 34000, 17000, 8500, 4250, 2125, 6376, 3188, 1594, 797, 2392, 1196, 598, 299, 898, 449, 1348, 674, 337, 1012, 506, 253, 760, 380, 190, 95, 286, 143, 430, 215, 646, 323, 970, 485, 1456, 728, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]

## Question 4

```python
def fuel_recursive(current_fuel, gas_station, fuel_consumption_rate, capacity, d, p):
    if gas_station < len(p)-1:
        if current_fuel < (d[gas_station+1]-d[gas_station])*fuel_consumption_rate:
            return (capacity-current_fuel)*p[gas_station] + fuel_recursive(capacity-(d[gas_station+1]-d[gas_station])*fuel_consumption_rate, 
                                     gas_station+1, fuel_consumption_rate, capacity, d, p)
        else:
            refill = (capacity-current_fuel)*p[gas_station] + fuel_recursive(capacity-(d[gas_station+1]-d[gas_station])*fuel_consumption_rate, 
                                     gas_station+1, fuel_consumption_rate, capacity, d, p)
            skip = fuel_recursive(current_fuel-(d[gas_station+1]-d[gas_station])*fuel_consumption_rate, 
                                     gas_station+1, fuel_consumption_rate, capacity, d, p)
            return min([refill, skip])
    else:
        if current_fuel < (d[gas_station+1]-d[gas_station])*fuel_consumption_rate:
            return (capacity-current_fuel)*p[gas_station]
        else:
            return 0

def cost_optimizer(c, f, d, p):
    n = len(p)
    if d[0] != 0:
        return 'First gas station must be at 0'
    for i in range(n):
        if (d[i+1]-d[i])*f > c:
            return 'Impossible!'
        if (d[i+1]-d[i]) <= 0:
            return 'Wrong distance data!'
    for price in p:
        if price < 0:
            return 'Fuel prices must be equal or greater than 0'
    return fuel_recursive(0, 0, f, c, d, p)
```

```python
C = 50
F = 0.1
D = [0,300,450,700,900,1100,1200]
P = [0,1100,1500,900,2100,1300]

print(cost_optimizer(C, F, D, P))
```

    69000.0

## Question 5

```python
nearest5 = lambda x : 5*round(x/5)
```

```python
print(nearest5(23))
```

    25

## Question 6

```python
names = lambda people : [person[0] + ' ' + person[1] for person in people]
```

```python
people = [['Mohammad', 'Moghaddam'],
          ['Arsalan', 'Firoozi'],
          ['MohammadReza', 'AliMohammadi']]

print(names(people))
```

    ['Mohammad Moghaddam', 'Arsalan Firoozi', 'MohammadReza AliMohammadi']

## Question 7

```python
%%writefile Q7.py
import numpy as np
def mySqrt(x):
    return np.sqrt(x)
```

    Writing Q7.py

```python
from Q7 import mySqrt as sqrt
print(sqrt(25))
```

    5.0

## Question 8

```python
with open('input_file.txt', 'r') as input_file:
    temp = input_file.readlines()
    temp = [item.split() for item in temp]
    temp = [item[1] + ' ' + item[0] + '\n' for item in temp]
    out = ''
    for item in temp:
        out = out + item
with open('output_file.txt', 'w') as output_file:
    output_file.write(out)
```
