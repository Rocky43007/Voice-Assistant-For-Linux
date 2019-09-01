import pickle

def fname():
    firstname = raw_input('Enter the contact\'s firstname: ')

    if firstname == False:
        firstname = raw_input('Enter the contact\'s firstname: ')
    else:
        print('Oops! Name Already in Contacts!')
        exit()

    file = open('fname', 'wb')

    pickle.dump(firstname, file)

    file.close()

def lname():
    lastname = raw_input('Enter the contact\'s lastname: ')

    if lastname == False:
        lastname = raw_input('Enter the contact\'s lastname: ')
    else:
        print('Oops! Name Already in Contacts.')

    file = open('lname', 'wb')

    pickle.dump(lastname, file)

    file.close()

