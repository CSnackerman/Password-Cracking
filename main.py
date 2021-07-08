import random

# *******************
# --- variables --- *
# *******************

valid_chars = ""

password_length = 3
password = ""

iterators = []
inc_points = []


# ***************
# --- setup --- *
# ***************

# white-list the characters
for ascii_val in range (33, 127):

    valid_chars += chr (ascii_val)

# print result
print ("\n--- Valid Password Characters ---")
print (valid_chars)

num_valid = len (valid_chars)
print ("num_valid =", num_valid)


# generate a random password
for symbol in range (password_length):

    index = random.randint (0, num_valid - 1)

    c = valid_chars [index]

    password += c

# print result
print ("\n--- Generated Password ---")
print (password)



# *********************
# --- brute force --- *
# *********************

print ("\n--- Brute Force ---")

# create a list of iterators (one for each password character)
# these will count up sort of like a clock with many hands
# all start at 0
for i in range (password_length):
    iterators.append (0)

# calculate the points where each "digit" gets incremented
# append them to the list
for i in range (1, password_length):
    inc_points.append (num_valid ** i)

print ("inc_points =", inc_points)

# calculate total possible combinations + print
num_combos = num_valid ** password_length
print ("num_combos =", "{:,}".format(num_combos), "\n")

# count up until completion
for combo in range (num_combos):

    print ("num_combos =", "{:,}".format(num_combos), "\n")

    print ("inc_points =", inc_points)

    print ("\ncombo# =", combo)

    print ("iterators =", iterators)

    # tick
    iterators [0] = (iterators [0] + 1) % num_valid
    
    # check for incrementations
    for i in range (len (inc_points) - 1):
        if combo > 0 and combo % inc_points [i] == inc_points [i] - 1:
            iterators [i + 1] += 1
            iterators [i] = 0
        

            input ("press enter to continue...")

    # TODO fix 2nd digit not incrementing properly for password length 3





