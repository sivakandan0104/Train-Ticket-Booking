import re
ticket_price = {'vadalur': 100,'madurai':300,
                'cuddalore': 150, 'chennai': 200,
                'salem': 75, 'trichy': 120,
                'chidambaram':120,'viruthachalam':120}
cs = {'A': 3, 'B': 2, 'C': 1}
class node:
    def __init__(self,name,ides,num,ad,ch,cl,st,en,price,status):
        self.Name = name
        self.Id = ad
        self.Number = num
        self.Adult = ad
        self.Child = ch
        self.Start = st
        self.Destination = en
        self.Price = price
        self.Status = status
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertatbegin(self,name,ides,num,ad,ch,cl,st,en,price,status):
        new_node = node(name,ides,num,ad,ch,cl,st,en,price,status)
        
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insertatend(self,name,ides,num,ad,ch,cl,st,en,price,status):
        new_node = node(name,ides,num,ad,ch,cl,st,en,price,status)
        
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            
            while current_node.next is not None:
                current_node = current_node.next
            
            current_node.next = new_node
    
    def insertatposition(self,name,ides,num,ad,ch,cl,st,en,price,status,index):
        new_node = node(name,ides,num,ad,ch,cl,st,en,price,status)
        
        if self.head == None:
            print('list is empty')
            return
        elif index == 0:
            self.insertatbegin(name,ides,num,ad,ch,cl,st,en,price,status)
        else:
            current_node = self.head
            previous_current = None
            position = 0
            
            while (position < index) and (current_node is not None):
                previous_current = current_node
                current_node = current_node.next
                position += 1
                
            if index == position:
                previous_current.next = new_node
                new_node.next = current_node
            else:
                print('cant add number in a position out of index')
        
    def removeatbegin(self):
        
        if self.head == None:
            print('list is empty')
            return
        else:
            current_node = self.head
            
            self.head = current_node.next
        
    def removeatend(self):
        
        if self.head == None:
            print('list is empty')
        elif self.head.next == None:
            self.head = None
        else:
            current_node = self.head
            previous_current = None
            
            while current_node.next is not None:
                previous_current = current_node
                current_node = current_node.next
                
            previous_current.next = None
            
    def removeatposition(self,index):
        
        if self.head == None:
            print('list is empty')
        elif index == 0:
            self.removeatbegin()
        else:
            current_node = self.head
            previous_current = None
            position = 0
            
            while (position < index) and (current_node is not None):
                previous_current = current_node
                current_node = current_node.next 
                position += 1
            
            if position == index:
                previous_current.next = current_node.next
            else:
                print('cant remove the node index out of range')
    
    def updateatposition(self,data,status,index):
        
        if self.head == None:
            print('This Booking ID isnt exist to refund')
        else:
            position = 0
            current_node = self.head
            
            while (position < index) and (current_node is not None):
                current_node = current_node.next
                position += 1
                
            if index == position and current_node is not None:
                m = current_node.Price
                current_node.Price = data
                current_node.Status = status
                print(f"Booking with ID has been refunded. Amount refunded: {m}")
                return current_node.adult + current_node.Child
            else:
                print('This Booking ID isnt exist to refund')
        
    def print_list(self):
        
        if self.head is None:
            print('list is empty')
        else:
            current_node = self.head
            
            while current_node is not None:
                print(f"\nName: {current_node.Name}")
                print(f"ID: {current_node.Id}")
                print(f"Number: {current_node.Number}")
                print(f"Adults: {current_node.Adult}")
                print(f"Children: {current_node.Child}")
                print(f"Start: {current_node.Start}")
                print(f"Destination: {current_node.Destination}")
                print(f"Price: {current_node.Price}")
                print(f"Status: {current_node.Status}")
                current_node = current_node.next
    
            print('None')
            
    def printposition(self,index):
        
        if self.head is None:
            print('\nThere is No Booking with the ID')
        
        else:
            current_node = self.head
            position = 0
            
            while (position < index) and (current_node is not None):
                current_node = current_node.next 
                position += 1
                
            if position == index and current_node is not None:
                print(f"\nName: {current_node.Name}")
                print(f"ID: {current_node.Id}")
                print(f"Number: {current_node.Number}")
                print(f"Adults: {current_node.Adult}")
                print(f"Children: {current_node.Child}")
                print(f"Start: {current_node.Start}")
                print(f"Destination: {current_node.Destination}")
                print(f"Price: {current_node.Price}")
                print(f"Status: {current_node.Status}")
            else:
                print('There is No Booking with the ID')
            
    def extract_num(self, ides):
        match = re.search(r'\d+$', ides)
        if match:
            return int(match.group())
        else:
            raise ValueError("No digits found at the end of the ID")

    def valid_place(self):
        while True:
            place = input('Enter the place name: ').strip().lower()
            if place in ticket_price:
                return place 
            print('Give a valid place name from:', list(ticket_price.keys())) 

    def valid_class(self):
        while True:
            clas = input("Enter the class [A, B, C]: ").strip().upper()
            if clas in cs:
                return clas
            print("Give a valid class ['A', 'B', 'C']") 
            
    def valid_number(self):
        while True:
            num = input('Enter your number: ')
            if num.isdigit() and len(num) == 10:
                return num
            else:
                print('\nPlease enter a valid 10-digit number.\n')

