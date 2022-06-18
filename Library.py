import requests
import json
import jsonpath
import openpyxl

class Common:
   
  def __init__(self):
    global vk
    global sh
    vk = openpyxl.load_workbook(FileNamePath)
    sh = vk[SheetName]
      
  def fetch_row_count(self, FileNamePath, SheetName):
    max_rows = sh.max_row
    return max_rows
  
  
  def fetch_column_count(self, FileNamePath,SheetName):
    max_columns = sh.max_column
    return max_columns
