# OPSDESK — CUSTOMER INTAKE V0.2

# SECTION 1 — CLEAN
def clean_name(name):
    return name.strip()


# SECTION 2 — VALIDATE
def val_name(first_name, last_name):

    if '' == first_name or '' == last_name:
        return True

    else:
        return False

# SECTION 3 — MAIN
# SECTION 3 — MAIN

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

first_name = clean_name(first_name)
last_name = clean_name(last_name)

# SECTION 3 — MAIN

if val_name(first_name, last_name):
    print("Error: Both names are required.")

else:
    print(f"{first_name} {last_name}")

    customers = {
        "first_name": first_name,
        "last_name": last_name
    }

    print(customers)

     # YOUR NEXT TASK:
    # Access the last_name value through
    print(customers['last_name'])
                    
    customers.update ({'last_name': 'Johnson'})
    # the dictionary and print it.

print(customers)