import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["value1", "value2", "value3"]) #name of the value to be stored

webpage = requests.get("") #web page link
soup = BeautifulSoup(webpage.content, "html.parser")
container = soup.select_one("") #the location of the tag containing the desired value

for con in container:
    value1 = container.select_one("") #The position of the desired value among the values in the container
    value2 = container.select_one("") #The position of the desired value among the values in the container
    value3 = container.select_one("") #The position of the desired value among the values in the container
    
    sheet.append([value1, value2, value3])


wb.save("File.xlsx")
