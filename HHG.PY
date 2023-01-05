class Hoghoogh():
    
    def __init__(self, hour, rate):
        self.hour = hour
        self.rate = rate
pul = Hoghoogh(int(input("please enter hours : ")), 1.5)
if pul.time > 40 :
    salary = (pul.time- 40) * (1.5) + 400
    print("payment will be : " , salary )     
else :
    print ("payment will be : " , pul.time * pul.rate)
    class Hoghoogh()
