### Print a welcome message
print("Welcome to East Francia.")
print("The year is 856 A.D.")
print("Louis the German is king and is trying to gain power over West Francia. You are a courtier.")
print("King Louis needs you to deliver a message to King Charles the Bald in West Francia.")
print("You get lost in the woods on the way, do you turn left or right?")

### Prompt user for a choice

pathChoice = input("> ")

if(pathChoice == "right"):
  print("You found a coconut tree but this is against the story. Restart Game.")
elif(pathChoice == "left"):
  print("As you go left, you see a large river with nowhere to go, you see a tunic inside of a large boat.")
  print("Do you steal the tunic? (steal tunic) or do you use the boat to go across the river? (travel)")

  travelChoice = input("> ")

  if(travelChoice == "steal tunic"):
    print("You attempt to steal the tunic, but you fall into the water.")
    print("The rivers are dangerous. You didn't even need the tunic but you took it anyway. It was someone else's tunic. Lesson learned. Restart Game.")
  elif(travelChoice == "travel"):
    print("You made it to the other side of the river.")
    print("There is a dead end if you go left. You must turn right. Will you turn right? Please...")
  

  rightChoice = input("> ")
  
  if(rightChoice == "right"):
   print("As you go right, you see a log cabin.")
   print("Do you want to open the door of the cabin? Yes or No?")
  elif(rightChoice == "left"):
   print("You found a log cabin. You decide not to open the door of the log cabin.")
   print("As you turn around, the river is causing a massive flood.")
   print("If only there was weather warnings back in 856 A.D.")
   print("The cabin is now flooded. Better luck next time.")

  
  cabinChoice = input("> ")

  if(cabinChoice == "yes"):
   print("You enter into the cabin.")
   print("You see a table with chairs with a wine barrel in the corner. You see a dresser. Should you sit down (sit) or open dresser? (open).")
  if(cabinChoice == "no"):
   print("A talking wolf comes to tell you to restart the game. What a terrible choice.")
    
    
  dresserChoice = input("> ")
  
  
  if(dresserChoice == "open"):
    print("You see a bag of coins in the drawer.")
    print("Should you steal the coins? Yes or no?")
  elif(dresserChoice == "sit"):
    print("You eat an apple and then you got a fever.")
    print("You have no energy. Restart Game.")
    
  coinsChoice = input("> ")
  
  if(coinsChoice == "yes"):
    print("Wait until King Louis hears about this. Those coins belonged to one of King Charle's guards.")
    print("You camp out for two weeks until King Louis's guards come to arrest you due to your theft.")
    print("The IRS is now investigating.....Actually, No...wrong time period. Restart Game.")
    
  elif(coinsChoice == "no"):
    print("You choose not to take the coins as you have morals. You do not fall into the temptations of silver.")
    print("What's Happening....Something is happening...")
    print("You open your eyes, it was all a dream.")
    print("King Louis summons you and needs you to deliver a message to King Charles. It's like deja vu all over again.")
    print("One week later, the message is delivered. You don't get a cookie but you get a rejoicing community, Isn't that awesome?")
    print("The End")
    print("Credit to Shaun Halverson for giving me tips on coding for this game.")
    exit()
    
