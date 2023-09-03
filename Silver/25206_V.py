import sys
input = sys.stdin.readline

def transfer(score):
    if score == "A+":
        return 4.5
    elif score == "A0":
        return 4.0
    elif score == "B+":
        return 3.5
    elif score == "B0":
        return 3.0
    elif score == "C+":
        return 2.5
    elif score == "C0":
        return 2.0
    elif score == "D+":
        return 1.5
    elif score == "D0":
        return 1.0
    elif score == "F":
        return 0
    
scores = list()
while True:
    try:
        info = list(input().split())
        if info[2] != "P":
            info[1] = float(info[1])
            scores.append(info)
    except:
        break

credit = 0.0
avg = 0.0

for i in scores:
    avg += i[1] * transfer(i[2])
    credit += i[1]
print(avg / credit)
