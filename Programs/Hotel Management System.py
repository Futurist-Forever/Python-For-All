# ----------------------------------------------------------------------------------------------------
# HOTEL MANAGEMENT SYSTEM PROGRAM
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------

pattern="----------------------------------------------------------------------------------------------------"

class hotelmanage:

# ----------------------------------------------------------------------------------------------------
# Initialization 
    def __init__(self,q='',s=0,p=0,r=0,t=0,a=1499,name='',checkindate='',checkoutdate='',roomno=1):
 
        print ("\n\n**********WELCOME TO HOTEL HILLSIDE**********\n\n")
 
        self.q=q
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.name=name
        self.checkindate=checkindate
        self.checkoutdate=checkoutdate
        self.roomno=roomno
        self.pattern=pattern
        print(pattern)
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Customer Information       
    def inputdata(self):
        print(pattern)
        self.name=input("\nEnter your Name:")
        self.checkindate=input("\nEnter your Check In date (DD/MM/YYYY):")
        self.checkoutdate=input("\nEnter your Checkout date (DD/MM/YYYY):")
        print("Your room no. is:",self.roomno,"\n")
        print(pattern)
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Room Rent       
    def roomrent(self):

        print(pattern)
 
        print ("Please select a room:-")
 
        print ("1.  Double Bed With AC---@Rs.3999")
 
        print ("2.  Single Bed With AC---@Rs.2999")
 
        print ("3.  Double Bed Without AC---@Rs.1999")
 
        print ("4.  Single Bed Without AC---@Rs.1199")

        print(pattern)
 
        x=int(input("Enter the number of your choice: "))
 
        n=int(input("For How Many Nights Did You Stay: "))

        print(pattern)
 
        if(x==1):
 
            print ("You have choosen room Double Bed With AC")
 
            self.s=3999*n
 
        elif (x==2):
 
            print ("You have choosen room Single Bed With AC")
 
            self.s=2999*n
 
        elif (x==3):
 
            print ("You have choosen room Double Bed Without AC")
 
            self.s=1999*n
 
        elif (x==4):
            print ("You have choosen room Single Bed Without AC")
 
            self.s=1199*n
 
        else:
 
            print ("Please choose a room")
 
        print ("Your choosen room rent is =",self.s,"\n")

        print(pattern)
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Food Cost 
    def foodpurchased(self):

        print(pattern)
 
        print("\n**********RESTAURANT MENU**********")
 
        print("\n1.  Dessert---@Rs.120","\n2.  Drinks---@Rs.30","\n3.  Breakfast---@Rs.70","\n4.  Lunch---@Rs.180","\n5.  Dinner---@Rs.150","\n6.  EXIT FROM THIS MENU")

        print(pattern)
 
        while (1):
 
            c=int(input("Enter the number of your choice:"))
 
            if (c==1):
                d=int(input("Enter the quantity:"))
                print(pattern)
                self.r=self.r+120*d
 
            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 print(pattern)
                 self.r=self.r+30*d
 
            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 print(pattern)
                 self.r=self.r+70*d
 
            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 print(pattern)
                 self.r=self.r+180*d
 
            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 print(pattern)
                 self.r=self.r+150*d
 
            elif (c==6):
                break
            else:
                print("You've Entered an Invalid Key")
                print(pattern)
 
        print ("Total Food Cost=Rs.",self.r,"\n")
        print(pattern)
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# Total Bill 
    def display(self):
        print(pattern)
        print ("\n******HOTEL BILL******\n")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Check in date:",self.checkindate)
        print ("Checkout date",self.checkoutdate)
        print ("Room no.",self.roomno)
        print ("Your Room rent is: Rs.",self.s)
        print ("Your Food bill is: Rs.",self.r)
        
        self.q=self.s+self.t+self.p+self.r
 
        print ("Your subtotal is: Rs.",self.q)
        print ("Additional Service Charges is: Rs.",self.a)
        print ("Your grandtotal is: Rs.",self.q+self.a,"\n")

        print("**********THANK YOU FOR VISITING US**********\n")
        print(pattern)
        self.roomno+=1
# ----------------------------------------------------------------------------------------------------
 

# ----------------------------------------------------------------------------------------------------
# Dashboard 
def main():
 
    a=hotelmanage()

    while (1):

        print(pattern)

        print("1.Enter Customer Data")
        
        print("2.Calculate Room Rent")
 
        print("3.Calculate Food Cost")
 
        print("4.Show Total Cost Including Taxes")
 
        print("5.EXIT FROM THIS PROGRAM")

        print(pattern)
 
        b=int(input("\nEnter the number of your choice:"))

        print(pattern)

        if (b==1):
            a.inputdata()
 
        if (b==2):
 
            a.roomrent()
 
        if (b==3):
 
            a.foodpurchased()
 
        if (b==4):
 
            a.display()
 
        if (b==5):
 
            quit()

print(pattern) 

main()


# ----------------------------------------------------------------------------------------------------
# *******************************************END OF PROGRAM*******************************************
