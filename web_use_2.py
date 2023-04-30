import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import re
import requests
from bs4 import BeautifulSoup
from test import retriever_2


Engineering = ['Chemical Engineering', 'Civil Engineering', 'Electrical Engineering', 'Environmental Engineering', 'Materials Engineering', 'Mechanical Engineering', 'Production/Industrial Engineering']

Mathematics_Sciences = ['Agriculture', 'Biology', 'Chemistry', 'Computer Science', 'Earth Science', 'Mathematics', 'Physics']

Social_Sciences = ['Business studies', 'Economics', 'Education', 'Geography', 'History', 'International Law', 'Linguistics', 'Political Science', 'Social Work', 'Sociology']

Health = ['Dentistry', 'Medicine', 'Nursing', 'Pharmacy / Pharmacology', 'Psychology', 'Veterinary Science']

# Using Chrome to access web
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver', options=chrome_options)


def fc(retriever_2: list, retriever_1: list) -> list:
    best_match = "Biology"
    subject_area = ""

    if best_match in Engineering:
        subject_area = "#subject_over_1"
    elif best_match in Mathematics_Sciences:
        subject_area = "#subject_over_2"
    elif best_match in Social_Sciences:
        subject_area = "#subject_over_3"
    else:
        subject_area = "#subject_over_4"

    label_text = retriever_2[0]
    # button = driver.find_element(By.XPATH, '//label[contains(text(), "{}")]/input'.format(label_text))

    # Click the radio button
    # button.click()
    # button = driver.find_element(By.XPATH, f'//a[@href="{subject_area}"]')
    # button.click()

    time.sleep(4)
    # find the label element containing the best_major text

    # button = driver.find_element(By.XPATH, '//label[contains(text(), "{}")]/input'.format(best_match))
    time.sleep(4)
    # button.click()

    # element = driver.find_element(By.XPATH, '//input[@value="Next"]')
    action = ActionChains(driver)
    # action.move_to_element(element).click().perform()
    time.sleep(4)

    Africa= ['All Country', 'Algeria', 'Angola', 'Cameroon', 'Cape Verde', 'Chad', 'Democratic Republic of the Congo', 'Egypt', 'Ethiopia', 'Ghana', 'Kenya', 'Lesotho', 'Libya', 'Madagascar', 'Malawi', 'Morocco', 'Mozambique', 'Namibia', 'Nigeria', 'Rwanda', 'Senegal', 'Somalia', 'South Africa', 'Sudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia','Zimbabwe']

    Asia=['All Country', 'Afghanistan', 'Armenia', 'Azerbaijan', 'Bangladesh', 'Cambodia', 'China', 'Chinese Taipei', 'Democratic Republic of Timor-Leste', 'Guinea', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Korea Republic Of', 'Kuwait', 'Kyrgyzstan', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'Sri Lanka', 'Syria', 'Thailand', 'United Arab Emirates', 'Uzbekistan', 'Vietnam','Yemen']

    Latin_America= ['All Country', 'Argentina', 'Barbados', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Haiti', 'Jamaica', 'Mexico', 'Panama', 'Peru', 'Puerto Rico', 'Trinidad Tobago', 'Uruguay','Venezuela']

    North_America= ['All Country', 'Canada', 'Curaao','United States']

    Europe=['All Country', 'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus Republic of', 'Czech Republic', 'Denmark', 'Estonia', 'Faroe Islands', 'Finland', 'France', 'Georgia', 'Germany', 'Gibraltar', 'Greece', 'Hungary', 'Iceland', 'International', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Montenegro', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'The Netherlands', 'Turkey', 'Ukraine', 'United Kingdom']

    Oceania= ['All Country', 'Australia', 'Fiji', 'New Zealand', 'Papua New Guinea']

    country_match=retriever_2[1]
    continent=""

    if country_match in North_America:
        continent = "#region_4"
    elif country_match in Europe:
        continent = "#region_5"
    elif country_match in Oceania:
        continent = "#region_6"
    else:
        continent = "#region_2"

    #time.sleep(4)
    #button = driver.find_element(By.XPATH, f'//a[@href="{continent}"]')
    #button.click()
    #time.sleep(4)

    #button = driver.find_element(By.XPATH, '//label[contains(text(), "{}")]/input'.format(country_match))

    #time.sleep(4)
    #button.click()
    #time.sleep(4)

    # element = driver.find_element(By.XPATH, '//input[@value="Next"]')
    # action = ActionChains(driver)
    # action.move_to_element(element).click().perform()
    time.sleep(4)

    label_text = retriever_2[2]
    #button = driver.find_element(By.XPATH, '//label[contains(text(), "{}")]/input'.format(label_text))
    #button.click()


    # Click the radio button

    # element = driver.find_element(By.XPATH, '//input[@value="Next"]')
    # button.click()
    time.sleep(4)

    from bs4 import BeautifulSoup

    html = '''
    <div class="row just-center Bg noMarg" style="display: flex;">
      <div class="col-sm-9 col-xs-12">
        <div class="row just-center">
          <div class="colum-flex">
            <div class="detail">
              <span>Hong Kong Polytechnic University</span>
              <a href="/study-at/hong-kong-polytechnic-university-rankings/?variant=track&amp;department=16089&amp;field=8">Find out more</a>
            </div>
          </div>
          <div class="colum-flex">
            <div class="detail">
              <span>Huazhong University of Science and Technology</span>
              <a href="/study-at/huazhong-university-of-science-and-technology-rankings/?variant=track&amp;department=16121&amp;field=8">Find out more</a>
            </div>
          </div>
          <div class="colum-flex">
            <div class="detail">
              <span>Tsinghua University</span>
              <a href="/study-at/tsinghua-university-rankings/?variant=track&amp;department=16085&amp;field=8">Find out more</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    '''

    soup = BeautifulSoup(html, 'html.parser')

    universities = []
    for detail in soup.find_all('div', {'class': 'detail'}):
        universities.append(detail.find('span').text)
    return universities


