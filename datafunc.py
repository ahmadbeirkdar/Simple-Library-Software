import csv
from datetime import datetime 
def read_data(filename):
    data =[]
    with open(filename) as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for line in csv_data:
            data.append(line)
    return data

def takeout(object, id, pid, filename):
    data = read_data(filename)
    flag = True
    for i in data:
        if int(i[0]) == id:
            print(f"ERROR: The following book is already signed out by {object.data_person[int(i[1])].name} on the data {i[2]}")
            flag = False
            break
    if len(data) == 0 or flag == True:
        datenow = datetime.now()
        with open(filename, mode='a+') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_data.writerow([id,pid,str(datenow)])
        print(f"\n{object.data_person[pid].name} has taken out the following book:\n{object.data_books[id]}")

def bringback(object,id,pid,filename):
    data = read_data(filename)
    flag = True
    for i in data:
        if int(i[0]) == id:
            flag = False
    if flag == True:
        print("ERROR: The following book was not signed out!")
    else:
        for i in range(0,len(data)):
            if int(data[i][0]) == id:
                del data[i]
                break
        with open(filename, mode='w') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in data:
                csv_data.writerow(i)
        print(f"\n{object.data_person[pid].name} has signed in the following book:\n{object.data_books[id]}")
        



def user_search_id(object, id, filename):
    id = int(id)
    data = read_data(filename)
    books = []
    dates = []
    for i in data:
        if int(i[1]) == id:
            books.append(object.data_books[int(i[0])])
            dates.append(i[2])
    if len(books) == 0:
        print("No loans under this account")
    else:
        print(f"\n{object.data_person[id].name} has the following books out: ")
        j = 0
        for i in books:
            print(i)
            print(f"\tOn: {dates[j]}\n")
            j += 1

def username_search(object, username, filename):
    data = read_data(filename)
    books = []
    dates = []
    id = None
    for i in object.data_person:
        if str(i.username) == str(username):
            id = int(i.pID)
    if id != None:
        for i in data:
            if int(i[1]) == id:
                books.append(object.data_books[int(i[0])])
                dates.append(i[2])
        if len(books) == 0:
            print("No loans under this account")
        else:
            print(f"\n{object.data_person[id].name} has the following books out: ")
            j = 0
            for i in books:
                print(i)
                print(f"\tOn: {dates[j]}\n")
                j += 1
    else:
        print("User not found")  
