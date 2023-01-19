"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = "2022-01-05"
-------------------------------------------------------
"""


VOWELS = ('aeiouAEIOU')


# =============================================== 1

def clean_list(values):
    
    for i in range(len(values)-1, -1,-1):
        if values.count(values[i]) > 1:
            values.pop(i)
    
    return None

#    uniques = []
   
#    for numbers in values:
#        if numbers not in uniques:
#            uniques.append(numbers)
#    print(f'Cleaned: {uniques}')


#for i in values:
#     if count > 1:
#       values.pop()

    #numbers = int
    
# =============================================== 2
    

def dsmvwl(s):
    
    
    out = s
  

    for letter in VOWELS:
        out = out.replace(letter, '')
    return out


    # Sentence = str(input('Enter a line of text! We will remove all the
    # vowels: )
    #.join
    #.lower
    #.translate
    
# =============================================== 3
def file_analyze(fv):


    #@@ how to use files in function
    # kevin has
    # 3 u case
    # number of l case = 55
    # number of d = 4
    # w spaces = 14
    # 2

    u = 0
    l = 0
    w = 0
    d = 0
    r = 0

    data = fv.read()

    for letter in data:
        if letter.isupper():
            u += 1

        elif letter.islower():
            l += 1

        elif letter.isspace():
            w += 1

        elif letter.isdigit():
            d += 1

    r = len(data) - (u + l + w + d)

    return(u, l, d, w, r)

# =============================================== 4
def is_leap_year(year):

    leap_year = False
    if(year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False

    return leap_year
# =============================================== 5
def is_palindrome(s):

    punctuations = '''!()-[]{};:'",<>./?@#$%^&*~'''

    palindrome = False

    r = s.replace(' ', '')
    t = r.lower()
    z = ''

    for char in t:
        if char not in punctuations:
            z = z + char

    if z == z[::-1]:
        palindrome = True

    return palindrome

# Able was I ere I saw Elba

# =============================================== 6
def max_diff(a):
    
    md = 0
    
    for i in range(len(a)-1):
        dif = abs(a[i]-a[i+1])
        if dif > md:
            md = dif
    return md
    
# =============================================== 7
def matrix_transpose(a):
    
    b = [[0] * len(a)] * len(a[0])
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a[i][j] 
            
    return b
    

# =============================================== 8
def matrix_stats(a):
    
    total = 0
    matrix = a
    AREA = len(matrix) * (len(matrix[0]))
    list = []

    # calculate the total of the array

    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            list.append(matrix[i][y])

    highest = max(list)
    lowest = min(list)

    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            total = total + matrix[i][y]

    average = total / AREA
    return highest, lowest, total, average
    
    
# =============================================== 9 

def pig_latin(word):

    string = word
    
    if len(string) > 0:
        first_letter = string[0]
        if first_letter.lower() in VOWELS:
            string += 'way'
        else:
            first_loop = True
            while not (string[0].lower() in (VOWELS+'y')) or first_loop:
                first_loop = False
                string = (string[0].isupper() and string[1:].capitalize() or string[1:]) + string[0].lower()
            string += 'ay'  
            
    return string

