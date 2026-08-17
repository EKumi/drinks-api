import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")


# built something that gives me unanswered stack overflow questions with fewer questions to answer

'''
for data in response.json()['items']:
    if data ['answer_count'] == 0:
        print (data['title'])
        print (data ['link'])
        print ()

    else:
        print ('Question doesn\'t meet requirements')
    print ()

'''

# How do I call the items in tags since tag is also an object or even iwner



# Building my own API


