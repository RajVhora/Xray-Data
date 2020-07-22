import os
from datetime import date
import csv

data = []

PATH = "patients/"
for patientfolder in os.listdir(PATH):
    trow = []
    patientdata = patientfolder.split('_')
    if len(patientdata) == 2:
        trow.append(patientdata[0])
        trow.append(" ")
        trow.append(patientdata[1])
    elif len(patientdata) == 3:
        trow.append(patientdata[0])
        trow.append(patientdata[1])
        trow.append(patientdata[2])
    else:
        trow.append(patientfolder)
        trow.append(" ")
        trow.append(' ')

    path_patient = os.path.join(PATH,patientfolder)
    for files in os.listdir(path_patient):
        if files.endswith(".jpg"):
            temp = files.split('_')
            temp = temp[1]
            Month = temp[0:2]
            Day = temp[2:4]
            Year = temp[4:8]
            date_info = str(date(int(Year),int(Month),int(Day)))
            trow.append(date_info)
            data.append(trow.copy())
            del trow[-1]

data = sorted(data,key= lambda row:row[3],reverse = True)

with open("XrayData.csv","w+",newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerow(['Name','SSNUM','INUM','Date'])
    csvWriter.writerows(data)
