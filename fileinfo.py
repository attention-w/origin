print("1")

data = [55,63,80,75,69,89,92,91,50,84,86,77,95,81,92,74,60,88,64,71]
#通过规则求解BEST,GOOD,PASS,FAIL，从略
BEST,GOOD,PASS,FAIL = 0,0,0,0
for score in data:
    if score < 60:
        FAIL = FAIL + 1
    elif score < 80:
        PASS = PASS + 1
    elif score < 90:
        GOOD = GOOD + 1
    else:
        BEST = BEST + 1
