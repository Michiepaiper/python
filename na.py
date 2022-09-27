# determine the classes for each age grade
# ages 5 go to kindergarten
# ages 6-17 -> grades 1-12
# ages greater than 17 -> college

# recieve age and store in age
age = eval(input("Enter age: "))

# and : if both are true it returns true
# or : if either condition is true then true
# not : convert a true statement into false                                                               # if age is 5 == kindergarten
if (age <= 5):                                           print("Go to kindergarten")                                                                               # if age is both greater or equal to 6 and less than or equal to 17 -> grades 1-12
elif (age >= 6) and (age <= 17):
    print("Go to grade 1-12")

# if age is greater than 17 -> college less than 17 convert true to false and vice versa
elif not(age < 17):
    print("College")

else:
    print("Go to College")
