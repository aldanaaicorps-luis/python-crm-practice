# EMAIL CONFIRMATION FOR CRM

# clean_email()        -> only cleans
# emails_match()       -> only checks if two emails match
# validate_email()     -> only checks if email format is acceptable
# get_confirmed_email() -> controls retry attempts


def clean_email(email):
    return email.strip().lower()


def emails_match(email, confirm_email):
    email = clean_email(email)
    confirm_email = clean_email(confirm_email)
    return email == confirm_email


def validate_email(email):
    email = clean_email(email)

    if email == "":
        return "Email cannot be blank."
    elif " " in email:
        return "Email cannot contain spaces."
    elif "@" not in email:
        return "Email must contain @."
    elif email.count("@") != 1:
        return "Email can only contain one @."
    elif "." not in email:
        return "Email must contain a domain like .com, .org, or .net."
    elif not email.endswith(".com") and not email.endswith(".org") and not email.endswith(".net"):
        return "Email must end with .com, .org, or .net."
    else:
        return "valid"


def get_confirmed_email():
    attempts = 0

    while attempts < 5:
        email = input("Enter your email: ")
        confirm_email = input("Confirm your email: ")

        email = clean_email(email)
        confirm_email = clean_email(confirm_email)

        if not emails_match(email, confirm_email):
            print("Emails do not match.")
            attempts += 1
            continue

        validation_result = validate_email(email)

        if validation_result != "valid":
            print(validation_result)
            attempts += 1
            continue

        print("Email confirmed.")
        return email

    print("Too many attempts. Please try again later.")
    return None


customer_email = get_confirmed_email()

if customer_email is None:
    exit()

print("Saved customer email:", customer_email)

#NAME CONFIRMATION
def clean_name(name):
    
    return name.strip() 

def names_match(name, confirm_name):
    
    return clean_name(name) == clean_name(confirm_name)    

def validate_name(name):
    name = clean_name(name)
    
    
    if name == "":
        
        return "Name cannot be blank. Please try again."

    else:
        print ("Names cannot be blank. Please try again.") 

        return name 

def get_confirmed_name(field_name):

    attempts = 0

    while attempts < 5:
        name = input("Enter your name.")
        confirm_name = input("Confirm your name.")

        name = clean_name(name)
        confirm_name = clean_name(confirm_name)

        if not names_match(name, confirm_name):
                print("Names do not match.")
                
                attempts += 1
                
                continue 
        
        validation_result = validate_name(name)

        if validation_result != "valid":
            
            print(validation_result)
            
            attempts += 1
            
            continue

        print("Name confirmed.")
        
        return (name)
    
    print("Too many attempts. Please try again.")
    
    return None
            







#phone number confirmation
def clean_phone_number(number)
    return number.strip()


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

zip_code = input('Enter your Zip Code:').strip()
confirm_zip_code = input('Confirm your Zip Code:').strip()

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
#employee name confirmation
emp_name = input('Enter employee name:').strip().capitalize()
confirm_emp_name = input('Confirm employee name:').strip().capitalize()

while emp_name != confirm_emp_name:
    print('Names do not match.')
    emp_name = input('Enter employee name:').strip().capitalize()
    confirm_emp_name = input('Confirm employee name:').strip().capitalize()
    if emp_name == confirm_emp_name:
        print('Employee name confirmed.')
    elif emp_name != confirm_emp_name:
         print('Names do not match. Please try again.')
    else:
        print('Employee name confirmed.')
#employee email, phone number, address, city, state, zip code, and employee number confirmation
emp_email = input('Enter employee email:').strip().lower()
confirm_emp_email = input('Confirm employee email:').strip().lower()
while emp_email != confirm_emp_email:
    print('Emails do not match.')
    emp_email = input('Enter employee email:').strip().lower()
    confirm_emp_email = input('Confirm employee email:').strip().lower()
    if emp_email == confirm_emp_email:
        print('Employee email confirmed.')
    elif emp_email != confirm_emp_email:
         print('Emails do not match. Please try again.')
    else:
        print('Employee email confirmed.')
#employee phone number

emp_phone = input('Enter employee phone number:').strip()
confirm_emp_phone = input('Confirm employee phone number:').strip()
while emp_phone != confirm_emp_phone:
    print('Phone numbers do not match.')
    emp_phone = input('Enter employee phone number:').strip()
    confirm_emp_phone = input('Confirm employee phone number:').strip()
    if emp_phone == confirm_emp_phone:
        print('Employee phone number confirmed.')
    elif emp_phone != confirm_emp_phone:
         print('Phone numbers do not match. Please try again.')
    else:
        print('Employee phone number confirmed.')
# emplooyee address
emp_address = input('Enter employee address:').strip()
confirm_emp_address = input('Confirm employee address:').strip()
while emp_address != confirm_emp_address:
    print('Addresses do not match.')
    emp_address = input('Enter employee address:').strip()
    confirm_emp_address = input('Confirm employee address:').strip()
    if emp_address == confirm_emp_address:
        print('Employee address confirmed.')
    elif emp_address != confirm_emp_address:
         print('Addresses do not match. Please try again.')
    else:
        print('Employee address confirmed.')
#employee city, 

emp_city = input('Enter employee city:').strip().capitalize()
confirm_emp_city = input('Confirm employee city:').strip().capitalize()
while emp_city != confirm_emp_city:
    print('Cities do not match.')
    emp_city = input('Enter employee city:').strip().capitalize()
    confirm_emp_city = input('Confirm employee city:').strip().capitalize()
    if emp_city == confirm_emp_city:
        print('Employee city confirmed.')
    elif emp_city != confirm_emp_city:
         print('Cities do not match. Please try again.')
    else:
        print('Employee city confirmed.')
#employee state
emp_state = input('Enter employee state:').strip().capitalize()
confirm_emp_state = input('Confirm employee state:').strip().capitalize()
while emp_state != confirm_emp_state:
    print('States do not match.')
    emp_state = input('Enter employee state:').strip().capitalize()
    confirm_emp_state = input('Confirm employee state:').strip().capitalize()
    if emp_state == confirm_emp_state:
        print('Employee state confirmed.')
    elif emp_state != confirm_emp_state:
         print('States do not match. Please try again.')
    else:
        print('Employee state confirmed.')
#employee zip code 
emp_zip_code = input('Enter employee zip code:').strip()
confirm_emp_zip_code = input('Confirm employee zip code:').strip()
while emp_zip_code != confirm_emp_zip_code:
    print('Zip codes do not match.')
    emp_zip_code = input('Enter employee zip code:').strip()
    confirm_emp_zip_code = input('Confirm employee zip code:').strip()
    if emp_zip_code == confirm_emp_zip_code:
        print('Employee zip code confirmed.')
    elif emp_zip_code != confirm_emp_zip_code:
         print('Zip codes do not match. Please try again.')
    else:
        print('Employee zip code confirmed.')
#employee country
emp_country = input('Enter employee country:').strip().capitalize()
confirm_emp_country = input('Confirm employee country:').strip().capitalize()
while emp_country != confirm_emp_country:
    print('Countries do not match.')
    emp_country = input('Enter employee country:').strip().capitalize()
    confirm_emp_country = input('Confirm employee country:').strip().capitalize()
    if emp_country == confirm_emp_country:
        print('Employee country confirmed.')
    elif emp_country != confirm_emp_country:
         print('Countries do not match. Please try again.')
    else:
        print('Employee country confirmed.')
#employee social security number
emp_social_security_number = input('Enter employee social security number:').strip()
confirm_emp_social_security_number = input('Confirm employee social security number:').strip()
while emp_social_security_number != confirm_emp_social_security_number:
    print('Social security numbers do not match.')
    emp_social_security_number = input('Enter employee social security number:').strip()
    confirm_emp_social_security_number = input('Confirm employee social security number:').strip()
    if emp_social_security_number == confirm_emp_social_security_number:
        print('Employee social security number confirmed.')
    elif emp_social_security_number != confirm_emp_social_security_number:
         print('Social security numbers do not match. Please try again.')
    else:
        print('Employee social security number confirmed.')
#employee employee number
emp_employee_number = input('Enter employee number:').strip()
confirm_emp_employee_number = input('Confirm employee number:').strip()
while emp_employee_number != confirm_emp_employee_number:
    print('Employee numbers do not match.')
    emp_employee_number = input('Enter employee number:').strip()
    confirm_emp_employee_number = input('Confirm employee number:').strip()
    if emp_employee_number == confirm_emp_employee_number:
        print('Employee number confirmed.')
    elif emp_employee_number != confirm_emp_employee_number:
         print('Employee numbers do not match. Please try again.')
    else:
        print('Employee number confirmed.')
#employee information export to text file
        
file = open('employee_info.txt', 'w')
contents = (f'Employee Name: {emp_name}\n'
            f'Employee Zip Code: {emp_zip_code}\n'
            f'Employee Country: {emp_country}\n'
            f'Employee Social Security Number: {emp_social_security_number}\n'
            f'Employee Number: {emp_employee_number}\n')
file.write(contents)
file.close()
#employee lookup
employee_lookup = input('Would you like to view the employee information? (yes/no): ').strip().lower()
if employee_lookup == 'yes':
    file = open('employee_info.txt', 'r')
    saved_employee = file.read()
    file.close()
    print('\nSaved Employee Information:')
    print(saved_employee)
#employee hours worked confirmation
scheadule_employee = input('Would you like to schedule an employee? (yes/no): ').strip().lower()
if scheadule_employee == 'yes':
    emp_name = input('Enter employee name:').strip().capitalize()
    emp_sched_hours = input('Enter employee scheduled hours:').strip()
    employee_number = input('Enter employee number:').strip()
    confirm_emp_sched_hours = input('Confirm employee scheduled hours:').strip()
#employee clockin 
emp_clockin = input('Enter employee clock-in time:').strip()
emp_confirm_clockin = input('Confirm employee clock-in time:').strip()
while emp_clockin != emp_confirm_clockin:
    print('Clock-in times do not match.')
    emp_clockin = input('Enter employee clock-in time:').strip()
    emp_confirm_clockin = input('Confirm employee clock-in time:').strip()
    if emp_clockin == emp_confirm_clockin:
        print('Employee clock-in time confirmed.')
    elif emp_clockin != emp_confirm_clockin:
         print('Clock-in times do not match. Please try again.')
    else:
        print('Employee clock-in time confirmed.')
#employee clockout
emp_clockout = input('Enter employee clock-out time:').strip()
emp_confirm_clockout = input('Confirm employee clock-out time:').strip()
while emp_clockout != emp_confirm_clockout:
    print('Clock-out times do not match.')
    emp_clockout = input('Enter employee clock-out time:').strip()
    emp_confirm_clockout = input('Confirm employee clock-out time:').strip()
    if emp_clockout == emp_confirm_clockout:
        print('Employee clock-out time confirmed.')
    elif emp_clockout != emp_confirm_clockout:
         print('Clock-out times do not match. Please try again.')
    else:
        print('Employee clock-out time confirmed.')
file = open('employee_schedule.txt', 'w')
contents = (f'Employee Name: {emp_name}\n'
            f'Employee Scheduled Hours: {emp_sched_hours}\n'
            f'Employee Number: {employee_number}\n'
            f'Employee Clock-in Time: {emp_clockin}\n'
            f'Employee Clock-out Time: {emp_clockout}\n')
file.write(contents)
file.close()
#total hours worked
emp_hours_worked = input('Enter employee hours worked:').strip()
emp_sched_hours = input('Enter employee scheduled hours:').strip()
emp_confirm_hours_worked = input('Confirm employee hours worked:').strip()
while emp_hours_worked != emp_confirm_hours_worked:
    print('Hours worked do not match.')
    emp_hours_worked = input('Enter employee hours worked:').strip()
    emp_confirm_hours_worked = input('Confirm employee hours worked:').strip()
    if emp_hours_worked == emp_confirm_hours_worked:
        print('Employee hours worked confirmed.')
    elif emp_hours_worked != emp_confirm_hours_worked:
         print('Hours worked do not match. Please try again.')
    else:
        print('Employee hours worked confirmed.')
#employee scheduled hours confirmation
emp_sched_hours = input('Enter employee scheduled hours:').strip()
emp_confirm_sched_hours = input('Confirm employee scheduled hours:').strip()
while emp_sched_hours != emp_confirm_sched_hours:
    print('Scheduled hours do not match.')
    emp_sched_hours = input('Enter employee scheduled hours:').strip()
    emp_confirm_sched_hours = input('Confirm employee scheduled hours:').strip()
    if emp_sched_hours == emp_confirm_sched_hours:
        print('Employee scheduled hours confirmed.')
    elif emp_sched_hours != emp_confirm_sched_hours:
         print('Scheduled hours do not match. Please try again.')
    else:
        print('Employee scheduled hours confirmed.')
file = open('employee_hours.txt', 'w')
contents = (f'Employee Name: {emp_name}\n'
            f'Employee Hours Worked: {emp_hours_worked}\n'
            f'Employee Scheduled Hours: {emp_sched_hours}\n')
file.write(contents)
file.close()

#calculate total hours worked #bid #materials #labor #permit cost #photos #punch list #rework #contract 
# #job #estimate #job #invoice #job #payment #job