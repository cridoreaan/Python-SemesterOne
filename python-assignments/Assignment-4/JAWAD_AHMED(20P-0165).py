#Writing Menu in the file named MENU_FILE
with open("MENU_FILE" , "w") as M:
    M.write("Burgers\nZinger Burger           230/-\nZinger Cheese Burger    260/-\nThames Special Burger   320/-\nBeef Burger             250/-\nTower Burger            320/-\nFish Burger             260/-\nFire Stone Burger       170/-\nCrispy Burger           170/-\nChicken Burger          180/-\nTikka Burger            170/-\nShami Burger            170/-")
    M.write("\nSteaks\nBeef or Chicken |-all steaks served with fries & vegetable\nArizona Steak     650/-\n(Char grilled beef or chicken topped with spicy American sauce)\nMushroom Steak    650/-\n(Tender line Char grilled beef or chicken topped withcreamy mushroom sauce)\nPepper Steak      650/-\n(Tender line beef or chicken medallion grilled topped with pepper corn sauce)\nPolo Tuscany      650/-\n(Char grilled steak topped with chef special sauce and slice cheese)")
STEAKS_DICTIONARY = {}   #This Steaks Dictionary is for storing steaks names and their prices as key,value
STEAKS_PRICES = []       #this list is for All Steaks Prices 
STEAKS_NAMES = []        #This list for Steaks Names
STEAKS = []              #This list includes Steaks with its prices
BURGERS_DICTIONARY = {}  #This Dictionary is for storing all Burgers names and their prices as key,value
BURGERS_PRICE = []       #This is for including all BURGERS Prices
BURGERS_LIST = []        #This list include all Burgers with prices       
STEAKS_LIST = []         #This List include all Steaks with prices
B_Names_L = []           #This list include all Burger Names
with open("MENU_FILE" , "r") as B:         #Oppening "MENU_FILE" in read mode
    for b in range(1 , 13):                        #Taking 12 lines from the file where Burgers names and prices
        BURGERS_LIST.append(B.readline().strip())  #Appending All Burgers,Prices in BURGERS_LIST 
    for s in range(14 , 23):                       #Taking all steaks from line 14,22 where Steaks
        STEAKS_LIST.append((B.readline().strip())) #Appending all Steaks in STEAKS_LIST file
for p in BURGERS_LIST[1:]:             #Skipping 1st line 
    B_Names_L.append(p[:21].strip())   #Appending all Burger names in List and removing spaces 
    BURGERS_PRICE.append(int(p[24:27])) #Appending All prices in the BURGERS_PRICE List
C = -1
while C <= 9:        #Now adding all Burgers Names and Burgers,Prices as key,value
    BURGERS_DICTIONARY[B_Names_L[C + 1]] = BURGERS_PRICE[C + 1]
    C += 1
S = 0
while S <= 6:           #Picking all Steaks Names and prices and Appending in Steaks list
    STEAKS.append(STEAKS_LIST[S + 2])
    S += 2
for s in STEAKS:                      
    STEAKS_PRICES.append((s[18:21]))          #Appending All Steaks Prices in List Names(STEAKS_PRICES)
    STEAKS_NAMES.append((s[:14].strip()))     #Appending All Steaks Names in List Names (STEAKS_NAMES)
S = -1
while S <= 2 :  #Appending all Steaks  Names,Prices in list as key,value
    STEAKS_DICTIONARY[STEAKS_NAMES[S + 1]] = STEAKS_PRICES[S + 1]
    S += 1
if input("You Want to see Menu?Yes or No") == "Yes": #For Showing Menu
    with open("MENU_FILE" , "r") as R:
        print(R.read())
    while input("Burgers OR Steaks?") == "Burgers": #For Showing Burgers
        for a in BURGERS_LIST:
            print(a)
        if input("Want to Choose something from the list?Yes or No") == "Yes": #If User want to select something from the list of Burgers
            BURGER_Name = input('What do you want?')    #Taking input which burger user want
            BURGER_PRICE = BURGERS_DICTIONARY[BURGER_Name] #Which Burger is given its key will store in BURGER_PRICE variable
            TAX = 18
            QUANTITY = int(input("How much quantity you want")) #Asking user for a Quantity
            Total_Price = str(BURGER_PRICE * QUANTITY + TAX) #Calculating Total_Price
            #Preparing Bill And storing it in a File Named Bill.txt
            TUPLE_B = ("BURGER You Order : " , BURGER_Name , '\n' , "TAX : " , str(TAX) ,'\n',"BURGER PRICE : ",str(BURGER_PRICE) , '\n',"Quantity You Ordered : " , str(QUANTITY) , '\n',"TOTAL PRICE : " , str(Total_Price)) 
            with open("bill.txt" , "w" ) as W:
                for i in TUPLE_B:
                    W.write(i)
            
                
            
            
            
    while input("Is You Want Steaks?Type Yes or No") == "Yes":  #If yes it take to Steaks Lists
        for b in STEAKS_LIST:
            print(b)
        if input("Want to Choose Something from the list?Yes or No ") == "Yes": #If user Wants to select Steaks
            Dish_Name = input('What do you want?') # Asking to user for input its dish
            STEAKS_PRICE = int(STEAKS_DICTIONARY[Dish_Name])  #Asking for a user to type its dish name and it will give its price Which is stored as a key
            TAX = 18 #Tax
            QUANTITY = int(input("How much quantity you want")) #Asking for a Quantity
            Total_Bill = str(QUANTITY * STEAKS_PRICE + TAX) #Calculating Total Bill
            #Prepaing the bill and Storing it in the file named bill.txt
            TUPLE_S = ("DISH YOU ORDERED : " , Dish_Name ,'\n' ,"DISH PRICE :", str(STEAKS_PRICE) , '\n' , "TAX : " ,str(TAX) , '\n',"QUANTITY YOU ORDERED : " , str(QUANTITY) ,'\n',"TOTAL BILL  : " , str(Total_Bill))
            with open("bill.txt" , "w") as S:
                for s in TUPLE_S:
                    S.write(s)
             
elif print("error"): #If user type in seeing Menu Something wrong then it tells it is wrong
    print("error")
else:
    if input("If you want to Exit then type Exit") == "Exit": #if user want to exit then type Exit 
        print("THANKS FOR COMING")   