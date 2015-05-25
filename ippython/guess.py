/usr/bin/python
#!/usr/bin/python
number = "42"
print "Guess my number...."
guess = raw_input(">")
if guess == number:
    print "Yes! that's it!"
else:
    print "No - It's", number
raw_input("Hit enter to continue")
