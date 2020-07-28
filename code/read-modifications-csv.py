
import csv
import os.path
import time
from collections import Counter

filelist = "file-list.txt"

def count_frequency (txtfile,csvfile):
  with open (txtfile) as f:
    content = f.read()

  ltrs = [c for c in content.lower() if "a" <= c <= "z"]
  cnt = Counter (ltrs)
  mc = cnt.most_common()
  total = sum ([x [1] for x in mc])
  rows = [[k, v] for (k,v) in mc]

  with open (csvfile, 'w') as f:
    writer = csv.writer (f,delimiter='\t')
    writer.writerows (rows)

  print ("Read", txtfile)
  print ("Wrote", csvfile)

def mod_date (filename):
  try:
    modTimesinceEpoc = os.path.getmtime (filename)
    modificationTime = time.strftime ('%Y-%m-%d %H:%M:%S', 
      time.localtime(modTimesinceEpoc))
    result = modificationTime
  except FileNotFoundError:
    result = ""
  return result

def check_mod (txtfile,csvfile):
  txt_mod = mod_date (txtfile)
  csv_mod = mod_date (csvfile)
  if csv_mod < txt_mod: count_frequency (txtfile,csvfile)

with open (filelist) as f:
  reader = csv.reader (f,delimiter='\t')
  for row in reader:
    txtfile = row [0]
    csvfile = f"freq-{txtfile}" [:-4] + ".csv"
    if os.path.isfile (txtfile):
      check_mod (txtfile,csvfile)
    else:
      print (f"File \"{txtfile}\" does not exist. "
             f"Check the file list \"{filelist}\"!")


