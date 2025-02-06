import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
cursor.execute('''
create table if not exists student(id integer primary key, name text not null,
age text not null)

''')
def list_student():
    cursor.execute("select *from student")
    for row in cursor.fetchall():
        print(row)
def add_student(name, age):
    cursor.execute("insert into student(name,age)values(?,?)",(name,age))
    conn.commit()
def update_student(id, name, age):
    cursor.execute("update student set name= ?, age=? where id = ?",(name, age, id))
    conn.commit()
def delete_student(id):
    cursor.execute("delete from student where id = ?",(id,))
    conn.commit()

def main():
    while True:
        print("Student Management system")
        print("1. List of Student")
        print("2. Add student ")
        print("3. update student")
        print("4. delete student record")
        print("5. exit from record")
        choice=input("Enter your choice")
        if choice=="1":
            list_student()
        elif choice=="2":
            name = input("Enter student Name:")
            age = input("Enter student age")
            add_student(name, age)
        elif choice=="3":
            id  =input("Enter your student id:")
            name = input("Enter student Name:")
            age = input("Enter student age")
            update_student(id, name, age)
        elif choice=="4":
            id  =input("Enter your student id for delete:")
            delete_student(id)
        elif choice=="5":
            break
        else:
            print("Enter right choice")
    conn.close()
            
if __name__ =="__main__":
    main()

