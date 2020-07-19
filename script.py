from bs4 import BeautifulSoup
import requests
import urlopen
import re
import json

#### variables for json
email=""
name=""
address=""
number=""
bed=""
bath=""
url="new_lead.html"
## opening html file
fp = open(url)
soup = BeautifulSoup(fp.read(), 'html5lib') 
table = soup.findAll(['a'])

## different regex
pattern_foremail = re.compile("^[a-z0-9](\.?[a-z0-9]){5,}@g(oogle)?mail\.com$")
pattern_forname = re.compile("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
pattern_foraddress= re.compile("^[#.0-9a-zA-Z\s,-]+$")
#pattern_forphone
# mail_list = re.findall(s, fp.read())
#print(mail_list)
i=0
j=0
for row in table:
    t={}
    t['text']=row.text
    t['url']=row['href']
    if(pattern_foremail.match(row.text)):
        email=row.text
    if(pattern_forname.match(row.text)):
        if(i==0):
            name=row.text
        i=i+1
    if(pattern_foraddress.match(row.text)):
        if(j==2):
            number=row.text
        elif(j==4):
            address=row.text
        j=j+1
    if(i>0 and j>4):
        break


pattern = re.compile("Beds+( [0-9])")
table =soup.findAll(['font'],attrs = {'class':'font12'})
k=0
for row in table:
    if(pattern.match(row.text)):
        a=row.text.split()
        for it in a:
            if(it.isdigit()):
                if(k==0):
                    bed=it
                    k=1
                else:
                    bath=it
                    if(k==1):
                        break

####create json here
final_json={"name":name,"email":email,"phone":number,"beds":bed,"baths":bath}
fp=open('output.json','w')
json.dump(final_json,fp)



