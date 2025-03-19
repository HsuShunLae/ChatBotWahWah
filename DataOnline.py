
import time
import requests
from bs4 import BeautifulSoup
import keyboard
import sys

# classes = ["df_da", "hgKElc", "UQt4rd", "zCubwf", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
#            "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table", "b1hJbf",
#            "dDoNo ikb4Bb gsrt", "sXLaOe", "LWkfKe",  "qv3Wpe","kno-rdesc" ]#

classes = ["rwrl rwrl_pri rwrl_padref", "rwrl rwrl_sec rwrl_padref rwrl_fontexp rwrl_bchl", "rwrl rwrl_pri rwrl_padref rwrl_fontexp rwrl_bchl", 
"rd_card_ml", "b_focusTextSmall curr_totxt", "wtr_condition wtr_condition2", "lyrics", "carousel-content", "fin_quotePrice", "b_focusTextSmall", "tta_outtxt", "dc_pd", "qna_daac", "l_ecrd_wptfcts"]

# useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',  
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'


def Online_Scraper(query, PRINT=False):
    query = query.replace(" + ", " plus ")
    query = query.replace(" - ", " minus ")
    # URL = "https://www.google.com/search?q=" + query
    URL = "https://www.bing.com/search?pglt=41&q=" + query
    headers = {'User-Agent': useragent}

    try:
        page = requests.get(URL, headers=headers, timeout=40)
        time.sleep(5)  # Add a delay of 5 seconds
        soup = BeautifulSoup(page.content, 'html.parser')

        for i in classes:
            try:
                result = soup.find(class_=i).get_text()
                if PRINT:
                    print("by class ", i)
                return result
            except AttributeError:
                pass

    except requests.exceptions.Timeout:
        print("The request timed out. Check your internet connection and try again.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    # return "no idea about that"
    return None

    
