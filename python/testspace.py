'''G:n7]N03300962' should equal 'G:n7]N 3300962'''
def increment_string(strng):
    numbers = ''
    
    for i in range(len(strng)-1,-1,-1):
        if not strng[i].isdigit():
            break
        else:
            number = strng[i] + numbers
            
    if len(numbers) == 0:
        return strng + "1"
    else:
        num_length = len(numbers)
        number = int(strng[len(strng)-num_length:]) +1
        if number //10 > (number-1) // 10:
            return(strng[:len(strng)-num_length]+"0"*(num_length-len(str(number)))+str(number))
        else:
            return(strng[:len(strng)-num_length]+"0"*(num_length-len(str(number)))+str(number))

print(increment_string('G:n7]N03300962'))
'''def increment_string(strng):
    #number = ''.join([strng[n] for n in range(len(strng)-1,-1,-1) if strng[n].isdigit()])
    number = ''
    for i in range(len(strng)-1,-1,-1):
        if not strng[i].isdigit():
            break
        else:
            number = strng[i] + number
    if not number:
        return strng + "1"
    if number //10 > (number +1) //10:
        
    print(number)
    return strng[:-len(number)] + number
'''
