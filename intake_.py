#Create a function called clean_phone(number) that removes leading and trailing spaces.
def clean_phone (number):
    return number.strip()


#Ask the user to enter their phone number.
number = input('Enter your number.')



#Ask the user to confirm their phone number.
confirm_phone = input('Confirm your number.')



#Clean both inputs using your function.
#Both cleaned numbers match.
#The number contains exactly 10 characters.
#Every character is a digit.
number = clean_phone(number)
confirm_phone = clean_phone(confirm_phone)
    


#Use if/else to check whether the two numbers match.
if number != confirm_phone:
    print('Numbers do not match')

    return False
    
    
elif (len(number) != 10):
    print('Error needs 10 digits.')


    return False

elif (not number.isdigit()) and (not confirm_phone.isdigit()):
    print('')

    return False

else:
    
    return True





