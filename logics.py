
try:
  i=0
  while i<5 :
    state_ = str(raw_input("T or F"))
    print(state_ + " ")

    if state_ == "T" :
      state = True
      print(state)
      i+=1
      print("State is {} and you have {} turns to go".format(state, 5-i))
    
    elif state_ == "F" and i>0 :
      state = False
      print(state)
      i-=1
      print("State is {} and you have {} turns to go".format(state, 5-i))

    else:
      print("Try again")

finally:
  print("Done")
