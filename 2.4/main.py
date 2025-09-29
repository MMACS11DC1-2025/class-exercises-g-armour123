responses = open("2.4/responses.csv")
for response in responses:
    response = response.split(",")
    if " " in response:
        print(response)