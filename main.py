# Marisol Morales & Andreas Moreno, 2/21/24, Classes & Objects Lab 4

import check_input
from contact import Contact


def read_file():
  contacts = []
  with open(r"addresses.txt", "r") as file:
    for line in file:
      info = line.strip().split(',')
      contact = Contact(*info) 
      contacts.append(contact)
  contacts.sort()
  return contacts
  

def write_file(contacts):
    with open('addresses.txt', 'w') as file:
      for contact in contacts:
        file.write(repr(contact) + '\n')

def get_menu_choice():
  print('Rolodex Menu:')
  print('1. Display Contacts')
  print('2. Add Contact')
  print('3. Search Contacts')
  print('4. Modify Contact')
  print('5. Save and Quit')
  return check_input.get_int_range('>', 1, 5)
  
def modify_contact(con):
  while True:
    print('Modify menu:')
    print('1. First Name')
    print('2. Last Name')
    print('3. Phone')
    print('4. Address')
    print('5. City')
    print('6. Zip')
    print('7. Save')
    
    user_choice = check_input.get_int_range('>', 1, 7)
    
    if user_choice == 7:
      break 
      
    elif user_choice == 1:
      new_first = input('Enter first name: ')
      con.fn = new_first
    elif user_choice == 2:
      new_last = input('Enter last name: ')
      con.ln = new_last
    elif user_choice == 3:
      new_phone = input('Enter phone number: ')
      con.ph = new_phone
    elif user_choice == 4:
      new_address = input('Enter address: ')
      con.addr = new_address
    elif user_choice == 5:
      new_city = input('Enter city: ')
      con.city = new_city
    elif user_choice == 6:
      new_zip = input('Enter zip: ')
      con.zip = new_zip

def main():
  contacts = read_file()
  while True:
    user_choice = get_menu_choice()

    if user_choice == 1:
      print(f'Number of contacts: {len(contacts)}')
      for i, contact in enumerate(contacts, 1):
        print(f'{i}.{contact}')
        print()
        
    elif user_choice == 2:
      print('Enter new contact: ')
      first_name = input('First name: ')
      last_name = input('Last name: ')
      phone = input('Phone number: ')
      address = input('Address: ')
      city = input('City: ')
      zip_code = input("Zip code: ")
      print()
      new_contact = Contact(first_name, last_name, phone, address, city, zip_code)
      contacts.append(new_contact)
      contacts.sort()
      write_file(contacts)
      
    elif user_choice == 3:
      found = False
      print('Search: ')
      print('1. Search by last name')
      print('2. Search by zip')
      user_search = check_input.get_int_range('>', 1, 2)
      if user_search == 1:
        user_last = input('Enter last name: ')
        print()
        for contact in contacts:
          if user_last.lower() == contact.ln.lower():
            print(contact.__str__())
            print()
            found = True
        if found is not True:
          print('Contact not found.')
      if user_search == 2:
        user_zip = input('Enter zip code: ')
        print()
        for contact in contacts:
          if user_zip == contact.zip:
            print(contact.__str__())
            print()
            found = True
        if found is not True:
          print('Contact not found.')
      
    elif user_choice == 4:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        found_contact = None
        for contact in contacts:
          if first_name == contact.fn and last_name == contact.ln:
            found_contact = contact
            break
        if found_contact:
          print("\nFound Contact:")
          print(found_contact)
          modify_contact(found_contact)
          contacts.sort()
        else:
          print("Contact not found.")  
      
    elif user_choice == 5:
      print('Saving...')
      write_file(contacts)
      print('Ending program')
      break


main()

