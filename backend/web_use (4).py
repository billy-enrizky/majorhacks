import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from test import retriever

# Using Chrome to access web
driver = webdriver.Chrome()

# Open the website
driver.get('https://www.marquette.edu/explore/choose-your-major/quiz.php')

#wait
time.sleep(7)

# Find button
button = driver.find_element(By.NAME, 'q1')

#Click
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(5)

button = driver.find_element(By.NAME, 'q2')
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'q3')
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'q4')
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'q5')
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'q6')
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'q7')
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'q8')
button.click()
next_button = driver.find_element(By.ID, 'next')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'q9')
button.click()
next_button = driver.find_element(By.ID, 'submit')
next_button.click()
time.sleep(4)

button = driver.find_element(By.NAME, 'qProblemSolver')
button.click()
next_button = driver.find_element(By.ID, 'submit')
next_button.click()
time.sleep(4)


html = driver.page_source

import requests
from bs4 import BeautifulSoup


# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Find the first major
first_major = soup.find_all('li')[0].a.text

# Print the text content of each li element in each unordered list
print(first_major)

# Find all li tags containing a tag with the desired href attribute
li_tags = soup.find_all('li')

# Extract the text content of the a tag within each li tag
majors = [li_tag.a.text for li_tag in li_tags]


# Open the website
driver.get('https://www.umultirank.org/best-university-for-me/subject')
Engineering = []
#wait
time.sleep(15)

# Find button
button = driver.find_element(By.NAME, 'level')
time.sleep(10)
#Click
button.click()

# Extract available majors

url = "https://www.umultirank.org/best-university-for-me/subject"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
avail_majors = []

for major in soup.select('input[name="subject"]'):
    avail_majors.append(major.parent.text.strip())

avail_majors=avail_majors[:-1]

# Choose the best major from majors that exist in available major
first_list = majors
second_list = avail_majors


best_match = None
max_similarity = -1

for major1 in first_list:
    for major2 in second_list:
        similarity = len(set(major1.lower().split()).intersection(major2.\
                                                                  lower().\
                                                                  split()))
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = major2

Engineering = ['Chemical Engineering', 'Civil Engineering', 'Electrical Engineering', 'Environmental Engineering', 'Materials Engineering', 'Mechanical Engineering', 'Production/Industrial Engineering']

Mathematics_Sciences = ['Agriculture', 'Biology', 'Chemistry', 'Computer Science', 'Earth Science', 'Mathematics', 'Physics']

Social_Sciences = ['Business studies', 'Economics', 'Education', 'Geography', 'History', 'International Law', 'Linguistics', 'Political Science', 'Social Work', 'Sociology']

Health = ['Dentistry', 'Medicine', 'Nursing', 'Pharmacy / Pharmacology', 'Psychology', 'Veterinary Science']

subject_area =""

if best_match in Engineering:
    subject_area = "#subject_over_1"
elif best_match in Mathematics_Sciences:
    subject_area = "#subject_over_2"
elif best_match in Social_Sciences:
    subject_area = "#subject_over_3"
else:
    subject_area = "#subject_over_4"


element = driver.find_element(By.XPATH, f'//a[@href="{subject_area}"]')


action = ActionChains(driver)
action.move_to_element(element).click().perform()

# find the label element containing the best_major text
label_element = driver.find_element(By.XPATH, f"//label[contains(text(), '{best_match}')]")


# element = driver.find_element(By.ID, 'subject_50')


# click the label element
# action = ActionChains(driver)
# action.move_to_element(element).click().perform()

element = driver.find_element(By.XPATH, '//input[@value="Next"]')
action = ActionChains(driver)
action.move_to_element(element).click().perform()
time.sleep(4)

element = driver.find_element(By.XPATH, '//input[@value="Next"]')
action = ActionChains(driver)
action.move_to_element(element).click().perform()
time.sleep(4)

element = driver.find_element(By.XPATH, '//input[@value="Next"]')
action = ActionChains(driver)
action.move_to_element(element).click().perform()
time.sleep(4)
