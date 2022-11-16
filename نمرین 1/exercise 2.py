hrs  = input("Enter Hours:")
h = float (hrs)
rte = input ("Enter rate per hour")
r = float (rte)
if h <= (40):
    p1= (h*r)
    print (p1)
elif h > 40:
    exthr = (h-40)
    extpay = exthr * 10 * 1.5
    p2 = (40 * 10 ) + float (extpay)
    print (p2)
