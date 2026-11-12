#clean
def clean_email(email):
    
    
    return email.strip().lower()

#val
def val_email(email):


    if email == '':
        return 'Email cannot be blank.'    
    
    elif '@' not in email:
        return 'Need @ in email.'

    elif not email.endswith('.com') and not email.endswith('.edu') and not email.endswith('.org') and not email.endswith('.net'):
        return 'Email needs .com, .edu, .org, .net'

    elif ' ' in email:
        return 'Email cannot have spaces.'


    else:

        return 'valid'

        
#compare 

#main 
def controller():

    email = input(' Enter your email: ')
    confirm_email = input(' Please confirm email: ')
     
    email = clean_email(email)
    confirm_email = clean_email(confirm_email)
    
    result = email 
    result = val_email(email)
    match = result
    print(result)
    print(match)



controller()

# STEP 1 — Collect both email inputs


    # STEP 2 — Clean each email independently


    # STEP 3 — Validate the cleaned primary email
    # Store the returned message separately


    # STEP 4 — Compare both cleaned emails
    # Store the Boolean separately


    # STEP 5 — Display the email and both results
