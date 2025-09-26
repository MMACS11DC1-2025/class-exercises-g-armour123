responses = open("responses.csv")
for response in responses:
    if "" in response.lower():
        print(response)