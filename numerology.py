alphabets = {'A':1,'J':1, 'S':1, 'B':2, 'K':2, 'T':2,'C':3, 'L':3, 'U':3,  'D':4, 'M':4, 'V':4,'E':5,
                  'N':5,'Ö':5, 'F':6, 'O':6,'X':6,'G':7, 'P':7, 'Y':7, 'H':8, 'Q':8, 'Z':8,'I':9, 'Ü':9, 'R':9,}


word1 = input("Please write your first name: ")

#select letters' value
def digit_sum(n):
    numbers=[]
    for digit in str(n):
        numbers.append(int(digit))

    total = 0
    for number in numbers:
        total += number
    return total

#after calculate
def numerology(word1):
        total = 0
        for letter in word1.upper():
            total += alphabets[letter]
            total = digit_sum(total)

        return total

print(numerology(word1))

word2 = input("Please write your surname: ")

#select letters' value
def digit_sum(n):
    numbers=[]
    for digit in str(n):
        numbers.append(int(digit))

    total = 0
    for number in numbers:
        total += number
    return total

#after calculate
def numerology(word2):
        total = 0
        for letter in word2.upper():
            total += alphabets[letter]
            total = digit_sum(total)

        return total

print(numerology(word2))

x = int(numerology(word1))
y = int(numerology(word2))

z = x+y

if z == 11 or z == 22:
    sum_of_digits = z
    if z== 33:
        sum_of_digits = z
        
    

else:
    sum_of_digits = 0 
    for digit in str(z):
        sum_of_digits += int(digit)


 
print(sum_of_digits)

if sum_of_digits == 1:
    print("You have leader soul")

elif sum_of_digits == 2:
    print("You have romantic soul")

elif sum_of_digits == 3:
    print("You have gamer soul")

elif sum_of_digits == 4:
    print("You have guaridan soul")

elif sum_of_digits == 5:
    print("You have innovator soul")

elif sum_of_digits == 6:
    print("You have parent soul")

elif sum_of_digits == 7:
    print("You have emotional soul")

elif sum_of_digits == 8:
    print("You have earthly soul")

elif sum_of_digits == 9:
    print("You have artist soul")

elif sum_of_digits == 11:
    print("You are alien")

elif sum_of_digits == 22:
    print("You are master")

elif sum_of_digits == 33:
    print("You are saint")



    





        
    
        
        

