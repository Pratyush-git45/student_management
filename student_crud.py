import psycopg2 
DB_NAME ="postgres"
DB_USER ="postgres.prijvfrvdfxxirkzhvpf"
DB_PASSWORD="Pratyush_1"
DB_HOST="aws-0-ap-south-1.pooler.supabase.com"
DB_PORT= "5432"
def db_connection(): #connection establishment
    try: 
        conn= psycopg2.connect(dbname= DB_NAME, user= DB_USER, password= DB_PASSWORD, host= DB_HOST, port= DB_PORT)
        return conn
    except Exception as e:
        print("error connecting to database")
        return None
    


# teachers table---------------------------

def create_tables(): #create table
    conn= db_connection()
    cursor= conn.cursor()
    #multiline
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher( 
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
    """)  
    conn.commit()
    cursor.close()
    conn.close()
    print("table created")
    

def insert_teacher(name,age): #insert data in teacher table
    conn= db_connection()
    cursor= conn.cursor()
    cursor.execute("INSERT INTO teacher (name, age) VALUES(%s,%s) RETURNING id",(name,age))
    conn.commit()
    cursor.close()
    conn.close()
    print("data inserted")

def update_teacher(name,age): #update data
    conn= db_connection()
    cursor= conn.cursor()
    cursor.execute("UPDATE teacher SET name= %s WHERE age=%s",(name,age))
    conn.commit()
    cursor.close()
    conn.close()
    print("data updated")

def delete_teacher(age): #delete data
    conn= db_connection()
    cursor= conn.cursor()
    cursor.execute("DELETE FROM teacher WHERE age=%s",(age,))
    conn.commit()
    cursor.close()
    conn.close()
    print("data deleted")

def modify_teacher(): #modify table to add column
    conn= db_connection()
    cursor= conn.cursor()
    cursor.execute("ALTER TABLE teacher ADD department_id INT REFERENCES departments(department_id) on delete cascade")
    conn.commit()
    cursor.close()
    conn.close()
    print("column added")

def modify_course(): #modify table to add column
    conn= db_connection()
    cursor= conn.cursor()
    cursor.execute("ALTER TABLE students ADD course_id INT REFERENCES courses(course_id) on delete cascade")
    conn.commit()
    cursor.close()
    conn.close()
    print("column added")



def insert_departments(departments):#insert data in department table
    conn= db_connection()
    cursor= conn.cursor()
    cursor.executemany("INSERT INTO departments (department_id, department_name) VALUES(%s,%s)", departments)
    conn.commit()
    cursor.close()
    conn.close()
    print("data inserted")

def department_name():
    return [
        (101, "English"),
        (102, "Nepali"),
        (103, "Spanish")
    ]

def insert_course(courses):#insert data in course table
    conn= db_connection()
    cursor= conn.cursor()
    cursor.executemany("INSERT INTO courses (course_id, course_name, credits, department_id) VALUES(%s,%s,%s,%s)", courses)
    conn.commit()
    cursor.close()
    conn.close()
    print("data inserted")

def course_name():
    return [
        (201, "English-literature",4,101),
        (202, "Nepali-literature",4,102),
        (203, "Spanish-literature",4,103)
    ]


def insert_students(students): #insert data into students
    conn=db_connection()
    cursor= conn.cursor()
    cursor.executemany("INSERT INTO students (student_id, first_name, last_name, email, enrollment_date, course_id) VALUES(%s, %s, %s, %s, %s, %s)", students)
    conn.commit()
    cursor.close()
    conn.close()
    print("data inserted")

def student_name():
    return [
        (1,'John', 'Doe', 'john.doe@example.com','2025-3-1',201),
        (2,'Jane', 'Smith', 'jane.smith@example.com','2025-3-3',202),
        (3,'Emily', 'Johnson', 'emily.johnson@example.com', '2025-3-5',203)
    ]

def truncate_teacher(): #drop table 
    conn=db_connection()
    cursor= conn.cursor()
    cursor.execute("drop TABLE teacher")
    conn.commit()
    cursor.close()
    conn.close()
    print("teachers table truncated")





if __name__=="__main__": #executes the function
    #db_connection()
    #create_tables()
    #insert_teacher("hari", 30)
    #update_teacher("rita", 20)
    #delete_teacher(30)
    #modify_teacher()
    #modify_course()

    # students= student_name()
    # insert_students(students)

    #truncate_teacher()

    
    