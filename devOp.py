# The num variable stores the input and converts input to int
num = int(input("Guess A Number From 1-100 :"))
# Checks if the input is 42 if not continue loop
while num!=42:

    print("Incorrect")
    num = int(input("Guess A Number From 1-100 :"))

print("Correct")    