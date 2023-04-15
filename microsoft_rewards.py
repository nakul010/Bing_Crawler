############## Bing crawler ##############

import os
# import shutil
import time
import socket
# import pywintypes
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from faker import Faker

def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False
toast = ToastNotifier()
# toast.show_toast("Rewards", "Microsoft Reward bot is going to run", duration=30)

# os.chdir("D:/Bing_Crawler")
fake = Faker()
test = test_connection()

if test:

    # driver = webdriver.Chrome(executable_path = ".\\Browser drivers\\chromedriver_win32\\chromedriver.exe")
    # driver = webdriver.Edge(executable_path=".\\Browser drivers\\edgedriver_win64\\msedgedriver.exe")

    driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    driver.maximize_window()
    # action = ActionChains(driver)
    # time.sleep(4)
    driver.get("https://rewards.bing.com/pointsbreakdown")
    # print(driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text)
    # print(type(driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text))
    time.sleep(3)
    
    points = 0

    total_pc_search = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text
    # print(total_pc_search[-2:])

    if total_pc_search[-2:] == 30:
        # points = 
        pc_search = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        microsoft_edge_bonus = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        print(pc_search, microsoft_edge_bonus)

        if pc_search == "30" and microsoft_edge_bonus == "3":
            driver.close()
        else:
            points = (33-((int(pc_search))+(int(microsoft_edge_bonus))))//3

    else:
        # print(driver.find_element(By.CSS_SELECTOR, "mee-rewards-counter-animation[from='$ctrl.previousPointsToNextLevel'] span[mee-element-ready='$ctrl.loadCounterAnimation()']"))
        pc_search = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        microsoft_edge_bonus = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
        print(pc_search, microsoft_edge_bonus)
        
        if pc_search == "90" and microsoft_edge_bonus == "12":
            driver.close()
        else:
            points = (102-((int(pc_search))+(int(microsoft_edge_bonus))))//3
    
    print(points)
    
    driver.get("https://www.bing.com/search?q=h&form=QBLH&sp=-1&pq=h&sc=10-1&qs=n&sk=&cvid=3E4543E2BC3B46C480C19004BB7B0D59&ghsh=0&ghacc=0&ghpl=")
    
    time.sleep(3)
    
    for i in range(points):
        print(i+1)
        searchbox = driver.find_element(By.ID, "sb_form_q")
        searchicon = driver.find_element(By.XPATH, "//input[@id='sb_form_go']")
        time.sleep(1)
        searchbox.click()
        searchbox.send_keys(Keys.CONTROL + "a")
        searchbox.send_keys(Keys.BACKSPACE)
        searchbox.send_keys(fake.name())
        searchicon.click()
        time.sleep(1)
        # searchbox.send_keys(Keys.ENTER)
        # searchbox.clear()
        time.sleep(1)
        driver.refresh()
        # time.sleep(1)
        # driver.refresh()
        time.sleep(2)

    # ActionChains(driver).send_keys(Keys.CONTROL, Keys.SHIFT, Keys.DELETE).perform()
    # driver.get("edge://settings/clearBrowserData")
    # time.sleep(5)
    # driver.find_element(By.XPATH, '//*[@id="clear-now"]').click()
    # time.sleep(5)
    # driver.get("edge://history/all")
    # time.sleep(3)

    # for i in range(15):
    # findbyid = DemoFindElementByID()
    # findbyid.locate_by_id_demo()


    # driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    # driver.get("https://www.bing.com/")
    # seacrh = driver.find_element(By.ID, "sb_form_q")
    # seacrh.send_keys("jj")
    # time.sleep(10)
    # for i in arr:
    #     driver.get(i)
    # print(driver.title)

    # driver.get("https://rewards.bing.com/pointsbreakdown")
    # # print(driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text)
    # # print(type(driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text))
    # time.sleep(5)

    # if driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text == "90" and driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b') == "12":
    #     driver.close()
    # else:
    #     driver.close()

    # time.sleep(5)
else:
    exit()
    # print("No Internet")
    