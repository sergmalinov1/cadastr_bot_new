import cv2
#import pyautogui as PG
#import numpy as np
#import imutils
import time
import functions as FN
import os




time.sleep(3)

cad_list = open('cad.txt', 'r')
url_cadaster = "https://e.land.gov.ua/back/cadaster/?cad_num="

col_tabs = 0
max_tabs = 20
for cadastr in cad_list:

    FN.open_page_in_new_tab(url_cadaster+cadastr)
    time.sleep(1)
    col_tabs +=1
    if(col_tabs >=max_tabs): #закрываем лишние вкладки
        time.sleep(3)
        FN.close_tabs(max_tabs)
        col_tabs = 0


unic_key = []
all_data_html = []  # сформировать массив распарсенного хтмл


# формируем список уникальных ключей
def add_unik_key(list_value):
    for data in list_value:
        if(unic_key.count(data.key) == 0):
            unic_key.append(data.key)


dir_name = 'C:\cadastr\download\\'

for root, dirs, files in os.walk(dir_name):
  for file in files:
      if file.endswith(".html"):
        list_value = FN.parser_html(dir_name, file)
        add_unik_key(list_value)
        all_data_html.append(list_value)


FN.generate_excel(all_data_html, unic_key)







cv2.waitKey(0)