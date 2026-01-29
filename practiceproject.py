items={"rice":20,"dal":90,"sugar":30}
price=0
pricelist=0
totalprice=0
ilist=0
qlist=0
plist=0
finalprice=0
for i in range(items(len)):
    inpt=input("if you want to buy press 2 or 3 for quit")
    if(inpt==2):
        item=input("enter an item")
        quantity=int(input("enter quantity"))
        if item in items.keys():
        price=quantity*items[item]
        pricelist.append((item,items,quantity,price))
        totalprice+=price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price) 
        finalprice+=price
    
