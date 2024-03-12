# functions
#- consists of function name, parameters.
# - starts "def" keyword.
# - Optimizes and make a block off code reuseable

def averageOfThreeNumbers(num1, num2, num3):
    #codes..
    average = (num1 + num2 + num3) / 3
    print("Average: ", average)
#Shortcut for copying highlighted/Single Line : alt + shift + ArrowDown/ArrowUp
#Shortcute for repositioning highlighted/Single Line : alt + arrowUp/Down
averageOfThreeNumbers(89,76,81)
averageOfThreeNumbers(89,76,81)
averageOfThreeNumbers(89,76,81)

#return function
title ="ang alamat ni loudie"
title2 ="Bagsakan Era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def joinString(message, message2):
    return message.join(message2)


print(stringToTitle(title))
print(stringToLowercase(title))
print(stringToUppercase(title))    
print(joinString(title,title2))    
