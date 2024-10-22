import linked_train
p = True
ide = "TN31A" 
ticket_avl = 50
ticket_sold = index = 0
obj = linked_train.LinkedList()
while p:
    print('\n> Train Ticket Booking\n')
    x = int(input('Enter Your Choice [1(booking), 2(view detail), 3(refund), 4(exit)] : '))
    if x == 1:
        if ticket_avl > 0:
            status = 'Active'
            name = input('\nEnter your name : ')
            ides = ide + str(index)
            num = obj.valid_number()
            
            while True:
                adult = int(input('Adult : '))
                child = int(input('Child : '))
                tot = adult + child
                if tot > 0:
                    break
                else:
                    print('\nYou must book at least one ticket.\n')
                    
            st = obj.valid_place()
            
            while True:
                en = obj.valid_place()
                if en != st:
                    break
                else:
                    print('\nThe destination cannot be the same as the starting place.\n')
                    
            clas = obj.valid_class()
            cost = linked_train.ticket_price[st] + linked_train.ticket_price[en]
            price = ((adult * cost) + round(child * cost/2)) * linked_train.cs[clas]

            if ticket_avl >= tot:
                ticket_avl -= tot
                index += 1
                obj.insertatend(name,ides,num,adult,child,clas,st,en,price,status)
                print('\nYour Order Placed.')
                print(f'your id is {ides}\n\n')
            else:
                print(f'ticket available is {ticket_avl} your placing {tot} ')
                
        else:
            print('Out Of Stock')
            
    if x == 2:
        name = input('\nEnter your Name : ')
        ides = input('Enter your Id : ')
        i = obj.extract_num(ides)
        obj.printposition(i)
    if x == 3:
        name = input('\nEnter your Name : ')
        ides = input('Enter your Id : ')
        i = obj.extract_num(ides)
        data = 0
        status = 'Refunded'
        obj.updateatposition(data, status, i)
    if x == 4:
        p = False
        print("\nThank you for using the train ticket booking system. Goodbye!")
        
#obj.print_list()