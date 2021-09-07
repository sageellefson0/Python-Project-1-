score = input("Enter Score: ")
scorefl = float(score)   
if scorefl >= 0.9:
    print ("A")
elif scorefl >= 0.8: 
    print("B")
elif scorefl >= 0.7:
     print("C")
elif scorefl >= 0.6:
    print("D")
elif scorefl > 0.6:
    print("F")
else: print("Error, please enter a letter between A-F")