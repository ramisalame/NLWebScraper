import time
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import testFile

#Automatically starts chrome 
driver = webdriver.Chrome()
driver.get("https://www.ctvnews.ca/")


#Wait a little for page to load 
time.sleep(6)

print(a)
