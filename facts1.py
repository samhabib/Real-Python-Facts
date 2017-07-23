There is actually a poem written by Tim Peters named as THE ZEN OF PYTHON which can be read by just writing import this in the interpreter.

# Try to guess the result before you actually run it
import this


One can return multiple values in Python. Don’t believe ? See the below code snippet:

# Multiple Return Values in Python!
def func():
   return 1, 2, 3, 4, 5
 
one, two, three, four, five = func()
 
print(one, two, three, four, five)


3. One can use an “else” clause with a “for” loop in Python. It’s a special type of syntax that executes only if the for loop exits naturally, without any break statements.

def func(array):
     for num in array:
        if num%2==0:
            print(num)
            break # Case1: Break is called, so 'else' wouldn't be executed.
     else: # Case 2: 'else' executed since break is not called
        print("No call for Break. Else is executed") 
 
print("1st Case:")
a = [2]
func(a)
print("2nd Case:")
a = [1]
func(a)

4. In Python, everything is done by reference. It doesn’t support pointers.

5. Function Argument Unpacking is another awesome feature of Python. One can unpack a list or a dictionary as function arguments using * and ** respectively. This is commonly known as the Splat operator. Example here

def point(x, y):
    print(x,y)
 
foo_list = (3, 4)
bar_dict = {'y': 3, 'x': 2}
 
point(*foo_list) # Unpacking Lists
point(**bar_dict) # Unpacking Dictionaries


6. Want to find the index inside a for loop? Wrap an iterable with ‘enumerate’ and it will yield the item along with its index. See this code snippet

# Know the index faster
vowels=['a','e','i','o','u']
for i, letter in enumerate(vowels):
    print (i, letter)
    
7. One can chain comparison operators in Python answer= 1<x<10 is executable in Python. More examples here

# Chaining Comparison Operators
i = 5;
 
ans = 1 < i < 10
print(ans)
 
ans = 10 > i <= 9
print(ans)
 
ans = 5 == i
print(ans)
