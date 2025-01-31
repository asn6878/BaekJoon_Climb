def printer(string:str):
    for i in range(0, len(string), 10):
        print(string[i:i+10])

printer(input())