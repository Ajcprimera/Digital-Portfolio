import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class webscrapping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://www.youtube.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_youtube(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'search_query')
        search_field.clear()
        driver.minimize_window()
        user = input('What song or video are you looking?=> ')
        driver.maximize_window()
        search_field.send_keys(user)
        search_field.submit()
        list_video = []
        
        for i in range(5):
            videos_name = driver.find_element(By.XPATH, f'//*[@id="contents"]/ytd-video-renderer[{i+1}]').find_element(By.ID, 'title-wrapper').text
            list_video.append(videos_name)
        

        flag = 1
        print('These are the options: ')
        for j in list_video:
            print(f'{flag}) {j}')
            flag += 1        
        driver.minimize_window()
        while True:
            try:
                user_play = int(input('What video or music would you like to play?(1 to 5): '))
                break
            except ValueError:
                print('You introduce a not integer value, try again: ')

        for j in range(user_play):
            if user_play == 1 or user_play == 2 or user_play == 3 or user_play == 4 or user_play == 5:
                driver.maximize_window()
                video_s = driver.find_element(By.XPATH, f'//*[@id="contents"]/ytd-video-renderer[{j+1}]').find_element(By.ID, 'title-wrapper')
                video_s.click()
                autoreplay = driver.find_element(By.CLASS_NAME, 'ytp-autonav-toggle-button')
                autoreplay.click()
                try:
                    WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,"//button[@aria-label='Replay']")))
                    break 
                except:
                    pass
        

        
    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)

    