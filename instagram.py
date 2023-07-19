#from instaUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = ""
password = ""
class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
          self.browser.get("https://www.instagram.com/accounts/login/")  
          time.sleep(3)
          usernameInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
          passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

          usernameInput.send_keys(self.username)
          passwordInput.send_keys(self.password)
          passwordInput.send_keys(Keys.ENTER)
          time.sleep(2)

    def getFollowing(self):
         self.browser.get(f"https://www.instagram.com/{self.username}")
         time.sleep(2)  
         followingLink = self.browser.find_element(By.XPATH, "//*[@id='mount_0_0_2o']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")
         followingLink.click()
         time.sleep(2)

         
         dialog = self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] ul")
         followingcount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))
         
         print(f"first count: {followingcount}")

         action = webdriver.ActionChains(self.browser)
         while True:
              dialog.click()
              action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
              time.sleep(2)

              newCount = len(dialog.find_elements(By.CSS_SELECTOR,"li"))

              if followingcount != newCount:
                   followingcount = newCount
                   print(f"second count: {newCount}")
                   time.sleep(1)
              else:
                   break             
              
         
         following = dialog.find_elements(By.CSS_SELECTOR, "li")

         followingList = []
         for user in following:
              link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
              followingList.append(user)
              
         with open("following.txt","w",encoding="UTF-8") as file:
              for item in followingList:
                   file.write(item + "\n")


    def followerUser(self, username):
         self.browser.get("https://www.instagram.com/" + username)
         time.sleep(2)

         follwerButton = self.browser.find_element(By.TAG_NAME, "button")
         if follwerButton.text != "Takiptesin":
              follwerButton.click()
              time.sleep(2)
         else:
              print("Zaten takiptesin")
              
         
    def unFollowUser(self, username):
         self.browser.get("https://www.instagram.com/" + username)
         time.sleep(2)

         followerButton = self.browser.find_element(By.TAG_NAME, "button")
         if followerButton.text == "Takiptesin":
              followerButton.click()
              time.sleep(2)
              self.browser.find_element(By.XPATH, '//button[text()="Takibi Bırak"]').click()
         else:
              print("Zaten takip etmiyorsunuz")



instgrm = Instagram(username,password)
instgrm.signIn()
instgrm.getFollowing()

# list = ["coders.world","kadinbirlider"]

# for user in list:
#      instgrm.followerUser(user)
#      time.sleep(3)
#instgrm.followerUser("coders.world")
#instgrm.unFollowUser("coders.world")