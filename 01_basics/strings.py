# =========== string manipulation ============= #

# list      0123456789
sentence = 'hello, jo!'

# [index]
sentence[9] # return (!)

# [start : end]                4567 [8]
sentence[4:8] # return (o, j)

# [start : end : interval]        02468 
sentence[0:10:2] # return (hlo o)

# [0 : 5] the same [5 : end string]
sentence[:5] # return (hello)

len(sentence) # return 10 (lenght of string)

# to count a caracter
sentence.count('o') # return 2

# to count a caracter in an interval
sentence.count('o', 6, 10) # return 1

# to find something in a string - if didn't find it return [-1]
sentence.find('lo') # return [3]

# to have a boolean to find
'hello' in sentence # return true

# to replace items - don't change origin
sentence.replace('jo', 'CJ') # return 'hello, CJ!'

# text transform
sentence.upper() # return 'HELLO, JO!' 
sentence.lower() # return 'hello, jo!'
sentence.capitalize() # return 'Hello, jo!' with only H upper
sentence.title() # return 'Hello Jo!' with start letter upper
sentence.strip() # return 'hello, jo!' without white spaces in begin or end
sentence.rsplit() # right
sentence.lstrip() # left

# divide string            01234  012
sentence.split() # return [hello][jo!] -> [0,1]

# to join string
'-'.join(sentence) # return 'hello-jo!'

# use """ text """ to keep format <prev>
print("""hello 
world! """) 
# return hello
#        world

# FORMAT f-strings

dollar = 100
# can use .format() instead f''
print('The bag price is US${}'.format(dollar))

# you can use expression/functions/modifier inside {} 
txt = f"It is very {'Expensive' if dollar>50 else 'Cheap'}"
print(txt)

# to format float use {var:.nf} n=number to case
print(f'Price is US${dollar:.2f}')

# can use modifier
result = f"The price is {dollar:,.2f} dollars"
print(result)

# Formatting Types MODIFIERS
# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding Unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format



