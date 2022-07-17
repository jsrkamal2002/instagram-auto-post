# importing librarys

import subprocess
import os
import shutil
import pyautogui
from selenium import webdriver
from time import sleep

# installing librarys

subprocess.call(['pip', 'install', 'selenium', 'pyautogui'])

# getting currentuser

a=os.environ.get('USERNAME')

# source file

src=input("Enter the source path: ")
dst=r"C:/Users/"+a+"/1.jpg"
shutil.copy(src,dst)
print("File copied successfully")

# getting username and password
username=input("Enter your username: ")
password=input("Enter your password: ")

# driver init

driver = webdriver.Chrome()
"""or
driver = webdriver.Chrome(executable_path=r"path-to-chromedriver.exe")"""

# getting to instagram

driver.get('https://www.instagram.com/')
driver.implicitly_wait(10)

# finding the username and password inputs

username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")


# logging into instagram

username_input.send_keys(username)
password_input.send_keys(password)

# clicking login btn

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(5)

# clicking not now btn

not_now_button = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
not_now_button.click()
sleep(5)
not_now_button2 = driver.find_element_by_xpath("//button[@class='_a9-- _a9_1']")
not_now_button2.click()
sleep(5)

# clicking upload btn

upload_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button")
upload_btn.click()
sleep(5)

# clicking pic btn

pic=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button")
pic.click()
sleep(5)

# giving the pic path

path="1.jpg"
pyautogui.write(path)
sleep(3)
pyautogui.press('enter')
sleep(2)

# no-crop

ori=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button")
ori.click()
sleep(2)

# sharing the post

next=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]")
next.click()
sleep(2)
next2=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button").click()
sleep(2)
next3=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button").click()
sleep(2)
next4=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button").click()
sleep(10)

# closing the driver/browser

driver.close()

# file upload completed notification

print("Uploaded successfully")

# removing the file

os.remove("C:/Users/"+a+"/1.jpg")
print("File removed successfully")

