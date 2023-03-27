#pip install easyocr
import easyocr
import regex as re
reader = easyocr.Reader(['ch_sim','en'])

result1 = reader.readtext('1.png',detail=0)
print(result1)

result2 = reader.readtext('2.png',detail=0)
print(result2)

result3 = reader.readtext('3.png',detail=0)
print(result3)

result4 = reader.readtext('4.png',detail=0)
print(result4)

result5 = reader.readtext('5.png',detail=0)
print(result5)

def phno(img):
  num = []
  for i in img:
    if re.findall(r'^[+]',i):
      num.append(i)
    elif(re.findall(r'^\d{3}-\d{3}-\d{4}$',i)):
      num.append(i)
  return num

def email(img):
  for i in img:
    if(re.findall(r'[\w\.-]+@[\w\.-]+',i)):
      return i

def website(img):
  website = ""
  for i in img:
    if re.match(r'^WWW(?=.*\.com)', i):
      website = i
    elif re.match(r'^\w+\.com$', i):
      website = ('WWW.'+i)
  if len(website) ==0:
    website = "Not Available"
  else:
    return website

def name(img):
  for i in img:
    return i

def designation(img):
  for i in img:
    return img[1]

def address(img):
  for i in img:
    if(re.findall(r'^123+\s[\w\.-]+',i)):
      return i[0:10]

def domain(img):
  for i in img[-1]:
    if len(img[-1])> 5:
      return img[-1]
    else:
      return img[-2]

def district(img):
  for i in img:
    if(re.search(r'^123+\s',i)):
      if len(i[10:20])> 6:
        return i[11:20].replace(",","")
    elif (re.search(r'\bErode\b',i)):
      return i.replace(";","")
  return "Not Available"

def pincode(img):
    pincode = None
    for i in img:
        pincode_match = re.search(r'(\d{6})|\b(\d{3}\s*\d{3})\b', i)
        if pincode_match:
            pincode = pincode_match.group(0).replace(' ', '')
    return pincode

def state(img): 
    for i in img:
        match = re.search(r'TamilNadu', i)
        if match:
            return match.group()
    return "Not found"

#create a dictionary with all the data
def data(img):
  data = {}
  data['Name'] = name(img)
  data['Designation'] = designation(img)
  data['Domain'] = domain(img)
  data['Contact'] = phno(img)
  data['E-mail'] = email(img)
  data['Website'] = website(img)
  data['Address'] = address(img)
  data['District'] = district(img)
  data['State'] = state(img)
  data['Pincode'] = pincode(img)
  return data

df_1 = pd.DataFrame(data(result1))

df_2 = pd.DataFrame(data(result2))
df_3 = pd.DataFrame(data(result3))
df_4 = pd.DataFrame(data(result4))
df_5 = pd.DataFrame(data(result5))

df = pd.concat([df_1,df_2,df_3,df_4,df_5])

df.to_csv('Extracted_data.csv',index=False)

pd.read_csv('Extracted_data.csv')
