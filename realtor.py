__author__ = 'DaddyQing'

#imports part
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class realtor(object):
  """
  simple wrapper for all the webpages availabe under on search, and price history part
