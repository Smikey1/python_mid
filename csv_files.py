"""------------>  Working with CSV Files <----------------
-------------------------------------------------------
"""

# ---------> FOR READING CSV FILE   <-----------

from csv import DictReader

#ordered dict
with open("new_file.csv","r") as rf:
    csv_reader = DictReader(rf,delimiter=",")
    for row in csv_reader:
        print(row["name"])  # order dict


# ---------> FOR WRITING CSV FILE   <-----------
from csv import DictWriter
# newline="" --> to remove space
with open("file2.csv","w",newline="") as wf:
    csv_writer = DictWriter(wf,fieldnames=["name","contact","address","dob"])
    csv_writer.writeheader()
    csv_writer.writerow(
        {"name":"Ram","contact":98564,"address":"ktm","dob":"7 Sept"}
        )
    csv_writer.writerow(
        {"name":"Kiran","contact":12345,"address":"btl","dob":"8 Aug"}
        )
    
    csv_writer.writerows([
        {"name":"dkasdk","contact":12345,"address":"btl","dob":"8 Aug"},
        {"name":"sdansran","contact":12345,"address":"btl","dob":"8 Aug"}
        ])

