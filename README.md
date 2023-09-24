# 0910

### Printing things to the screen
Our first code is to print **Hello World** to the screen, in order to do that, we will need to use a $\textit{built in}$ function, denoted as print. 

```python
print("Hello World")
```

By doing so, we will be printing **Hello World** to the screen. If we look carefully, there are two **"** surrounding **Hello World**. When something that is sandwhiched by two **"**, it represents a **string**. One might ask, what is **string**? **string** is really referring to **word(s)**.
For example, ```This is a word```, ```hi```, ```k```,```Jayden```, ```Chloe```, ```Claire```,and ```jeffrey is a monster``` will be considered as ```string``` in python. 

So, if we want to print ```i love programming in python```, first we have to include two **"** from the beginning of the string and at the end of the string which will look like this, ```"i love programming in python"```. From here, we simply add that string and put it in side the **(**some_string**)**. So we end up having ```print("i love programming in python")```

Here is the template, you will need to replace __replace_your_own_string__ to what you would like to print. ```print("__replace_your_own_string__")```

In summary, string is just referring to word(s), where words include numbers and word(s) in general. 

### Variable
Variable, it is the same concept from math. However, some might not know what a variable yet, so lets talk about it for a second.

1. Think about this, if you adopt a dog or cat, what would you do first in general? You will give him / her a name right? So when we alott a name to a pet, a pet will have a name. 
2. When you were born, you do not have a name initially. So your parents gave you the name when they had one. 
3. When you mom asks you to clean up your room, you might find a storage box and put everything into the box so that you can organize things better right? Once you packed everything, you will give your box a name, toys, bunch of box or what ever you can imagine right? So, that box is a variable you simply give a name to it.

So, we are simply assigning some name to a box so that we can put something into the box. For now, we can name anything you would like, also, as for the values, it can be numbers or words.

for example, if we would to create a box that holds a number to represent your age, we can do the following:

1. 
```python
age = 20
```

We are simply saying, we name the box as age and we put the value 20 into age. So, the life span of this code, age will be always equal to 20. 

2.
```python
DogFoodPrice = 29.99
```
In this example, we want to put the price, 29.99, into box. And we would like to name the box as DogFoodPrice. So, during hte life span of this exceprt, DogFoodprice will be 29,99.

### Deep thinking,

How do we assign ```Jeffrey Chan``` into the box called name? In another word, create a variable call name and set it's value to ```Jeffrey Chan```.

### Getting Input
We can get input from you by typing some word(s) thru the keyboard. Since what you type is considered as a string in python, so by default, everything is a string when you use an ```input()```. 
For exapmle,
```python
age = input("How old are you?")
```
This code will ask you to input something and store what ever you have inputed thru the keyboard and it will store it in to age. 

If we input 5, age is 5. However, is it a string or actual number?

Example 2,
```python
name = input("What is your name?")
```
This code will ask you to input your name. If you input ```Jayden, Chloe, and Claire```, ```Jayden, Chloe, and Claire``` will be stored into name.

Example 3,
```python
age = int(input("How old are you?"))
```
This code will ask you to input your age. This time, we have ```int()``` wrap around ```input()```, what it does is as follow, and assume we input 10.
1. ```age = int(input("How old are you?"))```
2. you input 5, which means ```input("How old are you?")``` will become 5 once you input 5 from the keyboard and hit enter.
3. ```age = int(5)```, since what ever we get from input, it is a **string (word(s))**, and if we would like to use age as a number, we will need to convert it to number. So what ```int()``` does is, int itself is integer, we are basically converting what ever that is inside the **(...)** to integer. Thats it.
4. ```age = 5```
### Logical statements
Logical statement will help us to decide what should we do based on different kind of situations. 

For example, 
1. **if** we are all hungry, lets go to eat some pizza. We can put this in coding manner. 
```python
areYouHungry = "Yes"
if areYouHungry == "Yes":
	print("Lets eat")
else:
	print("Lets wait until we are hungry")
```
What we did here is create a varaible call ```areYouHungry``` and assign the value of string, ```"Yes"```, to it. if areYouHungry is "Yes", that means we want to eat. Otherwise, we are not hungry and we will wait.

2. Lets get input from the keyboard and ask the same question like (1).
```python
areYouHungry = input("Are you hungry?")
if areYouHungry == "Yes":
	print("Lets eat")
else:
	print("Lets wait until we are hungry")
```
It does the same thing as (1), the only thing that is differ from (1) is the ```input()```

### Logical statement operators

Lets talk about the logical statement operators. Basically it is strictly following the mathematical operators like the follwoing
1. ```<``` : less than
2. ```<=``` : less than or equal to
3. ```>``` : greaater than
4. ```>=``` : greater than or equal to
5. ```!=``` : that ! is saying not, so combine the two symbols together is saying not equal to
6. ```==``` : that is saying are the equal. 

So when we are using logical statement. We will be comparing two things, namely A and B. It can be **both** string or **both** number. You cant compair words with a number.

For example:

```python 
a = 10
b = 20
if a < b:
	print("a is less than b")
if a <= b:
	print("a is less than or equal to b")
if a > b:
	print("a is less than b")
if a >= b:
	print("a is less than or equal to b")
if a !=  b:
	print("a and b is not the same")
if a ==  b:
	print("a is the same as b")

```

Output:
```
a is less than b
a is less than or equal to b
a and b is not the same
a is the same as b
```

Now, lets analyze the **if else if structure**.
```python
food = input("Do you want fries, burger, or desert?)
if food == "fries":
	print("you get a fries for lunch")
elif food == "burger":
	print("you get a burger for lunch")
else:
	print("you get a desert for lunch")
```
In this case, we are checking what would you like to eat. If the value of food is fries, then you will get a fries. If the value of food is burger, you will get a burger for food, otherwise, we will get desert because we only offer three types of food.

We will only get one thing done among all possible branches. If we have the following
```python
if option == "A":
	print("A")
elif option == "B":
	print("B")
elif option == "C":
	print("C")
elif option == "D":
	print("D")
elif option == "E":
	print("E")
elif option == "F":
	print("F")
else: 
	print("G")
```
We will executed one out of seven branches. So, we are basically **pre define** what are the possible behavior of a certain program. 

Keypoint here is, it doesnt matter how many branches ( branches is really referring to the amount of if elif checkings) we have, only one of them will be executed. 


# 0917

### Review

1.What is a string?

2.What is the idea of variable?

3.How to get input from user thru the keyboard?

4.After getting the input from user thru the keyboard, can we apply math operation on it? For example
```python
age = input("Your age")
age = age + 5
```
If we input 20, will we get 25 in this case?

5. How to conver the input frmo string to age?

6. How we make decision? What is the magic word? 

### Logical Statements

Lets summarize our logical statements,
1. The following is the basic structure of if else statement. 
```python
if ...:
	statement A
else:
	statement B
```
2. We can add more branches by using the keyword **elif**

```python
if ...:
	statement A
elif ...:
	statement B
else:
	statement C
```
3. we can add more branches

```python
if ...:
	statement A
elif ...:
	statement B
elif ...:
	statement C
elif ...:
	statement D
elif ...:
	statement E
elif ...:
	statement F
else:
	statement G
```

These three particular structures, have the same common behaviour that is only one statement will be executed.

Lets analyze another type of statement, assume each statement will print something to the screen, find out how many statements will be printed at most?

1. 

```python
if ...:
	statement A
if ...:
	statement B
if ...:
	statement C
```

2.
```python
if ...:
	statement A
if ...:
	statement B
elif ...:
	statement C
```
3. 
```python
if ...:
	statement A
if ...:
	statement B
elif ...:
	statement C
else:
	statement D
if ...:
	statement E
```

# 0924

Remember the following:

```python
age = input("What ever the question you would like to ask")
```

1. age is the variable that stores a value from user. You can assign a specific value to age if you want , so input is not needed.
	a. example:
	```python
	age = 10
	```
	In this case, we assign 10 to age. So the value of age is 10.

2. if we have
```python
age = input("what ever question you would like to ask")
print(age + 5)
```
By default, the type of age is english, we cant do math on english words. As a result, we will need to convert the input to a number of convert the age to a number.

	a. method 1:
	```python
	age = int(input("what ever question you would like to ask"))
	print(age + 5)
	```

	b. method 2:
	```python
	age = int(input("what ever question you would like to ask"))
	print(int(age)+5)
	```

3. when we get the input as english word (the actual type is call string, short for **str**), and if we want to compare the result, for example

```python
age = input("what ever question you would like to ask")
if age == 3:
	print("you are 3 year old")
else:
	print("you are not 3 year old")
```

We will have an error here because english word cant compare with number. That means we will have to convert the value to either english or number to make it work.

```python
age = input("what ever question you would like to ask")
if age == "3":
	print("you are 3 year old")
else:
	print("you are not 3 year old")
```

Problem Day:

1. Code up a simple algorithm that takes input and store your name, age, and gender. Then print out your name, age, and gender. After that, decide if you are at least 18 year old or not. If you are over 18, print you are older than 18. Otherwise, you are younger than 18.

2. Get two ages from user and check if the sum of two ages are greater than 50. 


















