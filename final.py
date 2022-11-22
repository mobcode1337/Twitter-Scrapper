import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
from email import message
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from datetime import datetime,date


def main():
    

    api_id = ''
    api_hash = ''
    
    # receiver user_id and access_hash, use
    #change user id
    user_id = 0
    # set it as default 0
    access_hash = 0
    # your phone number with country code 
    # example +9233333333333
    phone = ''

    #path to chrome web driver
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://twitter.com/login")

    ## credentials
    sleep(3)
    cred = open('credentials.txt','rt')
    context = cred.read()
    context = context.split('\n')

    user_name = context[0]
    user_password = context[1]
    # Setup the log in
    sleep(5)
    username = driver.find_element(By.XPATH,"//input[@name='text']")
    username.send_keys(user_name)
    next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
    next_button.click()

    sleep(3)
    password = driver.find_element(By.XPATH,"//input[@name='password']")
    password.send_keys(user_password)
    log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
    log_in.click()

    sleep(3)
    profile = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/a/div[4]/div')
    profile.click()

    sleep(3)
    follower = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div[2]/div[4]/div[2]/a')
    follower.click()
    sleep(5)
    followers = driver.find_elements(By.XPATH,'//div[@aria-label="Timeline: Followers"]//a[@role="link"]/div/div[@dir="ltr"]/span')

    old_followers = []
    new_followers = []

    filereader = csv.reader(open("followers.csv","r"),delimiter = ",")
    next(filereader) # skipping the column of the csv
    for row in filereader:
        old_followers.append(row[0])

    for i in followers:
        rep = i.text.replace('@','')
        if rep not in old_followers:
            new_followers.append([rep,f'https://twitter.com/{rep}'])


    # updating the old csv to save the new followers to the existing ones.
    with open('followers.csv','r+') as file:
        file.read()
        writer = csv.writer(file)
        writer.writerows(new_followers)
        file.close()

    driver.close()
    

    # Telegram
    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient('session', api_id, api_hash)
    
    # connecting and building the session
    client.connect()
    
    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    if not client.is_user_authorized():
        client.send_code_request(phone)

        # signing in the client
        client.sign_in(phone, input('Enter the code: '))

    try:
        
        # my user_id and access_hash for reference
        receiver = InputPeerUser(user_id, 0)
        today = date.today()
        now = datetime.now()
        day = today.strftime("%b-%d-%Y")
        current_time = now.strftime("%H:%M:%S")
        message = f"New Followers \n{day} {current_time} \n Count : {len(followers)}"
        client.send_message(receiver,message, parse_mode='html')
        if len(followers) != 0:
            for row in new_followers:
                message = f"{row[0]}, {row[1]}"
                client.send_message(receiver,message, parse_mode='html')

    except Exception as e:
        #prints error
        print(e);
    
    # disconnecting the telegram session
    client.disconnect()


if __name__ == "__main__":
    main()