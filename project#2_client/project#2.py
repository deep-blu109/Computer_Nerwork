import http.client

host = input('host : ')
port = int(input('port : '))
conn = http.client.HTTPConnection(host,port)

while(1):
    req = int(input("Command : "))

    if(req == 1):
        url = input("URL : ")
        NotHeader = int(input("header? : "))
        if(NotHeader == 0):
            conn.request("GET", url)
        elif(NotHeader == 1):
            header = {"User-Agent" : "2017047538/DEOKKWANYANG/WebClient/ComNet", "Content-type" : input("Content-type : ")}
            conn.request("GET", url, None, header)

        response = conn.getresponse()
        print(response.status, response.reason)

        result = response.read()

        print(result)
    
    elif(req == 2):
        url = input("URL : ")
        data = input("data : ")
        NotHeader = int(input("header? : "))
        if(NotHeader == 0):
            if(data == 'none'):
                conn.request("POST", url, None)
            else:
                conn.request("POST", url, data)
        else:    
            header = {"User-Agent" : "2017047538/DEOKKWANYANG/WebClient/ComNet", "Content-type" : input("Content-type : ")}
            if(data == 'none'):
                conn.request("POST", url, None, header)
            else:
                conn.request("POST", url, data, header)

        response = conn.getresponse()
        print(response.status, response.reason)

        result = response.read()

        print(result)
    
    elif(req == 0):
       break
