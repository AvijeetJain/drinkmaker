drinks=['1 Coffee','2 Milkshake','3 Mojito','4 Freaky shake','5 Smoothie','6 Mocktail','7 Chocolate_lovers']
total=0
print('--------------------- Welcome ---------------------\n----------------------- to -----------------------\n------------------- DRINKMAKER --------------------\n')
 
print('*********************\n        MENU \n*********************\n')
print(drinks)
print()

p=0

#coffee
p={'no' : '1', 'item' : '1. Latte', 'price':120 , 'stock': 9}
q={'no' : '2', 'item' : '2. Classic Frappe', 'price':165 , 'stock':8}
r={'no' : '3', 'item' : '3. Espresso', 'price':199 , 'stock': 5}
s={'no' : '4', 'item' : '4. Capuccino', 'price':165 , 'stock':6}
t={'no' : '5', 'item' : '5. Cafe Mocha', 'price':250 , 'stock': 9}
u={'no' : '6', 'item' : '6. Iced Americano', 'price':180 , 'stock':11}

cof=[p,q,r,s,t,u]

#milkshake
a={'no' : '1', 'item' : '1. Oreo Milkshake', 'price':215, 'stock': 5}
b={'no' : '2', 'item' : '2. Kitkat Milkshake', 'price':250 , 'stock':8}
c={'no' : '3', 'item' : '3. Belgium Milkshake', 'price':200 , 'stock': 5}
d={'no' : '4', 'item' : '4. Chocolate Hazelnut Milkshake', 'price':200 , 'stock':5}
e={'no' : '5', 'item' : '5. Nutella Milkshake', 'price':210 , 'stock': 7}
f={'no' : '6', 'item' : '6. Ferrero Milkshake', 'price':230 , 'stock':10}

milk=[a,b,c,d,e,f]

#mojito
g={'no' : '1', 'item' : '1. Peach', 'price':155 , 'stock': 5}
h={'no' : '2', 'item' : '2. Lemon', 'price':165 , 'stock':6}
i1={'no' : '3', 'item' : '3. Watermelon', 'price':160 , 'stock': 7}
j1={'no' : '4', 'item' : '4. Italian', 'price':165 , 'stock':6}
k1={'no' : '5', 'item' : '5. Paan Bahar', 'price':225 , 'stock': 9}
l1={'no' : '6', 'item' : '6. Fashion Fruit', 'price':178 , 'stock':3}

moj=[g,h,i1,j1,k1,l1]

#freaky shake

x={'no' : '1', 'item' : '1. Cookie & Cream', 'price':370 , 'stock': 5}
m1={'no' : '2', 'item' : '2. Red Velvet', 'price':370 , 'stock':8}
n1={'no' : '3', 'item' : '3. Caramel', 'price':400 , 'stock': 9}
o1={'no' : '4', 'item' : '4. Chocolate Monster', 'price':350 , 'stock':6}
v={'no' : '5', 'item' : '5. Colorful Candy', 'price':390 , 'stock': 8}
w={'no' : '6', 'item' : '6. Chocolate Indulge', 'price':410 , 'stock':4}

freaky=[x,m1,n1,o1,v,w]

#smoothie

aa={'no' : '1', 'item' : '1. Watermelon', 'price':245 , 'stock': 3}
bb={'no' : '2', 'item' : '2. Mango', 'price':213 , 'stock':3}
cc={'no' : '3', 'item' : '3. Kiwi Apple', 'price':350 , 'stock': 7}
dd={'no' : '4', 'item' : '4. Banana', 'price':178 , 'stock':12}
ee={'no' : '5', 'item' : '5. Strawberry', 'price':278 , 'stock': 9}
ff={'no' : '6', 'item' : '6. Raspberry', 'price':190 , 'stock':5}

smooth=[aa,bb,cc,dd,ee,ff]

#mocktails

gg={'no' : '1', 'item' : '1. Rowdy Rum', 'price':170 , 'stock': 12}
hh={'no' : '2', 'item' : '2. yo yo', 'price':199 , 'stock':11}
ii={'no' : '3', 'item' : '3. American Pie', 'price':185 , 'stock': 10}
jj={'no' : '4', 'item' : '4. Killer Lady', 'price':264 , 'stock':6}
kk={'no' : '5', 'item' : '5. Dadagiri Spicy', 'price':255 , 'stock': 2}
ll={'no' : '6', 'item' : '6. Ghost Rider', 'price':198 , 'stock':8}

mock=[gg,hh,ii,jj,kk,ll]

#chocolate lovers

xx={'no' : '1', 'item' : '1. French Vanilla', 'price':150 , 'stock': 7}
mm={'no' : '2', 'item' : '2. White Hot Chocolate', 'price':180 , 'stock':8}
nn={'no' : '3', 'item' : '3. Peanut Butter', 'price':220 , 'stock': 12}
oo={'no' : '4', 'item' : '4. Yum Yum', 'price':156 , 'stock':6}
vv={'no' : '5', 'item' : '5. ho ho', 'price':230 , 'stock': 8}
ww={'no' : '6', 'item' : '6. Mint White Chocolate', 'price':310 , 'stock':4}

lovers=[xx,mm,nn,oo,vv,ww]


order='yes'
order_no=0
selected=[]
while order=='yes' or order=='y' or order=='Y':
    
    selected_drink=input('What would you like to have today : ')
    print()
    for item in drinks:
        drinks=['1 Coffee','2 Milkshake','3 Mojito','4 Freaky shake','5 Smoothie','6 Mocktail','7 Chocolate_lovers']

        #billing for coffee
        
        if selected_drink=='Coffee' or selected_drink== '1' or selected_drink=='coffee' or selected_drink=='C' or selected_drink=='c':
            print('Item Name            Price \n')
            for ab in cof:
                string_name = ab.get('item')
                name_len = len(string_name)
                print(ab.get('item'), end='')
                for i in range(20 - name_len):
                  print(' ', end='')
                print(':',ab.get('price'),end=' ')
                print()
            print()
            coffee=input("Input coffee no: ")
            size=input("Cup_size(Small(Rs 30)/Medium(Rs 50)/Large(Rs 100)): ")
            
            if size=='small' or size=='s' or size=='Small' :
                p=30
            elif size=='medium' or size=='m' or size=='Medium':
                p=50
            elif size=='large' or size=='l' or size=='Large':
                p=100
            quantity1=int(input("Quantity: "))


            for i in cof:
            
                if coffee==i.get('no'):
                    
                    price1=i.get('price')
                    
                    stock1=i.get('stock')

                    if quantity1 <= stock1:
                        stock1-=quantity1
                        total=total+(price1*quantity1)+ (p*quantity1)
                        order_no+=1
                        i['stock']-=quantity1
                        selected1=[i.get('item'),price1,quantity1,size,(price1*quantity1)+(p*quantity1)]
                        selected.append(selected1)
                        
                            
                        continue
                    elif quantity1>stock1:
                        print('We do not have', quantity1, i.get('item'))
            break

        #billing for mojito
        elif selected_drink=='Mojito' or selected_drink== '3' or selected_drink=='mojito' or selected_drink=='M' or selected_drink=='m':
            print('Item Name            Price \n')
            for ac in moj:
                string_name = ac.get('item')
                name_len = len(string_name)
                print(ac.get('item'), end='')
                for i in range(20 - name_len):
                  print(' ', end='')
                print(':',ac.get('price'),end=' ')
                print()
            print()
            
            mojito=input("Select Mojito : ")
            size=input("Cup_size(Small(Rs 30)/Medium(Rs 50)/Large(Rs 100)): ")
            
            if size=='small' or size=='s' or size=='Small' :
                p=30
            elif size=='medium' or size=='m' or size=='Medium':
                p=50
            elif size=='large' or size=='l' or size=='Large':
                p=100
                
            quantity2=int(input("Quantity: "))
            for j in moj:
                if mojito==j.get('no'):
                    price2=j.get('price')
                    
                    stock2=j.get('stock')

                    if quantity2 <= stock2:
                        stock2-=quantity2
                        total=total + (price2*quantity2) + (p*quantity2)
                        order_no+=1
                        j['stock']-=quantity2
                        selected2=[j.get('item'),price2,quantity2,size,(price2*quantity2) + (p*quantity2)]
                        selected.append(selected2)
                        continue
                    elif quantity2>stock2:
                        print('we do not have', quantity2, j.get('item'))

            break
    
        #billing for milkshake
        elif selected_drink=='Milkshake' or selected_drink== '2' or selected_drink=='milkshake' or selected_drink=='M' or selected_drink=='m':
            print('Item Name                          Price \n')
            for ad in milk:
                string_name = ad.get('item')
                name_len = len(string_name)
                print(ad.get('item'), end='')
                for i in range(35 - name_len):
                  print(' ', end='')
                print(':',ad.get('price'),end='   ')
                print()
            print()
             
            milkshake=input("Select Milkshake : ")
            size=input("Cup_size(Small(Rs 30)/Medium(Rs 50)/Large(Rs 100)): ")

            if size=='small' or size=='s' or size=='Small' :
                p=30
            elif size=='medium' or size=='m' or size=='Medium':
                p=50
            elif size=='large' or size=='l' or size=='Large':
                p=100
                
            quantity3=int(input("Quantity: "))

            for k in milk:
                if milkshake==k.get('no'):
                    price3=k.get('price')
                    
                    stock3=k.get('stock')
                    if quantity3 <= stock3:
                        stock3-=quantity3
                        total=total + (price3*quantity3) + (p*quantity3)
                        order_no+=1
                        k['stock']-=quantity3
                        selected3=[k.get('item'),price3,quantity3,size,(price3*quantity3) + (p*quantity3)]
                        selected.append(selected3)
                        continue
                    elif quantity3>stock3:
                        print('we do not have', quantity3, k.get('item'))
                    
            break

        #billing for freaky shake
        elif selected_drink=='Freaky shake' or selected_drink== '4' or selected_drink=='freaky shake' or selected_drink=='f' or selected_drink=='F':
            print('Item Name                Price \n')
            for ae in freaky:
                string_name = ae.get('item')
                name_len = len(string_name)
                print(ae.get('item'), end='')
                for i in range(25 - name_len):
                  print(' ', end='')
                print(':',ae.get('price'),end='   ')
                print()
            print()
            
            freakyshake=input("Select Freaky Shake : ")
            size=input("Cup_size(Small(Rs 30)/Medium(Rs 50)/Large(Rs 100)): ")

            if size=='small' or size=='s' or size=='Small' :
                p=30
            elif size=='medium' or size=='m' or size=='Medium':
                p=50
            elif size=='large' or size=='l' or size=='Large':
                p=100
                
            quantity4=int(input("Quantity: "))

            for l in freaky:
                if freakyshake==l.get('no'):
                    price4=l.get('price')
                    
                    stock4=l.get('stock')
                    if quantity4 <= stock4:
                        stock4-=quantity4
                        total=total + (price4*quantity4) + (p*quantity4)
                        l['stock']-=quantity4
                        order_no+=1
                        selected4=[l.get('item'),price4,quantity4,size,(price4*quantity4) + (p*quantity4)]
                        selected.append(selected4)
                        continue
                    elif quantity4>stock4:
                        print('we do not have', quantity4, l.get('item'))
            break

        #billing for smoothie
        elif selected_drink=='Smoothie' or selected_drink== '5' or selected_drink=='smoothie' or selected_drink=='S' or selected_drink=='s':
            print('Item Name            Price \n')
            for af in smooth:
                string_name = af.get('item')
                name_len = len(string_name)
                print(af.get('item'), end='')
                for i in range(20 - name_len):
                  print(' ', end='')
                print(':',af.get('price'),end=' ')
                print()
            print()
            
            smoothie=input("Select Smoothie : ")
            size=input("Cup_size(Small(Rs 30)/Medium(Rs 50)/Large(Rs 100)): ")

            if size=='small' or size=='s' or size=='Small' :
                p=30
            elif size=='medium' or size=='m' or size=='Medium':
                p=50
            elif size=='large' or size=='l' or size=='Large':
                p=100
                
            quantity5=int(input("Quantity: "))

            for m in smooth:
                if smoothie==m.get('no'):
                    price5=m.get('price')
                    
                    stock5=m.get('stock')

                    if quantity5 <= stock5:
                        stock5-=quantity5
                        total=total + (price5*quantity5) + (p*quantity5)
                        m['stock']-=quantity5
                        order_no+=1
                        selected5=[m.get('item'),price5,quantity5,size,(price5*quantity5) + (p*quantity5)]
                        selected.append(selected5)
                        continue
                    elif quantity5>stock5:
                        print('we do not have', quantity5, m.get('item'))
            break


        #billing for mocktail
        elif selected_drink=='Mocktail' or selected_drink== '6' or selected_drink=='mocktail' or selected_drink=='M' or selected_drink=='m':
            print('Item Name                 Price \n')
            for ag in mock:
                string_name = ag.get('item')
                name_len = len(string_name)
                print(ag.get('item'), end='')
                for i in range(25 - name_len):
                  print(' ', end='')
                print(':',ag.get('price'),end='   ')
                print()
            print()
        
            mocktail=input("Select Mocktail : ")
            size=input("Cup_size(Small(Rs 30)/Medium(Rs 50)/Large(Rs 100)): ")

            if size=='small' or size=='s' or size=='Small' :
                p=30
            elif size=='medium' or size=='m' or size=='Medium':
                p=50
            elif size=='large' or size=='l' or size=='Large':
                p=100
                
            quantity6=int(input("Quantity: "))
            for n in mock:
                if mocktail==n.get('no'):
                    price6=n.get('price')
                    
                    stock6=n.get('stock')

                    if quantity6 <= stock6:
                        stock6-=quantity6
                        total=total + (price6*quantity6) + (p*quantity6)
                        n['stock']-=quantity6
                        order_no+=1
                        selected6=[n.get('item'),price6,quantity6,size,(price6*quantity6) + (p*quantity6)]
                        selected.append(selected6)
                        
                        continue
                    elif quantity6>stock6:
                        print('we do not have', quantity6, n.get('item'))

            break

        #billing for chocolate_lovers
        elif selected_drink=='Chocolate_lovers' or selected_drink== '7' or selected_drink=='chocolate lovers' or selected_drink=='Ch' or selected_drink=='ch':
            print('Item Name                      Price \n')
            for ah in lovers:
                string_name = ah.get('item')
                name_len = len(string_name)
                print(ah.get('item'), end='')
                for i in range(30 - name_len):
                  print(' ', end='')
                print(':',ah.get('price'),end='   ')
                print()
            print()
                
            chocolate_lovers=input("Select Chocolate Lovers : ")
            size=input("Cup_size(Small(Rs 30)/Medium(Rs 50)/Large(Rs 100)): ")
            
            if size=='small' or size=='s' or size=='Small' :
                p=30
            elif size=='medium' or size=='m' or size=='Medium':
                p=50
            elif size=='large' or size=='l' or size=='Large':
                p=100
                
            quantity7=int(input("Quantity: "))

            for o in lovers:
                if chocolate_lovers==o.get('no'):
                    price7=o.get('price')
                    
                    stock7=o.get('stock')

                    if quantity7 <= stock7:
                        stock7-=quantity7
                        total=total + (price7*quantity7)  + (p*quantity7)
                        o['stock']-=quantity7
                        order_no+=1
                        selected7=[o.get('item'),price7,quantity7,size,(price7*quantity7) + (p*quantity7)]
                        selected.append(selected7)
                        continue
                    elif quantity7>stock7:
                        print('we do not have', quantity7, o.get('item'))

            break
    order=input("Would you like to order anything else(yes/no) : ")
    print()
    if order=='yes' or order=='y' or order=='Y':
        print(drinks)
    print()

print('-------------------------------------------------------------------------------------------------------')
print()
print('Order No. : 2365224532547' )

print('PURCHASED ITEMS \n')

print('----------------------------------------PURCHASED ITEMS------------------------------------------------')
print()
abc=0
t=total*0.05
print('Item Name | Price | Quantity | Cup-Size | Total \n')
while order_no>0:
   for va in range(order_no):
        for pr in range(0,4324533):
            print(selected[abc][0],'  |  ', selected[abc][1],'  |  ', selected[abc][2],'  |  ', selected[abc][3],'  |  ', selected[abc][4], end=' ')
            print()
            abc+=1
            break
        print()
        order_no-=1

print("YOUR BILL IS          :",total)
print("TAX                   :  5%")
print("AMOUNT TO BE PAID     :",round(total+t))

print()


bbb=input("How would you like to pay(Cash/ Credit Card/ Debit Card/ Visa) : ")
cbc=int(input("Enter amount: "))
if cbc<(total+t):
    print("THE TRANSACTION CANNOT BE PROCESSED...AMOUNT TO BE PAID IS MORE THAN THE DEPOSITED AMOUNT")
    cbc=int(input("Enter amount: "))
    if cbc>=(total+t):
        print("AMOUNT RETURNED: ",cbc-round(total+t))
        print('Your order will be ready in 15 min')
  
elif cbc>=(total+t):
    print("AMOUNT RETURNED: ",cbc-round(total+t))
    print('Your order will be ready in 15 min')
print()

print('----------------------------------------- THANK YOU -----------------------------------------------------')
print()
print("----------------------------------------HAVE A NICE DAY--------------------------------------------------")



            
    
    
    
                 

    


    
    
    
