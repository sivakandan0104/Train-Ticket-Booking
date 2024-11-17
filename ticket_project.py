#Linkedlist code
import re
class node:
    def __init__(self,name,ides,num,ad,ch,total,st,en,price,status):
        self.Name = name
        self.Id = ides
        self.Number = num
        self.Adult = ad
        self.Child = ch
        self.Total = total
        self.Start = st
        self.Destination = en
        self.Price = price
        self.Status = status
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.ticket = 50
        self.count = 0
    
    def inserting(self,name,ides,num,ad,ch,total,st,en,price,status):
        new = node(name,ides,num,ad,ch,total,st,en,price,status)
        
        if self.head == None:
            self.head = new
        elif self.head.next == None:
            self.head.next = new
        else:
            current = self.head
            
            while current.next is not None:
                current = current.next
            
            current.next = new
            self.count += 1
        print(f'\nSuccessfully Booked Your id: {new.Id}')
        print(f'Price: ₹{new.Price}')
        
    def updating(self,ides): 
        ix = re.search(r'\d+$',ides)
        current = self.head

        while current is not None:
            index = re.search(r'\d+$',current.Id)
            if index.group() == ix.group():
                current.Status = 'Refunded'
                current.Price = 0
                self.ticket += current.Total
                print('\nThe Booking is Cancelled Succesfully')
                return
            current = current.next
        
        print('\nNo Booking Is Available with this ID')
    
    def printing(self,ides):
        ix = re.search(r'\d+$',ides)
        current = self.head
        
        while current is not None:
            index = re.search(r'\d+$',current.Id)
            if ix.group() == index.group():
                if current.Status != 'Refunded':
                    print(f'\nName: {current.Name}')
                    print(f'Id: {current.Id}')
                    print(f'No.Of.Tickets: {current.Total}')
                    print(f'Starting: {current.Start}')
                    print(f'Destination: {current.Destination}')
                    print(f'Price: ₹{current.Price}')
                else:
                    print(f'\nName: {current.Name}')
                    print(f'Status: {current.Status}')
                return
            current = current.next
        
        print('\nNo Booking Is Available with this ID')
    
    def validnumber(self):
        while True:
            number = input('enter Your Number: ')
            if number.isdigit() and len(number) == 10:
                return number
            else:
                print('Please enter a valid number')
                
#Main code

train = linkedlist()
count = 0
prices ={'vadalur': 100,'madurai':300,'cuddalore': 150, 'chennai': 200,'salem': 75, 'trichy': 120,'chidambaram':120,'viruthachalam':120}
areas = ['vadalur','madurai','cuddalore', 'chennai','salem', 'trichy','chidambaram','viruthachalam']
p = True
while True:
    x = int(input('\nEnter Your Choice[1(Booking), 2(Refund), 3(Print Receipt), 4(Tickets Available), 5(exit)]: '))
    if x == 1:
        if train.ticket > 0:
            name = input('\nEnter Your Name: ')
            ides = 'TN2024A' + str(count)
            num = train.validnumber()
            while True:
                ad = int(input('No.Of.Adults: '))
                ch = int(input('No.Of.Childs: '))
                if ad+ch > 0:
                    break
                else:
                    print('\nAtleast Book one ticket')
            total = ad + ch
            while True:
                print(areas)
                st = input('\nEnter Starting Point: ')
                if st in areas:
                    while True:
                        en = input('Enter Destination: ')
                        if en in areas:
                            if st != en:
                                p = False
                                break
                            else:
                                print('\nThe destination cannot be the same as the starting place.\n')
                        else:
                            print('\nPlease enter a valid destination\n')
                else:
                    print('\nPlease enter the valid location')
                if not p:
                    break
            cost = prices[st] + prices[en]
            price = int((cost * ad) + ((cost/2) * ch)) 
            status = 'Active'
            if (train.ticket-total) != 0:
                train.inserting(name, ides, num, ad, ch, total, st, en, price, status)
                train.ticket -= total
                count += 1
            else:
                print(f'\nNot Enough Tickets Available. Tickets Available: {train.ticket}')
        else:
            print('\nTicket Is Full')
    if x == 2:
        name = input('Enter Your Name: ')
        ides = input('Enter Your Id: ')
        train.updating(ides)
    if x == 3:
        name = input('Enter Your Name: ')
        ides = input('Enter Your Id: ')
        train.printing(ides)
    if x == 4:
        print(f'\nTickets Available: {train.ticket}')
    if x == 5:
        break
    
    
                
