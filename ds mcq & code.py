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
import pyperclip


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

username = input('Enter Your Email: ')
password = getpass.getpass(prompt='Enter Your Password:')


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


driver.maximize_window()

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a1665ead875d7faa97f7")#link
driver.find_element_by_id("txtOutput0").send_keys("11")
driver.find_element_by_id("txtOutput1").send_keys("6")
driver.find_element_by_id("txtOutput2").send_keys("30")
driver.find_element_by_id("txtOutput3").send_keys("1")
driver.find_element_by_id("txtOutput4").send_keys("7")
driver.find_element_by_id("txtOutput5").send_keys("5")
driver.find_element_by_id("txtOutput6").send_keys("2")
driver.find_element_by_id("txtOutput7").send_keys("18")
driver.find_element_by_id("txtOutput8").send_keys("3")
driver.find_element_by_id("txtOutput9").send_keys("4")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a2a15ead875d7faa9808")#link
driver.find_element_by_id("txtOutput0").send_keys("9.0")
driver.find_element_by_id("txtOutput1").send_keys("9.6")
driver.find_element_by_id("txtOutput2").send_keys("2.2")
driver.find_element_by_id("txtOutput3").send_keys("6.0")
driver.find_element_by_id("txtOutput4").send_keys("6.0")
driver.find_element_by_id("txtOutput5").send_keys("8.0")
driver.find_element_by_id("txtOutput6").send_keys("1.25")
driver.find_element_by_id("txtOutput7").send_keys("3.0")
driver.find_element_by_id("txtOutput8").send_keys("4.0")
driver.find_element_by_id("txtOutput9").send_keys("6.4")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a3645ead875d7faa9814")#link
driver.find_element_by_id("txtOutput0").send_keys("val1%10;")
driver.find_element_by_id("txtOutput1").send_keys("val1/10%10;")
driver.find_element_by_id("txtOutput2").send_keys("val1/100%10;")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa2a4275ead875d7faa9857")#link
driver.find_element_by_id("txtOutput0").send_keys("(15*count-11)")
driver.find_element_by_id("txtOutput1").send_keys("(-10*count+40)")
driver.find_element_by_id("txtOutput2").send_keys("(4*count-11)")
driver.find_element_by_id("txtOutput3").send_keys("(-3*count+100)")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aa557b75ead875d7faab603")#link
driver.find_element_by_id("txtOutput0").send_keys("true")
driver.find_element_by_id("txtOutput1").send_keys("false")
driver.find_element_by_id("txtOutput2").send_keys("false")
driver.find_element_by_id("txtOutput3").send_keys("true")
driver.find_element_by_id("txtOutput4").send_keys("true")
driver.find_element_by_id("txtOutput5").send_keys("false")
driver.find_element_by_id("txtOutput6").send_keys("true")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41bb0af83792199391808e")#link
driver.find_element_by_id("txtOutput0").send_keys("7")
driver.find_element_by_id("txtOutput1").send_keys("8")
driver.find_element_by_id("txtOutput2").send_keys("7")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e09056dc3de029e4889e6")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n;cin>>n;
    if(n%2 == 0){
        cout<<"Even"<<endl;
    }
    else{
        cout<<"Odd"<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e123c6dc3de029e488a24")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[3];
    for (int i = 0; i < 3; i++)
    {
        cin>>arr[i];
    }
    cout<<(*max_element(arr,arr+3))<<endl;
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e0c006dc3de029e4889fb")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main()
{
  	int n;
    cin>>n;
    if(n%4==0){
        if(n%100==0 && n%400!=0){
            cout<<"Not a Leap Year";
        }
        else{
            cout<<"Leap Year";
        }
    }
    else{
        cout<<"Not a Leap Year";
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d46dfdf695fda3b2cd0ac34")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[] = {2000, 500, 100, 50, 20, 10, 5, 2, 1};
    int n;cin>>n;
    int x  = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < x; i++)
    {
        int z = n/arr[i];
        n  = n - z*arr[i];
        arr[i] = z;
    }
    for (int i = 0; i < x; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e1fd86dc3de029e488a94")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include<iostream>
//#include<cstdio>
//#include<cmath>
using namespace std;
int main()
{
  int n;
  cin>>n;
  int sum=0;
  for(int i=1;i<=n;i++){
    sum=sum+i; 
  }
  cout<<sum;
   return 0;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e30b56dc3de029e488ad4")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    for (int i = 1; i <= n; i++){
        for(int j=i;j>=1;j--){
            cout<<j;
        }
        for(int j=2;j<=i;j++){
            cout<<j;
        }
        cout<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e33116dc3de029e488ad7")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int p =1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout<<p;
            if(j != i){
                cout<<" ";
            }
            p++;
        }
        cout<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e35746dc3de029e488ade")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
     for (int i = 0; i < 1; i++)
    {
        for (int j = 1; j < n-i+1; j++)
        {
            cout<<j;
        }
        int p = n-i-1;
        for (int j = 1; j < n; j++)
        {
            cout<<p;
            p--;
        }
        cout<<endl;
    }
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            cout<<j+1;
        }
        for (int j = 0; j < 2*i+1; j++)
        {
            cout<<"*";
        }
        int p = n - i-1;
        for (int j = 0; j < (n-i-1); j++)
        {
            cout<<p;
            p--;
        }
        cout<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e20796dc3de029e488a9b")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    for (int i = 1; i <= m; i++)
    {
        cout<<(n*i)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

####################### Functions #######################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b68df83792199391806c")#link
driver.find_element_by_id("txtOutput0").send_keys("-2 + 4 = 7")
driver.find_element_by_id("txtOutput1").send_keys("4 + -2 = 3")
driver.find_element_by_id("txtOutput2").send_keys("2 + 11 = 5")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b6e7f837921993918071")#link
driver.find_element_by_id("txtOutput0").send_keys("12")
driver.find_element_by_id("txtOutput1").send_keys("2")
driver.find_element_by_id("txtOutput2").send_keys("16")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b7f9f837921993918077")#link
driver.find_element_by_id("txtOutput0").send_keys("1342213422")
driver.find_element_by_id("txtOutput1").send_keys("""quotient and coding like code
code and quotient like coding
""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41b8c5f83792199391807e")#link
driver.find_element_by_id("txtOutput0").send_keys("""
cq3: x = 23, y = 7
cq2: x = 12, y = 1, z = 7
cq1: x = 7, y = 11, z = 12
""")
driver.find_element_by_id("txtOutput1").send_keys("""
cq3: x = 44, y = 11
cq2: x = 23, y = 1, z = 11
cq1: x = 11, y = 21, z = 23
""")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4e652dd2b99733e5c16900")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int sumOfRange(int min, int max){
  int sum(0);
  for (int i = min; i <= max; i++)
  {
    sum += i;
  }
  return sum;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a093c7917bcb854c302bd23")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
 * Complete the function 'verifyPrime'
 * @params
 *  n ->number which is to be checked from primality test
 *
 * @return
 *   true if the number is a prime number else false
 */
bool verifyPrime(int n){
  // Write your code her
  if(n == 0 || n == 1){
      return false;
  }
  for (int i = 2; i < n; i++)
  {
      if(n%i == 0){
          return false;
      }
  }
  return true;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a11753954305147defdced0")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
 * Complete the function 'primeFactors'
 * Print all the prime factors of the number
 * @params
 *   n -> numbers whose prime factors are to be found
 */
void primeFactors(int n){
  // Write your code here
  while (n%2 == 0) 
    { 
        printf("%d", 2);
        cout<<endl; 
        n = n/2; 
    } 
    for (int i = 3; i <= sqrt(n); i = i+2) 
    { 
        while (n%i == 0) 
        { 
            printf("%d", i); 
            cout<<endl;
            n = n/i; 
        } 
    } 
    if (n > 2) 
        printf ("%d", n); 
        cout<<endl;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a1056fb54305147defdcec2")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
 * Complete the function 'gcd'
 * @params
 *   i -> first integer
 *   j -> second integer
 *
 *  @returns
 *  an integer, denoting the gcd of i and j
 */
int gcd(int i, int j){
  if(j == 0){
    return i;
  }
  return gcd(j,i%j);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4e7676d2b99733e5c16921")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int binaryToDecimal(string binary){
  string num=binary;
  int sum=0;
  int base=1;
  for (int i=num.length()-1;i>=0;i--){
    if (num[i]=='1'){
      sum+=base;
    }
    base=base*2;
  }
  return sum;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41bb0af83792199391808e")#link
driver.find_element_by_id("txtOutput0").send_keys("7")
driver.find_element_by_id("txtOutput1").send_keys("8")
driver.find_element_by_id("txtOutput2").send_keys("7")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41ba29f837921993918087")#link
driver.find_element_by_id("txtOutput0").send_keys("m1-ii")
driver.find_element_by_id("txtOutput1").send_keys("Error")
driver.find_element_by_id("txtOutput2").send_keys("m1-if")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4a03903714c2304e8557f4")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// write the overloaded sum() functions for 2, 3 and 4 arguments
int sum(int a,int b){
  return a+b;
}
int sum(int a,int b,int c){
  return a+b+c;
}
int sum(int a,int b,int c,int d){
  return a+b+c+d;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)


driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4a06483714c2304e8557fc")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// Write overloaded display(string a) and display(string a, string b) functions
void display(string a){
  cout<<a;
}
void display(string a,string b){
  cout<<a<<"-";
  cout<<b;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

################################ Dynamic Memory Managment ################################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411e7f1fa97021c32ce070")#link
driver.find_element_by_id("txtOutput0").send_keys("70 25")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411ec71fa97021c32ce073")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411f161fa97021c32ce074")#link
driver.find_element_by_id("txtOutput0").send_keys("31")
driver.find_element_by_id("txtOutput1").send_keys("1004")
driver.find_element_by_id("txtOutput2").send_keys("1004")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a411f731fa97021c32ce079")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2bcdae6dc3de029e4887c8")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4ad952f5c97d305544b0d7")#link
driver.find_element_by_id("txtOutput0").send_keys("68")
driver.find_element_by_id("txtOutput1").send_keys("88")
driver.find_element_by_id("txtOutput2").send_keys("76")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b44c4dce25fb6141524a0ef")#link
driver.find_element_by_id("txtOutput1").send_keys("True")
driver.find_element_by_id("txtOutput0").send_keys("True")
driver.find_element_by_id("txtOutput2").send_keys("True")
driver.find_element_by_id("txtOutput3").send_keys("False")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b44c555e25fb6141524a0f5")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("Yes")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b44c69de25fb6141524a0f9")#link
driver.find_element_by_id("txtOutput0").send_keys("True")
driver.find_element_by_id("txtOutput1").send_keys("True")
driver.find_element_by_id("txtOutput2").send_keys("False")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4ada9ef5c97d305544b0dc")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4adc14f5c97d305544b0dd")#link
driver.find_element_by_id("txtOutput0").send_keys("0")
driver.find_element_by_id("txtOutput1").send_keys("2")
driver.find_element_by_id("txtOutput2").send_keys("2")
driver.find_element_by_id("txtOutput3").send_keys("1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4adcddf5c97d305544b0e3")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5ca2e6c893d7f626b4060811")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

vector<int> cutSticks(vector<int> lengths) {
  sort(lengths.begin() , lengths.end());
  int shortest = INT_MIN;
  vector<int> ans;
  for(int i=0;i<lengths.size();i++){
    if(lengths[i] > shortest){
    	ans.push_back(lengths.size() -i);
    	shortest = lengths[i];  
    }
    
  }
  return ans;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

###################### Object & Classes ######################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b18b68d7becc0459de9bf72")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41e78a378b141faaf16c23")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41e856378b141faaf16c5c")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("No")
driver.find_element_by_id("txtOutput2").send_keys("Yes")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41e8fa378b141faaf16c6c")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("Yes")
driver.find_element_by_id("txtOutput2").send_keys("No")
driver.find_element_by_id("txtOutput3").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41ea32378b141faaf16c7b")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("No")
driver.find_element_by_id("txtOutput2").send_keys("Yes")
driver.find_element_by_id("txtOutput3").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b41ea7f378b141faaf16c81")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("No")
driver.find_element_by_id("txtOutput2").send_keys("Yes")
driver.find_element_by_id("txtOutput3").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4ae0d2f5c97d305544b0ec")#link
driver.find_element_by_id("txtOutput0").send_keys("Modular")
driver.find_element_by_id("txtOutput1").send_keys("Monolithic")
driver.find_element_by_id("txtOutput2").send_keys("Object-Oriented")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aba57adecf32f0f52165aa5")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
class TimeSpan
{
  private: int hours;
  private: int minutes;
  public: TimeSpan(int initialHours, int initialMin){
    hours = 0;
    minutes = 0;
add(initialHours, initialMin);
  }
  public: int getHours(){
    return hours;
  }
  public: int getMinutes(){
    return minutes;
  }
  public: void add(int initialHours, int initialMin){
    hours += initialHours;
    minutes += initialMin;
	if(minutes >= 60){
      minutes -= 60;
      hours++;
    }
  }
  public: void add(TimeSpan tp){
	add(tp.hours, tp.minutes);
  }
  public: double getTotalHours(){
    return hours + minutes / 60.0;
  }
  public: std::string toString(){
std::string str{std::to_string(hours)+" Hours, "+std::to_string(minutes)+" Minutes"};
    return str;
  }
};
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5aba5b3becf32f0f52165adb")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

class Date
{
  // Write your code here
  private:
  int month,day;
  public:
  Date(int m,int d){
    month=m;
    day=d;
  }
  int daysInMonth(){
    if(month==4|| month==6 || month==9 || month==11){
      return 30;
    }else if(month==2){
      return 28;
    }
    else{
      return 31;
    }
  }
  int getDay(){
    return day;
  }
  int getMonth(){
    return month;
  }
  void nextDay(){
    day++;
    if(day>=daysInMonth()){
      month++;
      day=1;
      if(month>12){
        month=1;
      }
    }
  }
  string toString(){
    string result="";
    result+=to_string(month);
    result+="/";
    result+=to_string(day);
    return result;
  }
  int absoluteDay(){
    int days;
    days=day;
    switch(getMonth()){
      case 2:
        days+=31;
        break;
      case 3:
        days+=31+28;
        break;
      case 4:
        days+=31+28+31;
        break;
      case 5:
        days+=31+28+31+30;
        break;
      case 6:
        days+=31+28+31+30+31;
        break;
      case 7:
        days+=31+28+31+30+31+30;
        break;
      case 8:
        days+=31+28+31+30+31+30+31;
        break;
      case 9:
        days+=31+28+31+30+31+30+31+31;
        break;
      case 10:
        days+=31+28+31+30+31+30+31+31+30;
        break;
      case 11:
        days+=31+28+31+30+31+30+31+31+31;
        break;
      case 12:
        days+=31+28+31+30+31+30+31+31+31+30+30;
        break;
    }
    return days;
  }
};
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5b4cad9d2a3f026b0f4f0fc9")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int cnt=0;	// manipluate this variable in your code
class Counter
{ 
  public: 
	Counter(){
            cnt++;
            //cout<<"c1 id "<<cnt<<endl;
        }
        ~Counter(){
            cnt--;
            //cout<<"c2 id "<<cnt<<endl;
        }
};
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

############################ Asymptotic Notations ############################

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60db0fb0a85d46f848f4c912")
time.sleep(2)

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/60db1774a85d46f848f4c915")
time.sleep(2)

########################## Arrays & Linear Search ####################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a42313b1fa97021c32ce0a3")#link
driver.find_element_by_id("txtOutput0").send_keys("1 2 3 4 5")
driver.find_element_by_id("txtOutput1").send_keys("5 4 3 2 1")
driver.find_element_by_id("txtOutput2").send_keys("5 -15 -58 -35 25")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4231711fa97021c32ce0a8")#link
driver.find_element_by_id("txtOutput0").send_keys("1 -1 -4 -8 -13")
driver.find_element_by_id("txtOutput1").send_keys("5 1 -2 -4 -5")
driver.find_element_by_id("txtOutput2").send_keys("5 -60 -105 -107 -132")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4231aa1fa97021c32ce0ad")#link
driver.find_element_by_id("txtOutput0").send_keys("2 1 4 3 6")
driver.find_element_by_id("txtOutput1").send_keys("6 3 4 1 2")
driver.find_element_by_id("txtOutput2").send_keys("6 64 46 1 26 ")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4231ef1fa97021c32ce0b2")#link
driver.find_element_by_id("txtOutput0").send_keys("1 2 3 4 5")
driver.find_element_by_id("txtOutput1").send_keys("5 4 3 2 1")
driver.find_element_by_id("txtOutput2").send_keys("5 25 27 2 25")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a42359e1fa97021c32ce0c2")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487f12b1afa55f38fed739")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487f45b1afa55f38fed73a")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487fabb1afa55f38fed73b")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/59ff2beae63d6b7fd5dec1af")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include<iostream>
#include<cstdio>
#include<cmath>
# include<bits/stdc++.h>
// Include headers as needed
using namespace std;
int main()
{
  int n = 5;
  int arr [n];
  for(int i=0;i<n;i++){
    cin>>arr[i];
  }
  int max1 = INT_MIN , max2 = INT_MIN;
  for(int i=0;i<n;i++){
    if(arr[i]>max1){
      max1 = arr[i];
    }
  }
  for(int j=0;j<n;j++){
    if(arr[j]>max2 && arr[j]<max1){
      max2 = max(max2 , arr[j]);
    }
  }
  if(max2 == INT_MIN){
    cout<<0<<endl;
  }
  else{
  	cout<<max2;  
  }
    return 0;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fb5ee7a3c1824dba91428")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
   int T;
   cin>>T;
   for (int i = 0; i < T; i++)
   {
       int mf = 0;
       int max_count = 0;
       int n;
       cin>>n;
       int a[n];
       for (int i = 0; i < n; i++)
       {
           cin>>a[i];
       }
       for (int i = 0; i < n; i++)
       {
             	int count = 0;
           for (int j = i+1; j < n; j++)
           {
               if(a[i] == a[j]){
                   count++;
               }
               if(count >= max_count){
                   max_count = count;
                   mf = a[i];
               }
           }
       }
       cout<<mf<<endl;
   }
   return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a2e543e6dc3de029e488b37")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[10];
    for (int i = 0; i < 10; i++)
    {
        cin>>arr[i];
    }
    int neg(0),pos(0),even(0),odd(0);
    for (int i = 0; i < 10; i++)
    {
        if(arr[i]>=0){
            pos++;
        }
        if(arr[i]<0){
            neg++;
        }
        if(arr[i]%2 == 0){
            even++;
        }
        else{
            odd++;
        }
    }
    cout<<pos<<endl;
    cout<<neg<<endl;
    cout<<even<<endl;
    cout<<odd<<endl;
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d9f41ae5f73f530a20bd5d6")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   int arraysEqualorNot(vector<int> A, vector<int> B) {
  sort(A.begin(),A.end());
  sort(B.begin(),B.end());
  for (int i = 0; i < A.size(); i++)
   {
       if(A[i] != B[i]){
           return 0;
       }
   }
   return 1;
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fafbb7a3c1824dba9141c")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
void moveElements(int arr[], int n){
   int key,j;
   for (int i = 0; i < n; i++)
   {
       key = arr[i];
       j = i-1;
       while (j>=0 && arr[j]<0 && key>=0)
       {
           arr[j+1] = arr[j];
           j--;
       }
       arr[j+1] = key;
   }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

############################# Binary Search #########################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a487fdfb1afa55f38fed73c")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a48801bb1afa55f38fed73d")#link
driver.find_element_by_id("txtOutput0").send_keys("9")
driver.find_element_by_id("txtOutput1").send_keys("29")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488049b1afa55f38fed741")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488065b1afa55f38fed742")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fc0117a3c1824dba91440")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int getPairsCount(int arr[], int n, int sum){
  // Write your code here
  int s=0;
  int l=n-1;
  int count=0;
  while(s<l){
    if(arr[s]+arr[l]<sum) s++;
    else if(arr[s]+arr[l]==sum){
      int p=l;
      while(arr[l]==arr[p] && p>s){
        count++;
        p=p-1;
      }
      s++;
    }
    else{
    l--;
    }
  }
  return count;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a50df747a3c1824dba915dc")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
int find(int arr[],int n,int k){
    for (int i = 0; i < n; i++)
    {
         if(arr[i] == k){
            return i;
            break;
        }
    }
    return -1;
}
int main(){
    int t;cin>>t;
    while (t--)
    {
        int n,k;
        cin>>n>>k;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<find(arr,n,k)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d81f1f6e9156a66a25b7709")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int rotationCount(int a[], int size){
   int mn = *min_element(a,a+size);
    for (int i = 0; i < size; i++)
    {
        if(a[i] == mn){
            return i;
        }
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a539b04f239e2076be893e8")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

void sort(int arr[],int n){
   for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            if (arr[i] > arr[j])
            {
                int temp =  arr[i];
                arr[i] = arr[j];        
                arr[j] = temp;
            }
        }
    }
}
int getMissingElement(int* a,int a_size,int* b ,int b_size){
  	sort(a,a_size);
    sort(b,b_size);
    for (int i = 0; i < b_size; i++)
    {
        if(a[i] != b[i]){
            return a[i];
        }
    }
    return a[a_size-1];
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

########################## Linked Lists ########################## 

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f280f89496f09677d64e9")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f287289496f09677d64f2")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f291189496f09677d64fd")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f298989496f09677d6527")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f29d789496f09677d652e")#link
driver.find_element_by_id("txtOutput0").send_keys("True")
driver.find_element_by_id("txtOutput1").send_keys("False")
driver.find_element_by_id("txtOutput2").send_keys("True")
driver.find_element_by_id("txtOutput3").send_keys("False")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2ba289496f09677d6563")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2be889496f09677d656d")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f515c89496f09677d6947")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void forwardPrint(struct Node* head)
{
	if(head != NULL){
      cout<<head->data<<"-";
      forwardPrint(head->next);
    }
}
void backwardPrint(struct Node* head)
{
	if(head != NULL){
    backwardPrint(head->next);
    cout<<head->data<<"-";
  }
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70766389496f09677d7734")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/*
struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
struct Node *copyList(struct Node *org)
{
	 Node *ptr = NULL;
    while (org != NULL)
    {
      insertEnd(&ptr , org->data);
      org = org->next;
    }
    return ptr;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2ccb89496f09677d6585")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a707dd489496f09677d78ad")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
# include<bits/stdc++.h>
int minNode(Node *head){
    Node *last = head;
    int min = INT_MAX;
    while (last != NULL)
    {
        if(last->data < min){
            min = last->data;
        }
        last = last->next;
    }
    return min;
}
int maxNode(Node *head){
    Node *last = head;
    int max = INT_MIN;
    while (last != NULL)
    {
        if(last->data > max){
            max = last->data;
        }
        last = last->next;
    }
    return max;
}
void insertBeg(struct Node** head, int data){
  struct Node* node = (struct Node*) malloc(sizeof(struct Node));
  node->data  = data;     
  node->next = (*head);   
  (*head)    = node;  
}
struct Node * shiftSmallLarge(struct Node *org)
{
  	int x = minNode(org);
    int y = maxNode(org);
    if(org == NULL){
        return org;
    }
  	Node *ptr = NULL;
  	if(org->next == NULL){
        insertBeg(&ptr , x);
        return ptr;
    }
    Node *last = org;
    while (last != NULL)
    {
        if(last->data == x){
            last = last->next;
        }
        else if(last->data == y){
            last = last->next;
        }
        else{
            insertEnd(&ptr , last->data);
            last = last->next;
        }
    }
    insertBeg(&ptr , x);
    insertEnd(&ptr , y);
    return ptr;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b21d89496f09677d87e7")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
# include<bits/stdc++.h>
int checkPalindrome(struct Node* head) 
{
    if(head == NULL){
        return 0;
    }
	Node *ptr = head;
    stack<int> s;
    while (ptr != NULL)
    {
        s.push(ptr->data);
        ptr = ptr->next;
    }
    while (head != NULL)
    {
      int i = s.top();
      s.pop();
      if(head->data != i){
        return 0;
      }
      head = head->next;
    }
  return 1;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71aeac89496f09677d8758")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
int countNodes(struct Node *n)
{
    int res = 1;
    struct Node *temp = n;
    while (temp->next != n)
    {
        res++;
        temp = temp->next;
    }
    return res;
}
int  loopInList(Node* head) {
  struct Node *slow_p = head, *fast_p = head;
    while (slow_p && fast_p &&
                     fast_p->next)
    {
        slow_p = slow_p->next;
        fast_p = fast_p->next->next;
        if (slow_p == fast_p)
            return countNodes(slow_p);
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71abef89496f09677d871c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node *ptr = NULL;
void giveReverse(Node *head){
  ptr = NULL;
    if(head != NULL){
      giveReverse(head->next);
      insertEnd(&ptr,head->data);
    }
}
struct Node* reverseList(struct Node* head) {
    giveReverse(head);
  	return ptr;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2ea689496f09677d65b4")#link
driver.find_element_by_id("txtOutput0").send_keys("1 3 5 5 3 1")
driver.find_element_by_id("txtOutput1").send_keys("1 2 3 3 2 1")
driver.find_element_by_id("txtOutput2").send_keys("1 1 2 2 1 1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f2fdd89496f09677d65e0")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f309a89496f09677d65f9")#link
driver.find_element_by_id("txtOutput0").send_keys("2 1 4 3 6 5")
driver.find_element_by_id("txtOutput1").send_keys("1 1 2 2 3 3")
driver.find_element_by_id("txtOutput2").send_keys("1 1 2 1 2 2")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f317b89496f09677d6626")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b40f89496f09677d880a")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// struct Node
// {
//   int data;
//   Node* next;
// };
// Above node is used to declare a node
Node* addListNumbers(Node* head1,Node* head2){
  	int x = 0;
    int i = 0;
    while (head1 != NULL)
    {
      int m = head1->data;
      x = m*pow(10,i) + x;
      i++;
      head1 = head1->next;
    }
    int y = 0;
    int j = 0;
    while (head2 != NULL)
    {
      int m = head2->data;
      y = m*pow(10,j) + y;
      j++;
      head2 = head2->next;
    }
    int sum = x+y;
    Node *ptr = NULL;
    while (sum > 0 )
    {
      int x = sum%10;
      insertEnd(&ptr ,x);
      sum = sum/10;
    }
    return ptr;
}   
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b84689496f09677d8879")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
void deleteNodeK(Node* node){
    if(node == NULL){
      return;
    }
    if (node->next == NULL)
    {
        //free(node);
        return;
    }
    Node* temp = node->next;
    node->data = temp->data;
    node->next = temp->next;
    free(temp);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

################################# Doubly Linked Lists #################################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f336f89496f09677d6669")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f496589496f09677d6863")#link
driver.find_element_by_id("txtOutput0").send_keys("5 4 3 2 1")
driver.find_element_by_id("txtOutput1").send_keys("3 3 2 2 1 1")
driver.find_element_by_id("txtOutput2").send_keys("6 5 2 3 4")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f49d489496f09677d686d")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4ac489496f09677d688c")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4b5389496f09677d68a0")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4cc589496f09677d68c6")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4d4489496f09677d68ca")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4dca89496f09677d68d4")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71b9a389496f09677d88a7")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
    int data;
    struct Node *next;
  	struct Node *prev;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void swapNodes(Node** head, int x, int y){
  		if(x == y){
       return;
   }
    Node *prevX = NULL , *currX = *head;
    while (currX && currX->data != x)
    {
        prevX = currX;
        currX = currX->next;
    }
    Node *prevY = NULL , *currY = *head;
    while (currY && currY->data != y)
    {
        prevY = currY;
        currY = currY->next;
    }
    if(currX == NULL || currY == NULL){
        return;
    }
    if(prevX != NULL){
        prevX->next = currY;
    }
    else{
        *head = currY;
    }
    if(prevY != NULL){
    prevY->next = currX;
    }
    else{
        *head = currX;
    }
    Node *temp = currY->next;
    currY->next = currX->next;
    currX->next = temp;
}


 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d09b89496f09677d8d92")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
    int data;
    Node *next;
  	Node *prev;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void insertAtBeg(Node **head , int data){
    Node *node = new Node(data);
    node->data = data;
    node->next = *head;
    node->prev = NULL;
    if(head != NULL){
        (*head)->prev = node;
    }
    *head = node;
}
int deleteAtEnd(Node *head){
    Node *last = head;
    while (last->next != NULL)
    {
        last = last->next;
    }
    int x = last->data;
    last->prev->next = NULL;
    delete(last);
    return x;
}
Node* rotateByK(Node* head, int k)
{
	 if(head == NULL){
        return head;
    }
    for (int i = 0; i < k; i++)
    {
        int x = deleteAtEnd(head);
        insertAtBeg(&head,x);
    }
    return head;
}


 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d13989496f09677d8d9d")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node *next;
  	Node *prev;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* rearrangeList(Node* head){
   int i = 1;
    Node *even = NULL;
    Node  *odd = NULL;
    Node *last = head;
    while (last != NULL)
    {
      if(i%2 == 0){
        even = insertEnd(even , last->data);
      }
      if(i%2 != 0){
        odd = insertEnd(odd , last->data);
      }
      last = last->next;
      i++;
    }
    Node *final = NULL;
    while (even != NULL)
    {
      final = insertEnd(final , even->data);
      even = even->next;
    }
    while (odd != NULL)
    {
      final = insertEnd(final , odd->data);
      odd = odd->next;
    }
    return final;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

############################ Circular Linked List ############################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4e8389496f09677d68eb")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a6f4f0a89496f09677d68f2")#link
driver.find_element_by_id("txtOutput0").send_keys("5")
driver.find_element_by_id("txtOutput1").send_keys("4")
driver.find_element_by_id("txtOutput2").send_keys("5")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7593d2a0bdb04eb16c3c04")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
int isCircular(Node* head){
  	if(head == NULL){
      return 1;
    }
  	Node *node = head->next;
      while (node != head && node != NULL)
      {
        node = node->next;
      }
      return (node == head);    
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a759518a0bdb04eb16c3c0f")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* insertBeg(Node* head, int data){
  	 Node *ptr = new Node();
    ptr->data = data;
    ptr->next = NULL;
    Node *temp ;
    if(ptr == NULL){
        cout<<endl;
        printf("OVERFLOW");
    }
    else{
        if(head  == NULL){
            head = ptr;
            ptr->next = head;
        }
        else{
            temp = head;
            while (temp->next != head)
            {
                temp = temp->next;
            }
            ptr->next = head;
            temp->next = ptr;
            head = ptr;
        }
    }
  return head;
}
Node* insertEnd(Node* head, int data){
  Node *ptr = new Node();
    ptr->data = data;
    ptr->next = NULL;
    Node *temp ;
    if(ptr == NULL){
        cout<<endl;
        printf("OVERFLOW");
    }
    else{
        if(head  == NULL){
            head = ptr;
            ptr->next = head;
        }
        else{
            temp = head;
            while (temp->next != head)
            {
                temp = temp->next;
            }
            temp->next = ptr;
            ptr->next = head;
            return head;
        }
    }
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7595baa0bdb04eb16c3c19")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* deleteBeg(Node* head){
  	Node *p = head;
    while (p->next != head)
    {
        p = p->next;
    }
    p->next = head->next;
    int x = head->data;
    delete head;
    head = p->next;
    return head;
}
Node* deleteEnd(Node* head){
  	Node *p = head;
    while (p->next->next != head)
    {
        p = p->next;
    }
    Node *q = p->next;
    p->next = head;
    delete q;
    return head;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a75964aa0bdb04eb16c3c20")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
int countNodes(Node* head){
   int length = 0;
    if(head == NULL){
        return 0;
    }
    Node *p = head;
    while (p->next != head)
    {
        length++;
        p = p->next;
    }
    return length+1;
}

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7597cfa0bdb04eb16c3c26")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
void sortedInsert(Node **head , Node *newN){
    Node *current = *head;
    if(current == NULL){
        newN->next = newN;
        *head = newN;
    }
    else if(current->data >= newN->data){
        /* If value is smaller than head's value then
        we need to change next of last node */
        *head = insertBeg(*head , newN->data);
    }
    else{
        /* Locate the node before the point of insertion */
        while (current->next != *head && current->next->data < newN->data)
        {
            current = current->next;
        }
        newN->next = current->next;
        current->next = newN;
    }
}
Node* insertSorted(Node* head , int k){
    Node *ptr = new Node();
    ptr->data = k;
    sortedInsert(&head ,ptr);
    return head;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a759729a0bdb04eb16c3c23")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
    int data;
    struct Node* next;
};
Above structure is used to define the linked list, You have to complete the below functions only */
Node* listCut(Node* head){
 Node *head1=NULL;
  Node *head2=NULL;
  Node *temp1=head;
  Node *temp2=head;
  if(head==NULL) return 0;
  while(temp2->next!=head && temp2->next->next!=head){
    temp2=temp2->next->next;
    temp1=temp1->next;
  }
  if(temp2->next->next==head) temp2=temp2->next;
  head1=head;
  if(head->next!=head) head2=temp1->next;
  temp2->next=temp1->next;
  temp1->next=head;
  return head1,head2;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

################################### Stack ##############################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705c2489496f09677d73cf")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705ca889496f09677d73d0")#link
driver.find_element_by_id("txtOutput0").send_keys("DEOOUQITCETN")
driver.find_element_by_id("txtOutput1").send_keys("EDOCOUQITNET")
driver.find_element_by_id("txtOutput2").send_keys("OCEDOITEUQTN")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705d8789496f09677d73e1")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705e2589496f09677d73e6")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705ea889496f09677d73ef")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d4bc89496f09677d8f1d")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int isFull()
{
	return top == SIZE - 1;
}
// Function to check if stack is empty.
int isEmpty()
{
	return top == -1;
}
// Function to add an item to stack.
int push(int item)
{
	 if (isFull())
    {
        return -1;
    }
    else{
        Stack[++top] = item;
    }
}
// Function to remove an item from stack.
int pop()
{
	if(isEmpty()){
        return -1;
    }
    else{
        int val = Stack[top--];
        return val;
    }
}

""")
pyautogui.hotkey('ctrl', 'v')



WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d80889496f09677d8f55")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

string reverseString(CQStack *stack,string s){
  	 string ans = "";
    CQStack *sp = new CQStack(s.length());
    for (int i = 0; i < s.length(); i++)
    {
        sp->push(s[i]);
    }
    for (int i = 0; i < s.length(); i++)
    {
        int temp = sp->pop();
        ans += temp;
    }
    return ans;
}


""")
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705f0989496f09677d73f0")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a71d70489496f09677d8f46")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

class LinkStack{
  LinkList *first; // ref to first item on list
  int size;
  public:
    LinkStack(){
      	first = NULL;
        size = 0; 
    }
    bool isEmpty(){
		return first == NULL;
    }
    void push(int dd){
 		LinkList *ptr = new LinkList(dd);
         ptr->next = first;
         first = ptr;
         size ++;
     }
     int pop(){
 		if(isEmpty()){
             return -1;
         }
         size--;
         int temp = first->data;
         first = first->next;
         return temp;
     }
 };
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7338967e4d2702dca0472c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 void push(int item)
 {
 	if (isFull())
     {
         return;
     }
     else{
         Stack[++top] = item;
     }
 }
 // Function to remove an item from stack.
 int pop()
 {
 	 if(isEmpty()){
         return -1;
     }
     else{
         int val = Stack[top--];
         return val;
     }
 }
 // Function to return the minimum item from stack.
 int getMin()
 {
 	 int a = top;
     int min = Stack[a];
     while (a != -1)
     {
         int x = Stack[a];
         if(x<min){
             min = x;
         }
         a--;
     }
     return min;
 }


 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a73399d7e4d2702dca04734")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

 void printNextGreaterElement(int arr[],int n){
   for (int i = 0; i < n; i++)
     {
         for (int j = i; j < n; j++)
         {
             if(arr[j]>arr[i]){
                 cout<<arr[j]<<" ";
                 break;
             }
             else if(j == n-1){
                 cout<<"-1"<<" ";
             }
         }
     }
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733a277e4d2702dca0473c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

 int minReversal(char* expr){
   int len = strlen(expr);
     if (len%2)
 	return -1;
 	stack<char> s;
 	for (int i=0; i<len; i++)
 	{
 		if (expr[i]==']' && !s.empty())
 		{
 			if (s.top()=='[')
 				s.pop();
 			else
 				s.push(expr[i]);
 		}
 		else
 			s.push(expr[i]);
 	}
 	int x = s.size();
 	int n = 0;
 	while (!s.empty() && s.top() == '[')
 	{
 		s.pop();
 		n++;
 	}
 	return (x/2 + n%2);
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705f5f89496f09677d73f6")#link
driver.find_element_by_id("txtOutput0").send_keys("-24")
driver.find_element_by_id("txtOutput1").send_keys("52")
driver.find_element_by_id("txtOutput2").send_keys("4")
driver.find_element_by_id("txtOutput3").send_keys("-18")
driver.find_element_by_id("txtOutput4").send_keys("350")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a705fa089496f09677d73fe")#link
driver.find_element_by_id("txtOutput0").send_keys("3")
driver.find_element_by_id("txtOutput1").send_keys("2205")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70601589496f09677d7409")#link
driver.find_element_by_id("txtOutput0").send_keys("xy+2^x4-3/+")
driver.find_element_by_id("txtOutput1").send_keys("+^+xy2/-x43")
driver.find_element_by_id("txtOutput2").send_keys("ABC+-D*")
driver.find_element_by_id("txtOutput3").send_keys("*-A+BCD")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7060fd89496f09677d7423")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733bbc7e4d2702dca04794")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 struct stack{
   int size;
   char data;
   int top;
 };
 int isOperand(char ch){
     return (ch>= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z' || (isdigit(ch)));
 }
 int checkPrecedence(char ch){
     switch(ch){
         case '+':
         case '-':
             return 1;
         case '*':
         case '/':
             return 2;
         case '^':
             return 3;
     }
     return -1;
 }
 int infixToPostfix(char exp[], char output[])
 {
 	 int i = 0,k = 0;
     while (exp[i])
     {
         if(isOperand(exp[i])){
             output[k++] = exp[i];
         }
         else if(exp[i] == '('){
             push(exp[i]);
         }
         else if(exp[i] == ')'){
             while (!isEmpty() && Stack[top] != '(')
             {
                 output[k++] = Stack[top];
                 pop();
             }
             if(!isEmpty() && Stack[top] != '('){
                 return -1;
             }
             else{
                 pop();
             }
         }
         else{
             while (!isEmpty() && checkPrecedence(exp[i]) <= checkPrecedence(Stack[top]))
             {
                 output[k++] = Stack[top];
                 pop();
             }
             push(exp[i]);
         }
         i++;
     }
     while (!isEmpty())
     {
         output[k++] = Stack[top];
         pop();
     }
     output[k++] = '\\0';
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733c607e4d2702dca0479b")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

 int evalPostfix(CQStack *stack,string exp){
     int answer;
     CQStack *st = new CQStack(exp.length());
     for (int i = 0; i < exp[i]; i++)
     {
         if(isdigit(exp[i])){
             st->push(exp[i] - '0');
         }
         else{
             int op2 = st->pop();
             int op1 = st->pop();
             switch (exp[i])
             {
             case '+':
                 st->push(op1 + op2);
                 break;
             case '-':
                 st->push(op1 - op2);
                 break;
             case '*':
                 st->push(op1 * op2);
                 break;
             case '/':
                 st->push(op1 / op2);
                 break;
               case '^':
                 st->push(pow(op1,op2));
             }
         }
     }
     answer = st->pop();
     return answer;
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733d077e4d2702dca047ab")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 int evalPrefix(char* exp)
 {
 	int i,op1,op2;
   	int len = strlen(exp);
 	for ( i = len-1; i>=0 ; i--)
     {
       char c = exp[i];
       if (isdigit(c))
         push(c-'0');
       else
       {
         op1 = pop();
         op2 = pop();
         switch(c)
         {
           case '+': push(op1 + op2); break;
           case '-': push(op1 - op2); break;
           case '*': push(op1 * op2); break;
           case '/': push(op1 / op2); break;
           case '^':push(pow(op1,op2)); break;
         }
       }
     }
  	return pop();
 }
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# ################ Queue #####################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70659c89496f09677d74bb")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7065fe89496f09677d74c2")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70663389496f09677d74c8")#link
driver.find_element_by_id("txtOutput0").send_keys("CODEQUOTIENT")
driver.find_element_by_id("txtOutput1").send_keys("CODEQUOTIENT")
driver.find_element_by_id("txtOutput2").send_keys("CODEQUOTIENT")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a733ecf7e4d2702dca04877")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 void enqueue(int item)
{
	if(rear == SIZE){
      return;
    }
    if(front == -1 && rear == -1){
      front++;
      rear++;
    }
    else{
      rear++;
    }
    array[rear] = item;
}
// Method to remove an item from queue.
int dequeue()
{
	if(front>rear){
    return -1;
  }
  int item = array[front];
  front++;
  return item;
}
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70668889496f09677d74d3")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70675389496f09677d74eb")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7067c889496f09677d74f3")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70684489496f09677d74f4")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7340417e4d2702dca04904")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
class Queue { 
    struct QNode { 
        int data; 
        QNode* next; 
        QNode(int d){ 
            data = d; 
            next = NULL; 
        } 
    }; 
    QNode *front, *rear; 
    public:
  		// Constructor
        Queue(){
        }
  		// Add an element to the queue
        void enQueue(int x){
			QNode* newNode = new QNode(x);
      if(rear == NULL){
          front = rear = newNode;
          return;
      }
      rear->next = newNode;
      rear = newNode;
        }
  		// Delete front element from the queue
        int deQueue() { 
			 if(front == NULL){
          return -1;
       }
        int temp = front->data;
        front = front->next;
        if (front == NULL){
            rear = NULL;
        }
        return temp;
        }
};
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7341a37e4d2702dca0492c")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
 void reverseQueue(Queue *queue){
  // Write your code here 
  int arr[1000];
   int i = 0;
   while (!queue->isEmpty())
   {
       int temp = queue->deQueue();
       arr[i] = temp;
      i++;
   }
  for (int j = i-1; j >= 0; j--)
  {
    int x = arr[j];
    queue->enQueue(x);
  }
}
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7344a27e4d2702dca04960")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
/* push(int), pop(), isEmpty(), isFull() are available on Stack. */
class Queue
{
  //Beaware to do it public
  public:
  void enqueue(CQStack *st1, CQStack *st2, int item)
  {
		st1->push(item);
  }
  int dequeue(CQStack *st1, CQStack *st2)
  {
		if(st2->isEmpty() && st1->isEmpty()){
          return -1;
        }
        if(st2->isEmpty()){
            while (!st1->isEmpty())
            {
                st2->push(st1->pop());
            }
        }
        int temp = st2->pop();
        return temp;
  }
};
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7345b27e4d2702dca049b4")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
class Stack
{
  public:
  void push(QueueArray* qa1, QueueArray* qa2, int item)
  {
     while (!(qa1->front > qa1->rear))
      {
          qa2->enqueue(qa1->dequeue());
      }
      qa1->enqueue(item);
      while (!(qa2->front > qa2->rear))
      {
          qa1->enqueue(qa2->dequeue());
      }
  }
  int pop(QueueArray* qa1, QueueArray* qa2)
  {
    if((qa1->front > qa1->rear)){
          return -1;
      }
      int x = qa1->dequeue();
      return x;
  }
};
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

################## CQueue Module #####################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7068a289496f09677d7505")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70690489496f09677d750e")#link
driver.find_element_by_id("txtOutput0").send_keys("2 5")
driver.find_element_by_id("txtOutput1").send_keys("2 0")
driver.find_element_by_id("txtOutput2").send_keys("2 1")
driver.find_element_by_id("txtOutput3").send_keys("3 1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a759ed8a0bdb04eb16c3d28")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
// class QueueArray{
//   const int SIZE = 4; // Size of queue array
//   int front = -1; // front variable
//   int rear = -1; // rear variable
//   int *queue; // queue array 
//   public:
//   	QueueArray() // constructor 
//   	void enQueue(int data); // add data to the queue
//   	int deQueue(); // remove data from the queue
// };
// The above declaration is already done. Complete the function given below.
// Add data to the circular queue
void QueueArray::enQueue(int data){
   if((front == 0 && rear == SIZE-1) || (rear == (front - 1)%(SIZE-1))){
        return ;
    }
    if(front == -1){
        front = rear = 0;
    }
    else if(rear == SIZE-1 && front != 0){
        rear = 0;
    }
    else{
        rear++;
    }
    queue[rear] = data;
}
// Remove First element from queue
int QueueArray::deQueue(){
  if(front == -1){
        return -1;
    }
    int item = queue[front];
    if(front == rear ){
        front  = rear = -1;
    }
    else if(front == SIZE-1){
        front = 0;
    }
    else{
        front++;
    }
    return item;
}
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

# ################ Priority Queue #####################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70693989496f09677d7516")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a70698e89496f09677d7522")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a75d71da0bdb04eb16c3f35")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// struct Node{
//   int data;
//   int priority;
//   Node* next;
//   Node();
//   Node(int d,int p);
// };
// The above structure is used to declare a node
# include<bits/stdc++.h>
class PriorityQueue{
    Node *front, *rear;
    public:
      PriorityQueue(){
        front = NULL;
        rear = NULL;
      }
    void enQueue(int data,int priority){
      Node *tmp , *q;
      tmp = new Node(data,priority);
      if(front == NULL || priority < front->priority){
        tmp->next = front;
        front = tmp;
      }
      else{
        q = front;
        while (q->next != NULL && q->next->priority <= priority)
        {
          q = q->next;
        }
        tmp->next = q->next;
        q->next = tmp;
      }
    }
  	int deQueue(){
          Node *tmp;
          if(front == NULL){
              return -1;
          }
          else
          {
            tmp = front;
            int x = tmp->data;
            // cout<<tmp->data<<" ";
            front = front->next;
            free(tmp);
            return x;
          }
          return -1;		
    }
};


   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

############### Sorting #####################

driver.get("https://codequotient.com/attempt/attempttutorial/60d991baccde02f820596293/5a12e62546765b2b63e34716")
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488e3fb1afa55f38fed743")#link
driver.find_element_by_id("txtOutput0").send_keys("4")
driver.find_element_by_id("txtOutput1").send_keys("2")
driver.find_element_by_id("txtOutput2").send_keys("3")
driver.find_element_by_id("txtOutput3").send_keys("1")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488e6cb1afa55f38fed749")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488eb2b1afa55f38fed74a")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488ed8b1afa55f38fed74b")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488f09b1afa55f38fed74c")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fb6d87a3c1824dba9142b")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
    # include<bits/stdc++.h>
using namespace std;
int numberOfSwaps(int *A,int n){
    int isSorted = 1;
    int swap(0);
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if(A[j]>A[j+1]){
                int temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
                isSorted = 0;
                swap++;
            }
        }
        if(isSorted){
            return swap;
        }
    }
    return swap;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;cin>>n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<numberOfSwaps(arr,n)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489029b1afa55f38fed752")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489053b1afa55f38fed753")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489079b1afa55f38fed754")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a48909bb1afa55f38fed755")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4890bbb1afa55f38fed756")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)


driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a4fb7f57a3c1824dba9142e")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

# include<bits/stdc++.h>
using namespace std;
void swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int swaps(int arr[],int n){
    int min_index;
    int cnt = 0;
    for (int i = 0; i < n-1; i++)
    {
        min_index = i;
        int c = 0;
        for (int j = i+1; j < n; j++)
        {
            if(arr[j]<arr[min_index]){
                min_index = j;
                c= 1;
            }
        }
        if(c == 1){
            cnt++;
            c = 0;
        }
        swap(&arr[min_index],&arr[i]);
    }
    return cnt;
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;cin>>n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<swaps(arr,n)<<endl;
    }
    return 0;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488f53b1afa55f38fed74d")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488f8db1afa55f38fed74e")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488fb6b1afa55f38fed74f")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a488fe0b1afa55f38fed750")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a489006b1afa55f38fed751")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5d88852cffddab5e789a0efd")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

    # include<bits/stdc++.h>
using namespace std;
int InsertionSort(int *A,int n){
    int cnt = 0;
    int key,j;
    for (int i = 1; i <= n-1; i++)
    {
        key = A[i];
        j = i-1;
        int in = 0;
        while (j>=0 && A[j]>key)
        {
            A[j+1] = A[j];
            j--;
            cnt++;
            in = 1;
        }
        if(in == 1){
            cnt++;
            in = 0;
        }
        A[j+1] = key;
    }
    return cnt;
}
int main(){
    int t;
    cin>>t;
    while (t--)
    {
        int n;
        cin>>n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        cout<<InsertionSort(arr,n)<<endl;
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c27689e1bc7780800776e36")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* This function picks an element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) 
   to left of pivot and all greater elements to right of pivot */
void swap(int* a, int* b)    
{
  int t = *a;
  *a = *b;
  *b = t;
}
int partition (int array[], int low, int high) {
  int pivot = array[high];
    int i = low - 1;
    int j;
    for ( j = low; j <= high-1; j++)
    {
            if(array[j] <= pivot){
                i++;
                swap(&array[i],&array[j]);
            }
    }
    swap(&array[i + 1], &array[high]);
    return (i + 1);
}
/* low is for left index and high is right index of the sub-array of arr to be sorted */
void quickSort(int array[], int low, int high) {
  if (low < high)
  {
    int pivot_index;
    pivot_index = partition(array, low, high);
    quickSort(array, low, pivot_index - 1);
    quickSort(array, pivot_index + 1, high);
  }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c2767981bc7780800776e11")#link
t = driver.find_element_by_class_name("CodeMirror-code")
t.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] and Second subarray is arr[m+1..r] 
void merge(int array[], int l, int m, int r) {
  int i,j,k,B[r+1];
    i = l;
    j = m + 1;
    k = l;
    while (i<=m && j<=r)
    {
        if(array[i] < array[j]){
            B[k] = array[i];
            i++;
            k++;
        }
        else{
            B[k] = array[j];
            j++;
            k++;
        }
    }
    while (i <= m)
    {
        B[k] = array[i];
        k++;
        i++;
    }
    while (j <= r)
    {
        B[k] = array[j];
        k++;
        j++;
    }
    for (int i = l; i <= r ; i++)
    {
        array[i] = B[i];
    }
}
/* l is for left index and r is right index of the sub-array of arr to be sorted */
void mergeSort(int array[], int l, int r) {
   int mid;
    if(l<r){
        mid = (l+r)/2;
        mergeSort(array,l,mid);
        mergeSort(array,mid+1,r);
        merge(array,l,mid,r);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

###################### Binary Tree ############################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ea3ca0bdb04eb16c4a15")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eac1a0bdb04eb16c4a18")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eb7ea0bdb04eb16c4a26")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ebe4a0bdb04eb16c4a2c")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c6b36ce59546fd7abfdad")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
/* struct Node {
  int data;
  struct Node *left, *right;
};						
The above structure is used for tree node and the function below is also provided to build a new node with given data. 
struct Node* newNode(int data);
*/
struct Node * createBT(int arr[],Node *root,int i,int n){
    if(i<n){
        Node *temp = newNode(arr[i]);
        root = temp;
        root->left = createBT(arr,root->left,2*i+1,n);
        root->right = createBT(arr,root->right,2*i+2,n);
    }
    return root;
}
struct Node* buildTree(int t[], int n){
    int i = 0;
    Node *root = createBT(t,root,i,n);
    return root;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a75d71da0bdb04eb16c3f35")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c6e1cce59546fd7abfdc6")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

   /* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node.
*/
# include<queue>
void printLevelWise(struct Node* root){
  	if (root == NULL){ 
        return;
    }
    queue<Node *> q;
    q.push(root);
    while (q.empty() == false)
    {
        int nodeCount = q.size();
        while (nodeCount>0)
        {
            Node *node = q.front();
            cout<<node->data;
          	if(nodeCount>1){
              cout<<" ";
            }
            q.pop();
            if(node->left != NULL){
                q.push(node->left);
            }
            if(node->right != NULL){
                q.push(node->right);
            }
            nodeCount--;
        }
        cout<<endl;
    }
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c723c9fedba282eab5021")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node.
*/
int height(Node *root){
    if(root == NULL){
        return 0;
    }
    else{
        int left_height = height(root->left);
        int right_height = height(root->right);
        return max(left_height,right_height)+1;
    }
}
void printGivenLevel(struct Node* root, int level)
{
    if (root == NULL)
        return;
    if (level == 1)
        printf("%d ", root->data);
    else if (level > 1)
    {
        printGivenLevel(root->left, level-1);
        printGivenLevel(root->right, level-1);
    }
}
void printOdd(struct Node* root)
{
	 int h = height(root);
	for (int i = 1; i <= h; i+=2)
	{
		printGivenLevel(root,i);
	}
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c767fd287a634f8535300")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""
/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node. */
void printInorder(struct Node* root)
{
	if(root != NULL){
        printInorder(root->left);
        cout<<root->data<<" ";
        printInorder(root->right);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c77ecd287a634f853530e")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node.
*/
void inorder(Node* root){
  if(root != NULL){
      inorder(root->left);
      printf("%d ",root->data);
      inorder(root->right);
  }
}
void preorder(Node* root){
  if(root != NULL){
      printf("%d ",root->data);
      preorder(root->left);
      preorder(root->right);
  }
}
void postorder(Node* root){
  if(root != NULL){
        postorder(root->left);
        postorder(root->right);
        printf("%d ",root->data);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7c794fd287a634f8535319")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node and the function below is also provided to build a new node with given data. 
struct Node* newNode(int data);
*/
int search(int arr[], int strt, int end, int value)
{
    int i;
    for (i = strt; i <= end; i++) {
        if (arr[i] == value)
            break;
    }
    return i;
}
Node *buildUtil(int in[],int post[],int inStrt,int inEnd,int *pIndex){
	if(inStrt > inEnd){
		return NULL;
	}
	Node *node = newNode(post[*pIndex]);
	(*pIndex)--;
	if(inStrt == inEnd){
		return node;
	}
	int inIndex = search(in ,  inStrt , inEnd , node->data);
	node->right = buildUtil(in, post, inIndex + 1, inEnd, pIndex);
    node->left = buildUtil(in, post, inStrt, inIndex - 1, pIndex);
    return node;
}
Node* buildTree(int in[], int post[], int N){
	int pIndex = N - 1;
	return buildUtil(in , post , 0 , N-1 , &pIndex);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7da2cad287a634f8535a33")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node. */
int countLeafs(struct Node* root) 
{
	if (root == NULL)
    {
        return 0;
    }
    if (root->left == NULL && root->right == NULL)
    {
        return 1;
    }
    return countLeafs(root->left) + countLeafs(root->right);
}
int countNonLeafs(struct Node* root) 
{
	if(root == NULL || (root->left == NULL && root->right == NULL)){
        return 0;
    }
    return 1 + countNonLeafs(root->left) + countNonLeafs(root->right);
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7da375d287a634f8535a48")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node. */
void printArray(int ints[], int len)
{
	int i;
	for (i = 0; i < len; i++)
	{
		cout << ints[i] << " ";
	}
}
int x = 0;
void printPathsRecur(Node* node, int path[], int pathLen)
{
	if (node == NULL) return;
	path[pathLen] = node->data;
	pathLen++;
	if (node->left == NULL && node->right == NULL)
	{
      	x++;
		printArray(path, pathLen);
        cout<<(pathLen-1)<<endl;
	}
	else
	{
		printPathsRecur(node->left, path, pathLen);
		printPathsRecur(node->right, path, pathLen);
	}
}
void printAllPaths(Node* root) {
  	int path[1000];
	printPathsRecur(root, path, 0);
  if(root != NULL){
    cout<<x;
  }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7da3ffd287a634f8535a63")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node and the function below is also provided to build a new node with given data. 
struct Node* newNode(int data);
*/
# include<queue>
Node * nextRight(Node *root ,int k){
    if(root == NULL){
        return 0;
    }
    queue<Node *> qn;
    queue<int> ql;
    int level = 0;
    qn.push(root);
    ql.push(level);
    while (qn.size())
    {
        Node *node = qn.front();
        level = ql.front();
        qn.pop();
        ql.pop();
        if(node->data == k){
            if(ql.size() == 0 || ql.front() != level){
                return NULL;
            }
            return qn.front();
        }
        if(node->left != NULL){
            qn.push(node->left);
            ql.push(level+1);
        }
        if(node->right != NULL){
            qn.push(node->right);
            ql.push(level+1);
        }
    }
    return NULL;
}
int findRightSibling(struct Node* root, int key){
  Node *nr = nextRight(root,key);
    if(nr != NULL){
        return nr->data;
    }
    return -1;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

###################### Binary Search Tree ############################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ec53a0bdb04eb16c4a34")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eca4a0bdb04eb16c4a35")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ed70a0bdb04eb16c4a4a")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76eda4a0bdb04eb16c4a4e")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76edc8a0bdb04eb16c4a4f")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ee36a0bdb04eb16c4a61")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a76ee68a0bdb04eb16c4a62")#link
driver.find_element_by_id("txtOutput0").send_keys("3")
driver.find_element_by_id("txtOutput1").send_keys("3")
driver.find_element_by_id("txtOutput2").send_keys("2")
driver.find_element_by_id("txtOutput3").send_keys("5")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)
driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dae0ad287a634f8535d3a")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  struct Node *left, *right;
};
The above structure is used for tree node. */
int isBinarySearchTree(struct Node* t1){
 	static struct Node *prev = NULL;
    if(t1 != NULL){
        if(!isBinarySearchTree(t1->left)){
            return 0;
        }
        if(prev != NULL && t1->data <= prev->data){
            return 0;
        }
        prev = t1;
        return isBinarySearchTree(t1->right);
    }
    else{
        return 1;
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7daefad287a634f8535d43")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

/* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node. */
# include<bits/stdc++.h>
int x = 0;
int arr[100];
void makeArray(Node *t1,int k){
    if(t1 != NULL){
        arr[x] = t1->data;
        x++;
        makeArray(t1->left,k);
        makeArray(t1->right,k);
    }
}
int kSmallest(Node* t1, int k){
   makeArray(t1,k);
    sort(arr,arr+x); 
    int y = arr[k-1];
    return y;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7db00bd287a634f8535dee")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

    /* struct Node
{
  int data;
  Node *left, *right;
};
The above structure is used for tree node and also one function to create a new node as below is provided. 
Node* newNode(int data); 	*/
struct Node * insert(Node *root,int key){
    if(root == NULL){
        Node *temp = newNode(key);
        return temp;
    }
    if(key < root->data){
        root->left = insert(root->left,key);
    }
    else if(key > root->data){
        root->right = insert(root->right,key);
    }
    return root;
}
Node* buildSearchTree(int t[], int n){
  if(n == 0){
    return NULL;
  }
    Node* root = newNode(t[0]);
    for (int i = 1; i < n; i++)
    {
        insert(root,t[i]);
    }
    return(root);
}

 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

############################# Heap #############################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dc881d287a634f8535ffe")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dc8b8d287a634f8536005")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcac7d287a634f8536016")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcb4bd287a634f8536017")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcb9dd287a634f8536018")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcbd9d287a634f8536019")#link
driver.find_element_by_id("txtOutput0").send_keys("No")
driver.find_element_by_id("txtOutput1").send_keys("Yes")
driver.find_element_by_id("txtOutput2").send_keys("No")
driver.find_element_by_id("txtOutput3").send_keys("Yes")
driver.find_element_by_id("txtOutput4").send_keys("No")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcc73d287a634f8536020")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7dcd18d287a634f8536021")#link
driver.find_element_by_id("txtOutput0").send_keys("4 5 9 14 10 8 6 12 7")
driver.find_element_by_id("txtOutput1").send_keys("14 10 9 8 5 12 7 6 4")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(3)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7ec9fbd287a634f85366ac")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

void printKLargest(int array[],int n,int k){
    sort(array , array + n);
    for (int i = n-1; i > n-1-k; i--)
    {
      cout<<array[i];
      if(i > (n-k )){
        cout<<" "; 
      }
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7eca50d287a634f85366af")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

void maxHeapify(int arr[] , int i , int n){
    int l = (2*i) + 1;
    int r = (2*i) + 2;
    int largest = i;
    if(l<n && arr[l] > arr[i]){
        largest = l;
    }
    if(r<n && arr[r] > arr[largest]){
        largest = r;
    }
    if(largest != i){
        swap(arr[i] , arr[largest]);
        maxHeapify(arr , largest , n);
    }
}
void modifyMintoMax(int a[], int n){
  	for (int i = (n-2)/2; i >= 0; --i)
    {
        maxHeapify(a , i , n);
    }
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7eca9bd287a634f85366b2")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int isMaxHeap(int array[], int n){
  for (int i = 0; i <= (n-2)/2; i++)
  {
      if(array[2*i+1] >  array[i]){
          return false;
      }
      if(2*i+2 < n && array[2*i+2] > array[i]){
        return false;
      }
  }
  return true;
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5a7ecaecd287a634f85366b5")#link
t = driver.find_elements_by_class_name("CodeMirror-code")
t[1].click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyperclip.copy("""

int connectCost(int lengths[], int n){
  priority_queue<int ,vector<int> , greater<int>> pq;
  for (int i = 0; i < n; i++)
  {
    pq.push(lengths[i]);
  }
  int sum = 0;
  while (pq.size() != 1)
  {
    int x =  pq.top();
    pq.pop();
    int y =  pq.top();
    pq.pop();
    sum += (x+y);
    pq.push(x+y);
  }
	return sum;	
}
   
 """)
pyautogui.hotkey('ctrl', 'v')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeProgram"))).click()#Submit Button
time.sleep(2)

####################### Graph ############################

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c755f719d2de26a8b769243")#link
driver.find_element_by_id("chkOpt3").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7561679d2de26a8b769245")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7565239d2de26a8b769266")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7565989d2de26a8b769267")#link
driver.find_element_by_id("chkOpt1").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c7566099d2de26a8b769268")#link
driver.find_element_by_id("chkOpt2").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)

driver.get("https://codequotient.com/attempt/attemptquestion/60d991baccde02f820596293/5c75671b9d2de26a8b769269")#link
driver.find_element_by_id("chkOpt4").click()#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "executeMCQ"))).click()#Submit Button
time.sleep(2)