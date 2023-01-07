import mysql.connector
import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harish#4",
  database="FACE_DATA"
)

current_time=datetime.datetime.now()
mycursor = mydb.cursor(buffered=True)
# notOver=True
# while notOver:
#     name=input("Enter Name:")
#     if name=="EXIT":
#         notover=False
#         break
#     Roll_number=input('Enter Roll Number:')
#     mycursor.execute("INSERT INTO attendance_sheet(name,roll) VALUES('{}','{}')".format(name,Roll_number))
#     mydb.commit()


# mycursor.execute("SHOW TABLES")

# notExit=True
# while notExit:
#     name=input("Enter Name:")
#     if name=="EXIT":
#         notExit=False
#         break
#     value=input("Enter Value:")
#     mycursor.execute("INSERT INTO attendance_sheet(name,roll) VALUES('{}','{}')".format(name,value))

mydb.commit()
# for i in range(1,31):
#     cmd=f'''ALTER TABLE attendance_sheet
#     ADD `{i}/01` varchar(255);'''
#     print(cmd)
#     mycursor.execute(cmd)
#     mydb.commit()
mycursor.execute(f"SELECT '{current_time.day}/01' FROM face_data")
data=mycursor.fetchall()
attendance=[]
for i in data:

    a=str(i)
    b=a.lstrip("('")
    c=b.rstrip("',)")
    attendance.append(c)
print(attendance)



def mark_attendance(roll):
  roll_list=['121FP0426']
  if roll in roll_list:
    if attendance[roll_list.index(roll)]!='P':
      mycursor.execute(f"UPDATE attendance_sheet SET `{current_time.day}/01` = 'P' WHERE roll='{roll}' ")
      mydb.commit()
    else:
      pass
mark_attendance('121FP0426')
print(current_time.day)
print("Program Done Running")
