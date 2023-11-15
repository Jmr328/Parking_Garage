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
                print("Thank you, have a nice day")
                spaceNum += 1
                print(f"There are now {spaceNum} parking spaces left")
                break
            else:
                print("you owe some more money")

    

            
    
                
    
    
        



Park = Garage()

Park.takeTicket()
Park.incTicket()
Park.takeTicket()
Park.takeSpace()
Park.decSpaces()
Park.takeSpace()
Park.payForParking()