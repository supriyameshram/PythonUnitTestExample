import csv
 
with open('C:\\Users\supriya_meshram\PycharmProjects\Guru99-pytest\\registration_csv.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)


  
    