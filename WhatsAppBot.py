from selenium import webdriver
import pyautogui
import time
from OtherDetails import *

WHATSAPP_WEB_LINK = "https://web.whatsapp.com"
CHROME_DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"

class whatsAppBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=/Users/ashwi/AppData/Local/Google/Chrome/User Data/Default')
        
        options.add_argument('profile-directory=Default')
        
        
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=options)
        
        #self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        print("Bot created.")
        
    def type_word(self,word):
        print("Type function entered.")
        time.sleep(my_sleep_time)
        for i in word:
            pyautogui.press(i)
            
        time.sleep(my_sleep_time)
        pyautogui.press('enter')
        print("Message typed.")
        
    
    def enter_website(self):
        print("Entering website...")
        self.driver.get(WHATSAPP_WEB_LINK)
        
        #Address bar is highlighted due to "options.add_arguement" added.So pressing f6 twice will escape the address bar.
        pyautogui.press('f6', presses=3)
        print("Entered website.")
        
        
        #self.driver.find_element_by_name('rememberMe').click()
        #print("Remember me inputbox unchecked.")
        
        print("Scan the QR coe using your whatsApp mobile app.")
        time.sleep(QR_SCAN_TIME)
        
            
    def message(self,message_choice,my_message,user_name_list):
        if(message_choice):
            time.sleep(my_sleep_time)
            
            new_chat = self.driver.find_element_by_xpath("//*[name()='div'][@aria-label='New chat']")
            
            for user_name in user_name_list:
                new_chat.click()
                print("New chat button clicked. ")
                
                time.sleep(my_sleep_time)
                search_contacts = self.driver.find_element_by_xpath("//*[name()='div'][@class='_2_1wd copyable-text selectable-text']")
                print("Search contacts box found.")
                
                search_contacts.clear()
                print("Cleared.")
                
                search_contacts.click()
                print("Clicked.")
                
                self.type_word(user_name)
                
                message_bar = self.driver.find_element_by_xpath("//*[name()='div'][@class='_2_1wd copyable-text selectable-text']")
                print("Message bar found.")
                
                message_bar.clear()
                message_bar.click()
                print("Message bar clicked.")
                self.type_word(my_message)
                time.sleep(my_sleep_time)
            
    def spam(self,spam_choice,spam_target_list,my_spam_message,spam_count):
        if(spam_choice):
            for user in spam_target_list:
                time.sleep(my_sleep_time)
                
                new_chat = self.driver.find_element_by_xpath("//*[name()='div'][@aria-label='New chat']")
                
                new_chat.click()
                print("New chat button clicked. ")
                
                time.sleep(my_sleep_time)
                search_contacts = self.driver.find_element_by_xpath("//*[name()='div'][@class='_2_1wd copyable-text selectable-text']")
                print("Search contacts box found.")
                
                search_contacts.clear()
                print("Cleared.")
                
                search_contacts.click()
                print("Clicked.")
                
                self.type_word(user)
                
                count = 0
                while(count < spam_count-1):
                    self.type_word(my_spam_message)
                    count += 1
        

    
    def logout(self):
        time.sleep(my_sleep_time)
        self.driver.find_element_by_xpath("//*[name()='div'][@title='Menu']").click()
        time.sleep(my_sleep_time)
        print("Menu button clicked.")
        
        self.driver.find_element_by_xpath("//*[name()='div'][@aria-label='Log out']").click()
        print("Log out division clicked.")
        
    def close_tab(self):
        pyautogui.hotkey("ctrl","w")
        print("Tab closed.")
    
    
#TODO:Birthday wish on time.
bot = whatsAppBot()
bot.enter_website() 

bot.message(message_choice,my_message,user_name_list)
bot.spam(spam_choice,spam_target_list,my_spam_message,spam_count)
 
#bot.logout()  
bot.close_tab()  

bot.driver.quit()
print("Driver exited.")
exit()       