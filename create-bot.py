from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class create_bot:
    def __init__(self):
        print("Iniciando")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        #self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox(executable_path=r"geckodriver")

    def open_sites(self,sheets,anime_site,notion):
        print("Abrindo Sites")
        self.driver.get(sheets)
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.driver.execute_script("window.open('');") 
        self.driver.switch_to.window(self.driver.window_handles[1])        
        self.driver.get(anime_site)

        self.driver.execute_script("window.open('');") 
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get(notion)
        time.sleep(5)
    
    def login_notion(self,email,password):
        print("logando")
        act=ActionChains(self.driver)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/div[3]").click()
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH,'//*[@id="notion-email-input-1"]')
        email_input.send_keys(email)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        password_input = self.driver.find_element(By.XPATH,'//*[@id="notion-password-input-2"]')
        password_input.send_keys(password)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(2)

    def add_anime(self):
        print("comecei a adicionar um anime")
        act=ActionChains(self.driver)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(0.5)
        act.send_keys(Keys.ARROW_DOWN).perform()
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="topSearchText"]').click()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.DELETE).perform()
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(3)
        act.send_keys(Keys.ARROW_DOWN).perform()
        act.send_keys(Keys.ENTER).perform()
        time.sleep(6)

        images = self.driver.find_elements(By.XPATH, "//*[@src]")
        urls = []
        for link in images:
            url = link.get_attribute('src')
            if(url.startswith("https://cdn.myanimelist.net/images/anime/")):
                urls.append(url)

        self.driver.get("https://myanimelist.net")
        time.sleep(1)    

        print("adicionando o cover")
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(1)
        new = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[5]/div[1]")
        act.move_to_element(new).click().perform()
        time.sleep(2)
        add_cover = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/div/div[2]")
        act.move_to_element(add_cover).click().perform()
        time.sleep(2)
        change_cover = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[1]")
        act.move_to_element(change_cover).click().perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/div").click()
        time.sleep(1)
        cover_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/input")
        cover_link.click()
        cover_link.send_keys(urls)
        time.sleep(1)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div").click()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.ENTER).perform()
        
        num = int(1)
        while num < int(14):
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(1)
            act.send_keys(Keys.ARROW_RIGHT).perform()
            time.sleep(0.1)
            act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
            time.sleep(0.25)
            self.driver.switch_to.window(self.driver.window_handles[2])
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[3]/div/div[2]/div").click()
            time.sleep(1)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(0.25)
            act.send_keys(Keys.ENTER).perform()
            time.sleep(0.25)
            act.send_keys(Keys.ESCAPE).perform()
            time.sleep(0.25)
            print("completei o gênero número "+str(num))
            num+=int(1)

        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(0.5)
        act.send_keys(Keys.ARROW_RIGHT).perform()
        time.sleep(0.5)
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        time.sleep(0.5)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[4]/div/div[2]/div").click()
        time.sleep(1)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(1)
        act.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        act.send_keys(Keys.ESCAPE).perform()
        time.sleep(0.5)
        act.send_keys(Keys.ESCAPE).perform()
        time.sleep(0.5)

        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        act.send_keys(Keys.ARROW_RIGHT).perform()
        time.sleep(1)
        act.send_keys(Keys.F2).perform()
        act.send_keys("SIM").perform()
        time.sleep(0.5)
        act.send_keys(Keys.TAB).perform()
        act.send_keys(Keys.HOME).perform()

        print("adicionei mais um anime!!")
        bot.add_anime()

bot = create_bot()
bot.open_sites(google_drive_link,"https://myanimelist.net",notion_link)
bot.login_notion(email,senha)
bot.add_anime()

