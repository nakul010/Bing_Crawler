import os
import sys
# import shutil
import time
import socket
# import pywintypes
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from faker import Faker
import random

delay = random.uniform(2, 10)

def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False

def search():
    searchbox = driver.find_element(By.ID, "sb_form_q")
    searchicon = driver.find_element(By.XPATH, "//input[@id='sb_form_go']")
    time.sleep(delay)
    searchbox.click()
    searchbox.send_keys(Keys.CONTROL + "a")
    searchbox.send_keys(Keys.BACKSPACE)
    searchbox.send_keys(fake.name())
    searchicon.click()
    # searchbox.send_keys(Keys.ENTER)
    # searchbox.clear()
    # driver.refresh()
    time.sleep(delay)

def check_points():
    points = 0

    total_pc_search = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text
    # print(type(total_pc_search[-2:]))              //*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b

    if total_pc_search[-2:] == "30":
        pc_search = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        # microsoft_edge_bonus = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        # print(pc_search, microsoft_edge_bonus)

        # if pc_search == "30" and microsoft_edge_bonus == "3":
        if pc_search == "30":
            driver.quit()
            sys.exit()
        else:
            # points = (33-((int(pc_search))+(int(microsoft_edge_bonus))))//3
            points = (33-((int(pc_search))))//3

    else:
        # print(driver.find_element(By.CSS_SELECTOR, "mee-rewards-counter-animation[from='$ctrl.previousPointsToNextLevel'] span[mee-element-ready='$ctrl.loadCounterAnimation()']"))
        pc_search = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        # microsoft_edge_bonus = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        # print(pc_search, microsoft_edge_bonus)//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b
        
        # if pc_search == "90" and microsoft_edge_bonus == "12":
        if pc_search == "90":
            driver.quit()
            sys.exit()
        else:
            # points = (102-((int(pc_search))+(int(microsoft_edge_bonus))))//3
            points = (102-((int(pc_search))))//3
    
    # if points == 0
    driver.get("https://www.bing.com/search?q=h&form=QBLH&sp=-1&pq=h&sc=10-1&qs=n&sk=&cvid=3E4543E2BC3B46C480C19004BB7B0D59&ghsh=0&ghacc=0&ghpl=")

    # return points, microsoft_edge_bonus, pc_search, microsoft_edge_bonus
    return points, pc_search

# os.chdir("D:/Bing_Crawler")
fake = Faker()
test = test_connection()

# Notification
# toast = ToastNotifier()
# toast.show_toast("Rewards", "Microsoft Reward bot is going to run", duration=30)

if test:

    # driver = webdriver.Chrome(executable_path = ".\Browser drivers\chromedriver_win32\chromedriver.exe") # chrome driver
    driver = webdriver.Edge(executable_path="\Browser drivers\edgedriver_arm64\msedgedriver.exe") # microsoft egde driver

    # driver = webdriver.Edge() # microsoft egde driver
    driver.maximize_window()
    # action = ActionChains(driver)
    # time.sleep(delay)
    try:
        driver.get("https://rewards.bing.com/pointsbreakdown")
    except:
        sys.exit()
    # print(driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text)
    # print(type(driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text))
    # time.sleep(delay)
    
    # points, microsoft_edge_bonus, pc_search, microsoft_edge_bonus = check_points()
    # print(points, microsoft_edge_bonus, pc_search, microsoft_edge_bonus)
    points, pc_search = check_points()
    print(points, pc_search)
    time.sleep(delay)
    for i in range(points):
        element = driver.find_element(By.XPATH, '//*[@id="langChangeAnchor"]')
        ActionChains(driver).move_to_element(element).perform()
        print(i+1)
        search()

else:
    print("No Internet")
    # toast.show_toast("Rewards", "Microsoft Reward bot is going to run", duration=30)
    sys.exit()
    