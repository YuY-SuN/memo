#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys

option  = Options()
option.add_argument("--incognito")
service = Service(executable_path=sys.argv[1])
driver  = webdriver.Chrome(service=service, options=option)
driver.get("${URL}")



driver.quit()
