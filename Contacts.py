import pickle
import firsname as f

def contact_read():
    file = open('fname', 'rb')

    data = pickle.load(file)

    file.close()

    file2 = open('lname', 'rb')

    data2 = pickle.load(file2)

    file2.close()

    print('Showing Contact Info: \n')
    print('Name: ' + data + ' '+ data2 + '\n')

f.fname()
f.lname()
contact_read()