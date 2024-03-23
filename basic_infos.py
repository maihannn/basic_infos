# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Program #3: Add more info to ask and display.

# Ask for name.

name_input = input ("\033[0;32m" + "Enter your Name: " + "\033[0;37m")

# Ask for age.

age_input =  input ("\033[0;32m" + "Enter you Age: " + "\033[0;37m")

# Ask for address.

address_input = input ("\033[0;32m" + "Enter your Address: " + "\033[0;37m")

# Ask for contact number.

contact_input = input ("\033[0;32m" + "Enter your Contact Number: " + "\033[0;37m")

# Ask for hobbies.

hobbies_input = input ("\033[0;32m" + "What are your Hobbies : " + "\033[0;37m")

# Ask for favorite color.

color_input = input ("\033[0;32m" + "What is your Favorite Color: " + "\033[0;37m")

# Ask for dream job.

dream_job_input = input (str ("\033[0;32m" + "Enter your dream job: " + "\033[0;37m"))

# Display output.

print ("\n" + "\033[0;37m" + "Hi " + "\033[0;33m" + "\033[3m" + name_input + "!")
print ("\n" + "\033[0;37m" + "You are currently  " + "\033[0;33m" + "\033[3m" + age_input + ".")
print ("\n" + "\033[0;37m" + "You are currently residing in " + "\033[0;33m" + "\033[3m" + address_input + ".")
print ("\n" + "\033[0;37m" + "Contact Number: " + "\033[0;33m" + "\033[3m" + contact_input)
print ("\n" + "\033[0;37m" + "Your Hobbies are: " + "\033[0;33m" + "\033[3m" + hobbies_input + "!")

if color_input == "Red":
    print ("\n" +  "\033[0;37m" + "Your Favorite Color is  " + "\033[0;31m" + "\033[3m" + color_input + ".")
elif color_input == "Yellow":
    print ("\n"+  "\033[0;37m" + "Your Favorite Color is  " + "\033[0;33m" + "\033[3m" + color_input + ".")
elif color_input == "Green":
    print ("\n" + "\033[0;37m" + "Your Favorite Color is  " + "\033[0;32m" + "\033[3m" + color_input + ".")
elif color_input == "Blue":
    print ("\n" + "\033[0;37m" + "Your Favorite Color is  " + "\033[0;34m" + "\033[3m" + color_input + ".")
elif color_input == "Cyan":
    print ("\n" + "\033[0;37m" + "Your Favorite Color is  " + "\033[0;36m" + "\033[3m" + color_input + ".")
elif color_input == "Purple":
    print ("\n" + "\033[0;37m" + "Your Favorite Color is  " + "\033[0;35m" + "\033[3m" + color_input + ".")
else:
    print ("\n" + "\033[0;37m" + "Your Favorite Color is  " + "\033[0;37m" + "\033[3m" + color_input + ".")
    
print ("\n" +  "\033[0;37m" + "Your dream job is to be a " + "\033[0;33m" + "\033[3m" + dream_job_input + "!")