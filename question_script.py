import requests
import random
#In this file I find out how many questions are available from the API
#Last Check: 2:34am - EET 05/01/2023
#Questions Available at Last Check: 124

response = requests.get(f"https://opentdb.com/api.php?amount={50}&category=18&type=multiple")
while response.status_code != 200:
    response = requests.get(f"https://opentdb.com/api.php?amount={50}&category=18&type=multiple")
            
response = response.json()
questions = response['results']
while len(questions) < (150):
    response = requests.get(f"https://opentdb.com/api.php?amount={50}&category=18&type=multiple")
    if response.status_code == 200:
        response = response.json()
        response = response['results']
            
        for i in response:
            if i not in questions:
                questions.append(i)
    print(len(questions))
        
if len(questions) > (150): #this will most certainly happen but it is random
    diff = len(questions) - (150)
    for _ in range(diff):
        ind = random.randrange(len(questions))
        questions.pop(ind)
        print(len(questions))