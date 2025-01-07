# dictionaary me key value pari use karte  


# firt step install request ( pip install requests)

import requests


response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#"api.github.com/repos/SHOEBAZ/python-shoeb-pract/pulls"

#print(response)
#print(response.json()) # we get all the output jo hume url search par dikhti hai ye command se aur ye json data ko dictionary me bhi convert kar deta hai

complete_detail = response.json()
#print(complete_detail [0]["id"]) 


for i in range(len(complete_detail)):
    print(complete_detail [i] ["user"]["login"]) 