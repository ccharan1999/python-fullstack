shopname = "shopfront"
p1_name = "Bmw"
p1_stock= int("10") 
p1_prise = int("10000")
p2_name = "Tata"
p2_stock = int("20")
p2_prise = int("5000")
p3_name ="Honda"
P3_stock= int("30"),
P3_prise = int("9000")
print("="*50,"\n", f"{shopname:^50}","\n" , "=" * 50)
customer = input("Your name please:")
print(f"HI!!{customer}")
print(f"\n welcome to shop {customer}")
print(f"Select our product:{p1_name},{p2_name},{p3_name}")
product =input( ) 
if product  != p1_name and  product != p2_name and product != p3_name :
    print("product not avalible")
quantity =input("enter how much you want?")
if quantity != int:
    print("enter a number")
print ("please enter the prise")

 


