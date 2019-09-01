import pickle


def email():
    email = raw_input('Enter the contact\'s Emaol: ')

    if email== False:
        email = raw_input('Enter the contact\'s email: ')
    else:
        print('Oops! Email Already in Contacts!')
        exit()

    file = open('email', 'wb')

    pickle.dump(email, file)

    file.close()

def lname():
    phonenumber = raw_input('Enter the contact\'s phonenumber: ')

    if phonenumber == False:
        phonenumber = raw_input('Enter the contact\'s phonenumber: ')
    else:
        print('Oops! Phone Number Already in Contacts.')

    file = open('phonenumber', 'wb')

    pickle.dump(phonenumber, file)

    file.close()


def change():
    if open('email', 'wb')
