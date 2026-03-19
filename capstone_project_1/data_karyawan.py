import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tabulate import tabulate
import numpy as np
from scipy import stats


db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Barat1001",
    database="company_hr"
)
cursor = db.cursor()


def menampilkan_seluruh_data_karyawan():
    
    while True:
        inputan_ID= int(input("masukkan ID Karyawan: "))
        query = """
        SELECT *
        FROM employees e
        JOIN performance p
        WHERE e.employee_id = p.employee_id AND e.employee_id = %s
        """
        cursor.execute(query,(inputan_ID,))
        result = cursor.fetchone()

        cursor.execute("SELECT * FROM performance LIMIT 1")

        columns = [col[0] for col in cursor.description]

        print(columns)
        if result is not None:
            for i in range(len(columns)): 
                print(f"{columns[i]} : {result[i]}")
        else:
            print("Data karyawan dengan ID tersebut tidak ditemukan.")
            
       
            # print(F"""ID: {result[0]}, Nama: {result[1]}, Jenis Kelamin: {result[2]}, Tanggal Lahir: {result[3]}, Tanggal Masuk: {result[4]}, Jabatan: {result[5]}, Gaji: {result[6]}  Performance Score: {result[8]}, Attendance Rate: {result[9]}%, Late Count: {result[10]}, Leave Days: {result[11]}""")
        # else:
        #     print("Data karyawan dengan ID tersebut tidak ditemukan.")
        #     continue
        while True: 
            inputYN = input("Apakah Anda ingin mencari data karyawan lain? (y/n): ").lower() 
            if inputYN not in ['y','n']:
                print("Input tidak valid. Silakan masukkan 'y' untuk melihat data lain atau 'n' untuk keluar.")
            else: 
                break 
        if inputYN == 'n':
            break


def input_data_karyawan():
    employee_id = int(input("Masukkan ID Karyawan: "))
    name = input("Masukkan Nama Karyawan: ")
    gender = input("Masukkan Jenis Kelamin Karyawan (male/female): ")
    birth_date = input("Masukkan Tanggal Lahir Karyawan (YYYY-MM-DD): ")
    hire_date = input("Masukkan Tanggal Masuk Karyawan (YYYY-MM-DD): ")
    job_title = input("Masukkan Jabatan Karyawan: ")
    salary = int(input("Masukkan Gaji Karyawan: "))

    query = """
    INSERT INTO employees 
    (employee_id, name, gender, birth_date, hire_date, job_title, salary)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    values = (employee_id, name, gender, birth_date, hire_date, job_title, salary)
    cursor.execute(query, values)
    db.commit()

    print(f"Data karyawan berhasil ditambahkan. ID: {employee_id}, Nama: {name}, Jenis Kelamin: {gender}", f"Tanggal Lahir: {birth_date}, Tanggal Masuk: {hire_date}, Jabatan: {job_title}, Gaji: {salary}")


def input_data_performance():
    employee_id = int(input("Employee ID: "))
    kpi_score = float(input("Performance Score (0-5): "))
    attendance_rate = float(input("Attendance Rate (%): "))
    late_count = int(input("Late Count: "))
    leave_days = int(input("Leave Days: "))

    query = """
    INSERT INTO performance
    (employee_id, kpi_score, attendance_rate, late_count, leave_days)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (employee_id, kpi_score, attendance_rate, late_count, leave_days)
    cursor.execute(query, values)
    db.commit()

    print(f"""Data performance berhasil ditambahkan!
    Employee ID: {employee_id}, Performance Score: {kpi_score}, Attendance Rate: {attendance_rate}%, Late Count: {late_count}, Leave Days: {leave_days}""")

def input_data (): 
    print("=== Input Data Karyawan dan atau DataPerformance ===")
    while True:
        inputan = print("""
        1. masukkan data karyawan 
        2. masukkan data performance
        3. Exit
        """)
        inputan = input("Pilih menu: ")
        if inputan  in ['1', '2', '3']:
            if inputan == '1':
                input_data_karyawan()
            elif inputan == '2':
                input_data_performance()
            else:
                break
        else: 
            print("Input tidak valid. Silakan masukkan '1' untuk data karyawan, '2' untuk data performance, atau '3' untuk keluar.")


def top_karyawan ():
    query= """
    SELECT e.employee_id,
    e.name,
    e.job_title,
    e.salary,
    ROUND(
    (attendance_rate/20*0.4) +
    (GREATEST(0, 5 - (late_count * 0.5)) * 0.3) +
    (kpi_score_score * 0.3),
    2
    ) AS performance_score
    FROM employees e
    JOIN performance p
    ON e.employee_id = p.employee_id
    ORDER BY performance_score DESC
    LIMIT 10
    """
    cursor.execute(query)
    result = cursor.fetchall()
    headers = ["Employee ID", "Name", "Job Title", "Salary", "Performance Score"]

    print("\n=== TOP PERFORMER ===")
    print(tabulate(result, headers=headers, tablefmt="grid"))

def low_karyawan ():
    query= """
    SELECT e.employee_id,
    e.name,
    e.job_title,
    e.salary,
    ROUND(
    (attendance_rate/20*0.4) +
    (GREATEST(0, 5 - (late_count * 0.5)) * 0.3) +
    (kpi_score_score * 0.3),
    2
    ) AS performance_score
    FROM employees e
    JOIN performance p
    ON e.employee_id = p.employee_id
    ORDER BY performance_score ASC
    LIMIT 10
    """
    cursor.execute(query)
    result = cursor.fetchall()
    headers = ["Employee ID", "Name", "Job Title", "Salary", "Performance Score"]

    print("\n=== LOW PERFORMER ===")
    print(tabulate(result, headers=headers, tablefmt="grid"))
  

def top_and_low_karyawan():
    while True:
        inputan_TL = input("Apakah Anda ingin melihat top karyawan (t) atau low karyawan (l)? (t/l): ").lower() 
        if inputan_TL in ['t', 'l']:
            if inputan_TL == 't':
                top_karyawan()
                break
            elif inputan_TL == 'l':
                low_karyawan()
                break
        else: 
            print("Input tidak valid. Silakan masukkan 't' untuk top atau 'l' untuk low.")


def visualisasi_rata_rata_gaji(cursor):
    query = """
    SELECT 
    e.employee_id,
    e.name,
    e.job_title,
    e.salary,
    p.kpi_score,
    p.attendance_rate
    FROM employees e
    JOIN performance p
    ON e.employee_id = p.employee_id
    """
    df = pd.read_sql(query, db)

    avg_salary = df.groupby('job_title')['salary'].mean().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    avg_salary.plot(kind='bar')
    plt.title("Top 10 Average Salary per Job Title")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualisasi_performance_score (cursor):
    query = """
    SELECT 
    ROUND(
    (attendance_rate/20*0.4) +
    (GREATEST(0, 5 - (late_count * 0.5)) * 0.3) +
    (kpi_score * 0.3),
    2
    ) AS performance_score

    FROM performance;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    scores = [row[0] for row in result]

    high = sum(1 for s in scores if s >= 4.5)
    medium = sum(1 for s in scores if 3.5 <= s < 4.5)
    low = sum(1 for s in scores if s < 3.5)

    labels = ['High', 'Medium', 'Low']
    sizes = [high, medium, low]

    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Distribusi Performance Karyawan")
    plt.show()

def visualisasi_data_karyawan(cursor):
    while True:
        inputan_YN = input("Apakah Anda ingin melihat visualisasi rata-rata gaji (a) atau attendance vs performance (b)? (a/b): ").lower() 
        if inputan_YN in ['a', 'b']:
            if inputan_YN == 'a':
                visualisasi_rata_rata_gaji(cursor)
                break
            elif inputan_YN == 'b':
                visualisasi_performance_score(cursor)
                break
        else: 
            print("Input tidak valid. Silakan masukkan 'a' untuk rata-rata gaji atau 'b' untuk attendance vs performance.")

def show_descriptive_statistics(cursor):
    while True:
        column= input("""
            Masukkan kolom yang ingin dianalisis :
            1. kpi_score
            2. attendance_rate
            3. late_count
            4. leave_days
            : """)
        list_column = ['kpi_score', 'attendance_rate', 'late_count', 'leave_days']
        if column not in ['1', '2', '3', '4']:
            print("Input tidak valid. Silakan masukkan nomor kolom yang benar.")
            continue
        else : 
            break

    column_int= int(column) - 1
    query = """
    SELECT 
    """ + list_column[column_int] + """
    FROM performance
    """
    cursor.execute(query)
    result = cursor.fetchall()
    scores = [float(row[0]) for row in result if row[0] is not None]

    values, counts = np.unique(scores, return_counts=True)
    mode_value = values[counts.argmax()]


    print("\n=== DESCRIPTIVE STATISTICS ===")
    print("\n=== DESCRIPTIVE STATISTICS ===")
    print(f"Mean: {stats.tmean(scores):.2f}")
    print(f"Median: {np.median(scores):.2f}")
    print(f"Min: {min(scores)}")
    print(f"Max: {max(scores)}")
    print(f"Standard Deviation: {stats.tstd(scores):.2f}")


while True:

    print("\n=== HR SYSTEM ===")
    print("1. Lihat Data karyawan")
    print("2. input data karyawan dan performance")
    print("3. melihat top dan low karyawan berdasarkan performance score")
    print("4. visualisasi data karyawan")
    print("5. Descriptive Statistics")
    print("6. Exit")

    menu = input("Pilih menu: ")

    if menu == "1":
        menampilkan_seluruh_data_karyawan()
    elif menu == "2":
        input_data()
    elif menu == "3":
        top_and_low_karyawan()
    elif menu == "4":
        visualisasi_data_karyawan(cursor)
    elif menu == "5":
        show_descriptive_statistics(cursor)
    elif menu == "6":
        break