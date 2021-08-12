from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import pyautogui


# To be printed dollar
dollar = "$" * 99

# User Inputs

print('\n', dollar)

print('')
print('Welcome to Coding Quotient, lazy people!! ^_^')
print(">>If you've reached here I'm assuming you've read the README.md and have the settings configured")
print(">>Please check all the configurations before proceeding as it may cause this program to crash otherwise")
print("Made With ♥ By RITISH KHANNA")
print("Follow Me on Github ----> https://github.com/RitishKhanna")

print('\n', dollar)

username = input('Coding Quotient Email: ')
password = getpass.getpass(prompt='Coding Quotient Password:')




# Importing Chrome Driver

driver_path = "./chromedriver.exe"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Where the Magic happens function


time.sleep(2)
driver.get("https://codequotient.com/login")
time.sleep(2)
driver.find_element_by_id("email").send_keys(username)
time.sleep(2)
driver.find_element_by_id("password").send_keys(password)
time.sleep(2)
driver.find_element_by_id("btnSubmit").click()
time.sleep(2)


##################### Module-1 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6064494e5ba633d51d490209")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("create table students(rollNo int,studentName varchar(50),branch varchar(10),semester int);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606452b65ba633d51d490210")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("alter table student add gender  varchar(1);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606458055ba633d51d49021d")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""alter table students rename column phone to contact;
alter table students modify stud_name varchar(30);
alter table students drop column marks;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60645a755ba633d51d49022a")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("alter table student rename to student_data;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60645c305ba633d51d490231")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("drop table student;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606534215d680d3edcdff153")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("truncate table student;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

##################### Module-2 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60652ec45d680d3edcdff14f")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""insert into student values(106,'Ajay','CSE',4);
insert into student values(107,'Atul','ECE',6);
insert into student(rollNo,studentName,semester) values(108,'Yuvraj',6);
insert into student(rollNo,studentName,semester) values(109,'Vaibhav',4);
insert into student(rollNo,studentName,branch) values(110,'Utkarsh','CSE');
insert into student(rollNo,studentName,branch) values(111,'Rohit','Civil');""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60656d6a5d680d3edcdff177")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""update student set studentName='Sumit Sharma' where rollNo='654';
update student set semester=4 where semester is null;
update student set branch='Civil' where rollNo='655';""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60652ece5d680d3edcdff150")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""delete from student where semester=2 and branch='ECE';
delete from student WHERE branch is null;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60652ed85d680d3edcdff151")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select studentName from student;
select semester,studentName,rollNo from student;
select * from student;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606585405d680d3edcdff18c")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select rollNo from student where branch is null;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60681d9d5d680d3edcdff608")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select roll_no as " + '"id"' + "," "fname as" + '"name"' + "from students;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 7
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60658d2c5d680d3edcdff1cd")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select marks from student where studentName='Hardik';
select rollNo from student where studentName !='Kanav';
select rollNo,StudentName from student where branch='CSE';
select studentName from student where rollNo>653;
select branch from student where rollNo>654;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 8
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60652ee05d680d3edcdff152")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select * from student where marks/2>40;
select studentName as "studname", marks+10 as "inc_marks" from student;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 9
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606599fb5d680d3edcdff1de")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select rollNo, studentName from student where semester=4 and marks>75;
select rollNo, studentName from student where branch='ECE' or semester=6;
select rollNo from student where branch='CSE' or marks<40;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 10
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60659a045d680d3edcdff1df")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select rollNo from student where marks between 55 and 65;
select studentName from student where branch in ('CSE','ME');
select rollNo,marks from student where branch not in ('IT','ECE','ME');""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 11
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60659a145d680d3edcdff1e0")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select rollNo,studentName from student where studentName like '_a%';")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

##################### Module-3 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606692af5d680d3edcdff215")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""create table students(id int,name varchar(50), age int, constraint age check(age>15));
alter table dept add constraint dept_id check (dept_id>100);""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60669aba5d680d3edcdff21b")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""create table students(id int,name varchar(50),age int, branch varchar(10) default 'CSE');
alter table dept modify dept_name default 'ECE';""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066a95a5d680d3edcdff225")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE TABLE students(id int primary key, name varchar(50),age int);
ALTER TABLE DEPT ADD primary key(dept_id);""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066afc35d680d3edcdff229")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""create table students(id int,name varchar(50) not null,age int);
alter table dept modify dept_name not null;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066b46b5d680d3edcdff22c")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""create table students(id int,name varchar(50) unique,age int);
alter table dept add unique(dept_name);
""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066c6f25d680d3edcdff238")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""create table dept(dept_id int primary key, dept_name varchar(50));
create table students(roll_no int,student_name varchar(50),age int,dept_id int, foreign key(dept_id) references dept(dept_id));""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

##################### Module-4 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6067f7d25d680d3edcdff43d")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select stud_dept as" + '"dept"' + "," + "count(roll_no) as" + '"cnt"' + "from students group by stud_dept;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6067f7d85d680d3edcdff43e")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select stud_dept as" + '"dept"' + "," + "count(roll_no) as" + '"cnt"' + "from students group by stud_dept having stud_dept in ('CSE','Mechanical');")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6067f7de5d680d3edcdff43f")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select * from students order by stud_name asc;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6067fe955d680d3edcdff4c9")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select max(stud_marks) as" + '"highest"' + "," + "min(stud_marks) as" + '"lowest"' "from students;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606800d85d680d3edcdff4f9")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select count(*) as" + '"count"' + "from students where stud_marks>50;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606800dd5d680d3edcdff4fa")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select sum(stud_marks) as "sum" from students where stud_dept='ECE';
select avg(stud_marks) as "average" from students where stud_marks>70;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 7
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6068045c5d680d3edcdff531")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select upper(stud_fname) as "upper" from students;
select lower(stud_lname) as "lower" from students;
select length(stud_full_name) as "length" from students;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 8
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60680cc65d680d3edcdff596")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select round(CGPA,2) as "Rounded" from students;
select trunc(CGPA,1) as "Truncated" from students;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 9
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606806ce5d680d3edcdff590")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select fname || ' ' || lname as "FullName" from students;
select replace(fname,'a','i') as "UpdatedFirstName" from students;
select substr(fname,1,5) as "Initials" from students;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 10
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606806d55d680d3edcdff591")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select abs(months_between(birthdate,to_date('03/04/2021','DD/MM/YYYY'))) as "Difference" from students;
select next_day(birthdate,'thursday') as "NextThursday" from students;
select add_months(birthdate,10) as "AddedMonths" from students;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

##################### Module-5 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066cd145d680d3edcdff240")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select roll_no, stud_name,marks from students cross join stud_marks;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066d32c5d680d3edcdff246")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select * from students inner join stud_marks on students.roll_no=stud_marks.stud_roll where marks between 30 and 75; ")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066dc7a5d680d3edcdff24d")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select roll_no,stud_name,marks from students left join stud_marks on students.roll_no=stud_marks.stud_roll; ")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066dc8c5d680d3edcdff24e")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select roll_no,stud_name,marks from students right join stud_marks on students.roll_no=stud_marks.stud_roll;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066e09b5d680d3edcdff2f6")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select roll_no,stud_name,marks from students full outer join stud_marks on students.roll_no=stud_marks.stud_roll;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6066dc9a5d680d3edcdff24f")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select * from students natural join stud_marks where marks>=35;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

##################### Module-6 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60671b0c484d133ebe6c602e")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select empno from emp where sal=(select max(sal) from emp where deptno=(select deptno from dept where dname='ACCOUNTING'));
select avg(sal) from emp where deptno=(select deptno from dept where dname='SALES');""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60672b3d484d133ebe6c6034")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select empno as "empid", ename as "empname" from emp where mgr=(select empno from emp where ename='KING');
select empno as "empid", ename as "empname" from emp where JOB='ANALYST' and sal=(select max(sal) from emp where job='ANALYST');""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60673042484d133ebe6c603b")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select empno as "empid", ename as "empname" from emp where sal>(select avg(sal) from emp);
select empno as "empid", ename as "empname",hiredate as "joining" from emp where deptno=(select deptno from dept where loc='DALLAS');""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6067dd085d680d3edcdff392")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""select empno as "empid" from emp emp1 where sal=(select max(sal) from emp where deptno=emp1.deptno);
select empno as "empid" ,ename as "ename" from emp emp1 where exists (select empno from emp where mgr=emp1.empno);""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/6067dd125d680d3edcdff393")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("select empno as" + '"empid"' + "from emp emp1 where sal>(select avg(sal) from emp where deptno=emp1.deptno);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

#################### Module-7 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606be29f5d680d3edcdff778")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE INDEX stud_single_idx ON students (rollNo);
CREATE INDEX stud_comp_idx ON students (fname, lname);
CREATE UNIQUE INDEX stud_uniq_idx ON students (email_id);
CREATE INDEX stud_func_idx ON students (TRUNC(email_id,2));""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606bf2af5d680d3edcdff7b4")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("ALTER INDEX stud_idx RENAME TO student_index;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606bf7f05d680d3edcdff7b7")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("DROP INDEX stud_idx; ")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

#################### Module-8 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606bfc3a5d680d3edcdff7bb")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE SEQUENCE stud_seq
START WITH 1000
INCREMENT BY 2
MINVALUE 10
MAXVALUE 5000
CYCLE;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606c06e75d680d3edcdff7cc")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""ALTER SEQUENCE stud_seq
INCREMENT BY 10
MAXVALUE 10000
NOCYCLE;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606fde29e410107cfa50e0a7")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE CLUSTER stud_dept_cluster (dept_no INT);
CREATE INDEX cluster_index ON CLUSTER stud_dept_cluster;
CREATE TABLE students (rollNo INT, sname VARCHAR2(20), deptno INT) CLUSTER stud_dept_cluster(deptno);
CREATE TABLE dept (deptno INT, dname VARCHAR(20), d_head VARCHAR2(50)) CLUSTER stud_dept_cluster(deptno);""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

##################### Module-9 ######################

# 1
f = open("Unattempted Questions DBMS.txt", "w")
(f.write("https://codequotient.com/attempt/attempttutorial/60d9a3de72f3f3f870e276e3/606c18da5d680d3edcdff818"  + "\n"))

# 2
f = open("Unattempted Questions DBMS.txt", "a")
(f.write("https://codequotient.com/attempt/attempttutorial/60d9a3de72f3f3f870e276e3/606c1f715d680d3edcdff8c0"  + "\n"))

##################### Module-10 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606c34ae5d680d3edcdffa17")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE OR REPLACE VIEW student_view AS SELECT roll_no AS "ID", marks FROM students WHERE marks > 75;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606c3cf35d680d3edcdffa1a")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE OR REPLACE VIEW student_view AS SELECT roll_no AS "ID",stud_name AS "name", marks FROM
students WHERE marks>50;""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606c3f5f5d680d3edcdffa1f")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("RENAME stud_view TO student_view;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606c40065d680d3edcdffa28")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("DROP VIEW student_view;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

#################### Module-11 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606c47d55d680d3edcdffb26")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
l number:=20;
b number:=10;
area number;
perimeter number;
BEGIN
area:=l*b;
perimeter:=2*(l+b);
dbms_output.put_line(area);
dbms_output.put_line(perimeter);
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606d33db143dd77d2259449e")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
stud_row_type students%rowtype;
BEGIN
SELECT * INTO stud_row_type FROM students WHERE roll_no='4';
DBMS_output.put_line(stud_row_type.fname||' '||stud_row_type.CGPA);
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606d3dd9143dd77d225944a3")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
studRoll student.rollNo%type;
studName student.studentName%type;
studBranch student.branch%type;
studSem student.semester%type;
BEGIN
INSERT INTO student(rollNo, studentName, branch, semester) VALUES(345, 'Ayush', 'CSE',6);
INSERT INTO student(rollNo, studentName, branch) VALUES(167, 'Gopal', 'ECE');
INSERT INTO student(rollNo, studentName, semester) VALUES(370, 'Pranav', 8);
UPDATE student SET studentName='Aman' WHERE rollNo=124;
DELETE student WHERE rollNo='109';
DELETE student WHERE rollNo='655';
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606d5204143dd77d225944ab")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
marks student.marks %type;
CURSOR stud_cursor IS select rollNo,marks from student;
roll_no student.rollNo %type; 
grade varchar(20);
BEGIN
OPEN stud_cursor;
LOOP
FETCH stud_cursor into roll_no, marks;
EXIT WHEN stud_cursor%notfound;
/* Use control statements to store the grade in the variable `grade` according to `marks` */
/* Do not change the given code */
/* Write the code from this line */
IF (marks>=90) AND (marks<=100) THEN
grade:='O';
ELSIF (marks>=80) AND (marks<=89) THEN
grade:='A+';
ELSIF (marks>=70) AND (marks<=79) THEN
grade:='A';
ELSIF (marks>=60) AND (marks<=69) THEN
grade:='B+';
ELSIF (marks>=50) AND (marks<=59) THEN
grade:='B';
ELSIF (marks>=40) AND (marks<=49) THEN
grade:='C';
ELSIF (marks>=33) AND (marks<=39) THEN
grade:='P';
ELSE
grade:='F';
END IF;
dbms_output.put_line(roll_no||' '||grade);
END LOOP;
CLOSE stud_cursor;
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606d6cc7143dd77d225944b1")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
i number:=1;
BEGIN
FOR i IN 1..200 LOOP
IF MOD(i, 2)=0 THEN
dbms_output.put_line(i);
END IF;
END LOOP;
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606d73de143dd77d225944b6")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
a number := 0;
BEGIN
<<adder>>
a:=a+1;
dbms_output.put_line(a);
IF a<50 THEN
goto adder;
END IF;
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

#################### Module-12 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606d8e1e143dd77d225944b9")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
dividend number;
divisor number;
quotient number;
CURSOR to_divide_cursor IS select dividend,divisor from to_divide;
BEGIN
OPEN to_divide_cursor;
LOOP
FETCH to_divide_cursor INTO dividend,divisor;
quotient:=dividend/divisor;
dbms_output.put_line(quotient);
EXIT WHEN to_divide_cursor%notfound;
END LOOP;
/* DO NOT change the code */
/* Add the exception handling block and complete the code */
EXCEPTION
WHEN ZERO_DIVIDE THEN
dbms_output.put_line(SQLCODE||' '||SQLERRM);
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606da014143dd77d22594559")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
zero_exception EXCEPTION;
dividend NUMBER := 50;
divisor NUMBER :=0;
PRAGMA EXCEPTION_INIT(zero_exception,-20001);
BEGIN
IF divisor=0 THEN
RAISE_APPLICATION_ERROR(-20001, 'Division by zero');
END IF;
EXCEPTION
WHEN zero_exception THEN
DBMS_OUTPUT.PUT_LINE(SQLERRM);
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

##################### Module-13 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606e7bef143dd77d225947c1")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE OR REPLACE TRIGGER student_tirgger BEFORE INSERT OR UPDATE ON students
BEGIN
NULL;
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606e8482143dd77d225947c6")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE OR REPLACE TRIGGER stud_trigger BEFORE INSERT ON students FOR EACH ROW
DECLARE
stud_excep EXCEPTION;
PRAGMA EXCEPTION_INIT(stud_excep,-20001);
BEGIN
IF :NEW.roll_no<0 THEN
RAISE_APPLICATION_ERROR(-20001,'Roll Number can not be negative');
ELSE
DBMS_output.put_line('Data Inserted');
END IF;
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606e8488143dd77d225947c7")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE OR REPLACE TRIGGER stud_update
AFTER UPDATE
ON students
FOR EACH ROW
BEGIN INSERT INTO stud_logs VALUES(:OLD.roll_no,'updated');
END;
/
CREATE OR REPLACE TRIGGER stud_delete
AFTER DELETE
ON students
FOR EACH ROW
BEGIN INSERT INTO stud_logs VALUES(:OLD.roll_no,'deleted');
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60701134e410107cfa50e0c2")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("ALTER TRIGGER stud_trigger DISABLE;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/606e848d143dd77d225947c8")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("DROP TRIGGER stud_trigger;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

#################### Module-14 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60dbef8eccde02f82059632a")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
affected_rows number;
BEGIN
DELETE FROM emp WHERE sal < 1500;
IF SQL%NOTFOUND THEN
DBMS_output.put_line('No Row To Delete');
ELSIF SQL%FOUND THEN
affected_rows:=SQL%ROWCOUNT;
dbms_output.put_line(affected_rows);
END IF;
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60dc0540ccde02f820596372")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""DECLARE
CURSOR c is select sal from emp where deptno=20;
salsum emp.sal %type;
BEGIN
salsum:=0;
for i in c LOOP
salsum := salsum+i.sal;
END LOOP;
dbms_output.put_line(salsum);
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

################### Module-15 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60dc10eaccde02f820596387")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE OR REPLACE PROCEDURE update_stud(rollNo IN INT, marks IN INT)
IS
BEGIN
UPDATE students set marks = marks where roll_no = rollNo;
END;
/
CREATE OR REPLACE PROCEDURE insert_stud(stud_roll IN INT, studName IN VARCHAR2, stud_marks IN INT)
IS
BEGIN
INSERT INTO students VALUES(stud_roll,studName,stud_marks);
END;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60d9a3de72f3f3f870e276e3/60dc0ac7ccde02f82059637a")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""CREATE OR REPLACE FUNCTION getMaximum(x IN number, y IN number, z IN number)
RETURN number
IS
maxnum number;
BEGIN
IF x > y AND x > z THEN
maxnum:=x;
ELSIF y > x AND y > z THEN 
maxnum:=y;
ELSE
maxnum:=z;
END IF;
RETURN maxnum;
END;
/
CREATE OR REPLACE FUNCTION getSquare(x1 in number)
RETURN number
IS
BEGIN
RETURN (x1*x1);
end;
/""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
f = open("Unattempted Questions DBMS.txt", "a")
(f.write("https://codequotient.com/attempt/attempttutorial/60d9a3de72f3f3f870e276e3/60dc342fccde02f820596396"  + "\n"))
f.close()






time.sleep(120)
driver.quit()