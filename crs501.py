#EMAIL CONFIRMATION

email = input('Enter your email:')
confirm_email = input('Confirm your email:')

email = email.strip().lower()
confirm_email = confirm_email.strip().lower()
i = 0 
while email != confirm_email and i < 5:
    print('Emails do not match.')
    email = input('Enter your email:')
    confirm_email = input('Confirm your email:')
    email = email.strip().lower()
    confirm_email = confirm_email.strip().lower()
    i += 1

if email == confirm_email:
    print('Email confirmed.')
    
elif i == 5:
        print('Too many attempts. Please try again later.')



i += 1
#NAME CONFIRMATION
first_name = input('Enter your First Name: ')
first_name = first_name.strip().capitalize()
confirm_first_name = input('Confirm your First Name: ')
confirm_first_name = confirm_first_name.strip().capitalize()
last_name = input('Enter your Last Name: ')
last_name = last_name.strip().capitalize()
confirm_last_name = input('Confirm your Last Name: ')
confirm_last_name = confirm_last_name.strip().capitalize()

i = 0
while first_name != confirm_first_name and i < 5:
    print('First names do not match.')
    first_name = input('Enter your First Name: ')
    first_name = first_name.strip().capitalize()
    confirm_first_name = input('Confirm your First Name: ')
    confirm_first_name = confirm_first_name.strip().capitalize()
    i += 1

if first_name == confirm_first_name:
    print('First name confirmed.')
    i += 1

while last_name != confirm_last_name and i < 5:
    print('Last names do not match.')
    last_name = input('Enter your Last Name: ')
    last_name = last_name.strip().capitalize()
    confirm_last_name = input('Confirm your Last Name: ')
    confirm_last_name = confirm_last_name.strip().capitalize()
    i += 1

if last_name == confirm_last_name:
    print('Last name confirmed.')
    i += 1



#phone number confirmation
phone_number = input('Enter your phone number: ')
phone_number = phone_number.strip()
confirm_phone_number = input('Confirm your phone number: ')
confirm_phone_number = confirm_phone_number.strip()
i = 0
while phone_number != confirm_phone_number and i < 5:
    print('Phone numbers do not match.')
    phone_number = input('Enter your phone number: ')
    phone_number = phone_number.strip()
    confirm_phone_number = input('Confirm your phone number: ')
    confirm_phone_number = confirm_phone_number.strip()
    i += 1
    if i == 5:
        print('Too many attempts. Please try again later.')
        exit()

    else:
        print('Phone number confirmed.')

#COMPANY CONFIRMATION
company = input('Enter your company name: ')
company = company.strip().capitalize()
confirm_company = input('Confirm your company name: ')
confirm_company = confirm_company.strip().capitalize()
i = 0
while company != confirm_company and i < 5:
    print('Company names do not match.')
    company = input('Enter your company name: ')
    company = company.strip().capitalize()
    confirm_company = input('Confirm your company name: ')
    confirm_company = confirm_company.strip().capitalize()
    i += 1
    if i == 5:
        print('Too many attempts. Please try again later.')
        exit()

    else:
        print('Company name confirmed.')

address = input('Enter your address: ')
address = address.strip()
confirm_address = input('Confirm your address: ')
confirm_address = confirm_address.strip()
i = 0 
while address != confirm_address and i < 5:
    print('Addresses do not match.')
    address = input('Enter your address: ')
    address = address.strip()

    i += 1
    if i == 5:
        print('Too many attempts. Please try again later.')
        exit()

    else:
        print('Address confirmed.')

#city, state, zip code, country confirmation

city = input('Enter your City:').strip().capitalize()
confirm_city = input('Confirm your City:').strip().capitalize()

i = 0 
while city != confirm_city and i < 5:
    print('Cities do not match.')
    city = input('Enter your City:').strip().capitalize()
    confirm_city = input('confirm your City:').strip().capitalize()
    i += 1
    if i == 5:
        print('Too many attempts. Please try again later.')
        exit()

    else:
        print('City confirmed.')

#state zip code, country confirmation

state = input('Enter your state:').strip().capitalize()
confirm_state = input('Confirm your state:').strip().capitalize()

i = 0
while state != confirm_state and i < 5:
    print('States do not match.')
    state = input('Enter your State:').strip().capitalize()
    confirm_state = input('Confirm your State:').strip().capitalize()
    i += 1
    if i == 5:
        print('Too many attempts. Please try again later.')
        exit()

    else:
        print('State confirmed.')

#zip_code country

zip_code = input('Enter your Zip Code').strip()
confirm_zip_code = input('Confirm your Zip Code').strip()

i = 0 
while zip_code != confirm_zip_code and i < 5:
 print('Zip code does not match.')
 zip_code = input('Enter Zip Code:').strip()
 confirm_zip_code = input('Confirm Zip Code:').strip()

i += 1 

if i == 5:
    print('Too many attempts. Please try again later.')
    exit()

else:
    print('Zip Code confirmed.')
                 
                 
print(f'Name: {first_name} {last_name}')
print(f'Email: {email}')
print(f'Phone: {phone_number}')
print(f'Company: {company}')
print(f'Address: {address}')
print(f'city: {city}')
print(f'State: {state}')
print(f'Zip Code: {zip_code}')


#Exporting to a text file

file = open('customer_info.txt', 'w')
contents = (f'Name: {first_name} {last_name}\n'
f'Email: {email}\n'
f'Phone: {phone_number}\n'
f'Company: {company}\n'
f'Address: {address}\n'
f'City: {city}\n'
f'State: {state}\n'
f'Zip Code: {zip_code}\n')
file.write(contents)
file.close()

#enter employees