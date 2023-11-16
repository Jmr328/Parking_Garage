class Garage():

    Ticket = []
    spaces = 25

    def __init__(self):
        self.ticket = 1
        self.spaces = 25
        
    def takeTicket(self):               
        ticketNum = self.ticket
        print(f"Here's your ticket, #{ticketNum}")

    def allTicket(self, ticket):
        self.ticket = ticket

    def incTicket(self):
        if self.ticket ==isinstance(self.ticket, str):
            print("No fun")
        else:
            self.ticket += 1
    
    def decTicket(self):
        if self.ticket ==isinstance(self.ticket, str):
            print("No fun")
        else:
            self.ticket -= 1

    def takeSpace(self):
        spaceNum = self.spaces
        print(f"There are {spaceNum} parking spaces left")
    
    def allSpaces(self, spaces):
        self.spaces = spaces    

    def decSpaces(self):
        if self.ticket ==isinstance(self.ticket, str):
            print("No fun")
        else:
            self.spaces -= 1

    def incSpaces(self):
        if self.ticket ==isinstance(self.ticket, str):
            print("No fun")
        else:
            self.spaces += 1
    
    def payForParking(self):
        
        while True:
            spaceNum = self.spaces
            paid = int(input("Please enter 5 bones: "))
            if paid >= 5:
                print("\nThank you, have a nice day")
                spaceNum += 1
                print(f"There are now {spaceNum} parking spaces left")
                break
            else:
                print("That ain't gunna work")


Park = Garage()

def inRun():
    while True:
        question = input("Please press 'Enter' for a ticket: ")

        if question == '':
            Park.takeTicket()
            Park.incTicket()            
            Park.decSpaces()
            Park.takeSpace()
            break
        else:
            print("\nI said press 'Enter' for a Ticket: ")

def outRun():
    while True:
        question = input("\nPlease press 'Enter' and insert your ticket: ")

        if question == '':
            Park.payForParking()
            break
        else:
            print("\nYou don't like to follow directions do you?")



    
inRun()
outRun()
