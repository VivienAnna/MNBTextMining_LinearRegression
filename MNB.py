import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pickle
import json

all_paragraphs=[]

# Set up the webdriver
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service, options=chrome_options)

# Function to query the text from the website
def GetText(year, driver):
    url='https://www.mnb.hu/monetaris-politika/a-monetaris-tanacs/kozlemenyek/'+str(year)
    headers={
        'User-Agent':"Custom"
    }
    driver.get(url)
    t=driver.page_source

    # Function to click on the next button
    def Next():
        if len(driver.find_elements(By.LINK_TEXT, 'következő'))>0:
            button = driver.find_element(By.LINK_TEXT, 'következő')
            button.click()
            time.sleep(3)
            return False
        else:
            return True

    # Loop through the pages
    length=1
    soup = BeautifulSoup(t, features="html5lib")
    while(length>0):
        soup = BeautifulSoup(t, features="html5lib")
        trs = soup.find_all(class_="news-list-item")
        length=len(trs)
        for element in trs:
            if "Közlemény" in element.contents[3].a.text:
                tmp_list=[]
                print(element.p.text[:-1])
                print(element.contents[3].a["href"][2:])
                time.sleep(3)
                justifiction_req=requests.get("https://"+element.contents[3].a["href"][2:])
                bs = BeautifulSoup(justifiction_req.text, features="html5lib")

                tmp=""
                new_tmp=""
                if(bs.find("p", string="Indoklás")==None and len(bs.find_all("p"))>2):
                    if(bs.find("strong")!=None):
                        if(bs.find_all("strong")[-1].parent.name=="td"):
                            tmp = tmp + bs.find("p").text
                            for p in bs.find("p").next_siblings:
                                if ("MAGYAR NEMZETI BANK" in p.text):
                                    break
                                tmp = tmp + p.text
                        else:
                            for p in bs.find_all("strong")[-1].parent.next_siblings:
                                if ("MAGYAR NEMZETI BANK" in p.text):
                                     break
                                tmp=tmp+p.text
                    else:
                        tmp=tmp+bs.find("p").text
                        for p in bs.find("p").next_siblings:
                            if ("MAGYAR NEMZETI BANK" in p.text):
                                 break
                            tmp = tmp +p.text
                else:
                    if(len(bs.find_all("p"))>2):
                        list = bs.find("p", string="Indoklás").next_siblings
                        for p in list:
                            if ("MAGYAR NEMZETI BANK" in p.text):
                                break
                            tmp= tmp+p.text
                    else:
                        tmp="\n"+"A Monetáris Tanács áttekintette a gazdasági és pénzügyi folyamatokat. Meghirdetett ülésezési rendjének megfelelően nem tárgyalta a jegybanki alapkamatláb megváltoztatását."+"\n"

                print(tmp)
                new_tmp=tmp.strip()
                tmp_list.append(element.p.text[:-1])
                tmp_list.append(new_tmp)
                all_paragraphs.append(tmp_list)

        if Next():
            break
        response=driver.page_source
        t=response


for i in range(2017,2024):
    GetText(i, driver)

# Save the paragraphs to a json, pickle and csv file
print(all_paragraphs)
with open("RawText_MNB/paragraphs.json", "w", encoding="utf-8") as fp:
    json.dump(all_paragraphs, fp)

with open('RawText_MNB/paragraphs.pickle', 'wb') as handle:
    pickle.dump(all_paragraphs, handle, protocol=pickle.HIGHEST_PROTOCOL)

my_df = pd.DataFrame(all_paragraphs)
my_df.to_csv('RawText_MNB/paragraphs.csv', index=False, header=False, encoding='utf-8')
