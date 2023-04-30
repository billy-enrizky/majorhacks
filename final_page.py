import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Using Chrome to access web
def fc(retriever_1) -> str:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

    # Open the website
    driver.get('https://www.marquette.edu/explore/choose-your-major/quiz.php')

    #wait
    time.sleep(7)

    # Find button

    label_text = retriever_1[0]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))

    #Click
    button.click()
    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(5)

    label_text = retriever_1[1]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()

    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[2]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()
    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[3]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()

    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[4]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()

    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[5]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()

    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[6]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()

    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[7]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()

    next_button = driver.find_element(By.ID, 'next')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[8]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()
    next_button = driver.find_element(By.ID, 'submit')
    next_button.click()
    time.sleep(4)

    label_text = retriever_1[9]
    button = driver.find_element(By.XPATH,"//label[contains(text(), '{}')]/input".format(label_text))
    button.click()

    next_button = driver.find_element(By.ID, 'submit')
    next_button.click()
    time.sleep(4)


    html = driver.page_source

    import requests
    from bs4 import BeautifulSoup


    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all li tags containing a tag with the desired href attribute
    li_tags = soup.find_all('li')

    # Extract the text content of the a tag within each li tag
    majors = [li_tag.a.text for li_tag in li_tags]


    # Open the website
    driver.get('https://www.umultirank.org/best-university-for-me/subject')

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
    return best_match
