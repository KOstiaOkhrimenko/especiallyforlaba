magnitude = float(input())
if magnitude > 0 and magnitude < 2:
    print("micro")
if  (magnitude >2 and magnitude < 3) or magnitude == 2:
    print("very minor")
if (magnitude > 3 and magnitude < 4) or  magnitude == 3:
    print("minor")
if (magnitude > 4 and magnitude < 5) or magnitude == 4:
    print("light")
if (magnitude > 5 and magnitude < 6) or magnitude == 5:
    print("moderate")
if (magnitude > 6 and magnitude < 7) or magnitude == 6:
    print("strong")
if (magnitude > 7 and magnitude < 8) or magnitude == 7:
    print("major")
if (magnitude > 8 and magnitude < 10) or magnitude == 8:
    print("great")
if magnitude > 10:
    print("meteoric")


     
