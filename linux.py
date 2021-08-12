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
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60c8b0030b1bf52076e075ac")
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9c62672f3f3f870e278c4")#link
driver.find_element_by_id("chkOpt5").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9e95a72f3f3f870e279f9")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc7313cfaf5f6628f2d3dd")
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9db6872f3f3f870e279f0")#link
driver.find_element_by_id("chkOpt6").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9e07a72f3f3f870e279f1")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 7
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9e25672f3f3f870e279f2")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 8
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc7726cfaf5f6628f2d3e4")
time.sleep(2)

# 9
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9e37972f3f3f870e279f3")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

###################### Module-2 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d54dd44774a790905fa2f1")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(3)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d560694774a790905fa2f3")#link
driver.find_element_by_id("txtOutput0").send_keys("info ls")
driver.find_element_by_id("txtOutput1").send_keys("info cat")
driver.find_element_by_id("txtOutput2").send_keys("info man")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d5710a4774a790905fa2f8")#link
driver.find_element_by_id("txtOutput0").send_keys("root")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d566734774a790905fa2f7")#link
driver.find_element_by_id("chkOpt4").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(3)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d5771f4774a790905fa2fc")#link
driver.find_element_by_id("txtOutput0").send_keys("Linux")
driver.find_element_by_id("txtOutput1").send_keys("5.4.0-70-generic")
driver.find_element_by_id("txtOutput2").send_keys("x86_64")
driver.find_element_by_id("txtOutput3").send_keys("GNU/Linux")
driver.find_element_by_id("txtOutput4").send_keys("0")
driver.find_element_by_id("txtOutput5").send_keys("0")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d57b7e4774a790905fa303")#link
driver.find_element_by_id("txtOutput0").send_keys("cal 2022")
driver.find_element_by_id("txtOutput1").send_keys("cal 09 2016")
driver.find_element_by_id("txtOutput2").send_keys("cal -3")
driver.find_element_by_id("txtOutput3").send_keys("date +%Y")
driver.find_element_by_id("txtOutput4").send_keys("date +%u")
driver.find_element_by_id("txtOutput5").send_keys("date +%s")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 7
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60dc421eccde02f8205963a3")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(3)

# 8
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60dc4733ccde02f8205963a4")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "rm -r students")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 9
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60dc3934ccde02f82059639f")#link
driver.find_element_by_id("txtOutput0").send_keys("help cd")
driver.find_element_by_id("txtOutput1").send_keys("uptime")
driver.find_element_by_id("txtOutput2").send_keys("tty")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 10
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc7afacfaf5f6628f2d3f3")
time.sleep(2)

# 11
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d595b24774a790905fa319")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "mkdir -p students/{John,Tom}" + "\n" + "rm -r marks")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 12
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60ccab42cfaf5f6628f2d440")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "mkdir -p d1/{dd1,dd2}")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 13
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60c8b25a0b1bf52076e075b1")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "touch f1 f2")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 14
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d5b7a64774a790905fa320")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "touch studentNames.txt" + "\n" + "cat students.txt > studentNames.txt" + "\n" + "cat newStudents.txt >> students.txt" + "\n" + "mv students.txt names.txt")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

15
f = open("Unattempted Questions LINUX.txt", "w")
(f.write("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60dc5ec4ccde02f8205963b3"  + "\n"))

###################### Module-3 ######################

# 1
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc8151cfaf5f6628f2d401")
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d99cb772f3f3f870e269e7")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc92c7cfaf5f6628f2d40b")
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9eae272f3f3f870e27a60")#link
driver.find_element_by_id("chkOpt5").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9ec6f72f3f3f870e27a62")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(3)

# 6
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc9673cfaf5f6628f2d410")
time.sleep(2)

# 7
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60dd452372f3f3f870e2c743")
time.sleep(2)

###################### Module-4 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9a0ed72f3f3f870e2747e")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "wc -l numbers.txt" + "\n" + "wc -L numbers.txt" + "\n" + "sort -g numbers.txt")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9b6f472f3f3f870e276ef")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "sort names.txt > sortedNames.txt" + "\n" + "grep -i '^D' names.txt > startsWithD.txt" + "\n" + "grep -i 'E$' names.txt > endsWithE.txt")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

2
f = open("Unattempted Questions LINUX.txt", "a")
(f.write("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9b6f472f3f3f870e276ef"  + "\n"))

# 3
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc9dfdcfaf5f6628f2d421")
time.sleep(2)

# 4
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc9e76cfaf5f6628f2d424")
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9ee0d72f3f3f870e27b02")#link
driver.find_element_by_id("chkOpt1").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9ef2972f3f3f870e27b39")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 7
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d9f0bb72f3f3f870e27ba8")#link
driver.find_element_by_id("chkOpt3").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(2)

# 8
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60da95eea85d46f848f4ad5e")#link
driver.find_element_by_id("chkOpt2").click()#
driver.find_element_by_id("executeMCQ").click()#Submit Button
time.sleep(3)

###################### Module-5 ######################

# 1
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cc9fe4cfaf5f6628f2d42b")
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60da9ef6a85d46f848f4ad61")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "#!/bin/bash" + "\n" + "echo Hello CodeQuotient")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60daa6d0a85d46f848f4ad65")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "#!/bin/bash" + "\n" + "read a" + "\n" + 'echo Hello "$a"! Welcome to CodeQuotient!')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 4
driver.get("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cca130cfaf5f6628f2d431")
time.sleep(2)

###################### Module-6 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60daad86a85d46f848f4af31")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "#!/bin/bash" + "\n" + "read a" + "\n" + "read b" + "\n" + "if [[ $a == $b ]]" + "\n" + "then" + "\n" + "echo 'EQUAL'" + "\n" + "else" + "\n" + "echo 'NOT EQUAL'" + "\n" + "fi")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60dab63fa85d46f848f4af6e")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.write("\n" + "#!/bin/bash" + "\n" + "read a" + "\n" + "if [ -e $a ]; then" + "\n" + "echo 'Exists'" + "\n" + "else" + "\n" + "echo 'Not Exists'" + "\n" + "fi")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60dabb4ca85d46f848f4afc6")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
declare -i a
declare -i b
declare -i c
declare -i sum
read a
read b
read c
sum="$a+$b+$c"
echo "$sum""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


# 4
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60cd9203b24fd66650a95db5")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
declare -i a
declare -i b
declare -i c
read a
read b
read c
if ((a>b));
then 
	if((a>c));
	then 
		echo ""$a""
	else
		echo ""$c""
	fi
else 
	if((b>c));
	then	
		echo ""$b""
	else
		echo ""$c""
	fi		
fi""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60dac652a85d46f848f4b0ff")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
read n
declare -i count
count=0
for (( i=1; i<=n; i++))
do
        read a
        if [ $((a%2)) -eq 0 ]
        then
                count=count+1
        fi
done
echo "$count""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60cd93f5b24fd66650a95dbd")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
declare -i a
declare -i b
declare -i c
read a
b=0
c=a
while [ $c -gt 0 ]
do
        b+=c%10
        c=c/10
done
echo $b""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

7
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60cd97aeb24fd66650a95dec")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
declare -i n
read n
for ((i=n;i>0;i=i-1)); do
        echo ""$i""
done""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 8
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/5a0f043154305147defdce88")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
declare -i n
declare -i sum
read n
sum=1
for ((i = 1; i<=n; i++)); do
        sum=$((sum*i))
done
echo $sum""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 9
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60cd9a55b24fd66650a95e03")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
read number
n=1
new=${#number}
while((n<=$new))
do
a=`echo $number | cut -c $n`
echo -n ""$a""
echo "" 
n=`expr $n + 2`
done""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

###################### Module-7 ######################

# 1
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60dad18da85d46f848f4b1e1")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
read a
read b
read c
con=$a$b$c
echo $con
echo ${#con}
read x
read y
# echo "$con:$x:$y"
printf "%s\n" "${con:x:y}""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 2
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60daddf1a85d46f848f4b668")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
read day
case $day in
1)
        echo "Monday"
        ;;
2)
        echo "Tuesday"
        ;;
3)
        echo "Wednesday"
        ;;
4)
        echo "Thursday"
        ;;
5)
        echo "Friday"
        ;;
6)
        echo "Saturday"
        ;;
7)
        echo "Sunday"
        ;;
*)
        echo "Invalid Day Number"
        ;;
esac""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 3
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60d19d2e9f664cbbcac6523e")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""#!/bin/bash
read a
read b
if [[ ""$a"" == *""$b""* ]]; then
    rest=${a#*$b}
    echo $(( ${#a} - ${#rest} - ${#b} +1 ))
else
    echo ""-1""
fi""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

4
f = open("Unattempted Questions LINUX.txt", "a")
(f.write("https://codequotient.com/attempt/attempttutorial/60dd90b3a85d46f848f4d643/60cca932cfaf5f6628f2d43c" + "\n"))

# 5
driver.get("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60cda4a7b24fd66650a95e34")#link
driver.find_element_by_class_name("CodeMirror-line").click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("""verifyPalindrome()
{
s=0
rev=""
temp=$num  
while [ $num -gt 0 ]
do
    s=$(( $num % 10 ))  
    num=$(( $num / 10 )) 
    rev=$( echo ${rev}${s} ) 
done
if [ $temp -eq $rev ];
then
    echo ""Yes""
else
    echo ""No""
fi
""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# 6
f = open("Unattempted Questions LINUX.txt", "a")
(f.write("https://codequotient.com/attempt/attemptquestion/60dd90b3a85d46f848f4d643/60cda151b24fd66650a95e16"  + "\n"))
f.close()




time.sleep(120)
driver.quit()