#define the menu f resturant
menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'cofee':80,
}
print("wellcome to our python restaurant")
print("pizza: Rs=40\n,pasta: Rs=50\n,burger: Rs=60\n,salad: Rs=70\n,cofee Rs=80")
order_total=0
item_1=input("enter the name of item you want to order=")
if item_1 in menu:
  order_total+=menu[item_1]
  print(f" your item {item_1}has been added to your ordered")
 
else:
  print(f"your item{item_1} is not available yet!!") 
another_order=input("do you want to add another item(yes/no)")
if another_order == "yes":
  item_2=input("enter the name of second item")
  if item_2 in menu:
    order_total+=menu[item_2]
    print(f"item {item_2}has been added to your order]")
  else:
    print(f"ordered item {item_2}is not available yet!!")
print(f"the total amount of iem is to pay {order_total}")