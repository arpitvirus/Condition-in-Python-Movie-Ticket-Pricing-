# Movie Ticket Pricing .
# Movie Tickets are priced based on age: $12 for adult (18 and Over), $ 8 for children . Everyone gets a $2 discount on Wednesday.
Age = int(input("Enter Your Age :"))
Days = ["","Monday","Tuesday","Wednesday","Thusday","Friday","Satarday","Sunday"]
def Weeks():
    for i in range(8):
        print(Days[i],"Number is ",i, )
Weeks()
day_num = int(input("Enter Day Number :"))

def Movie_Price():
    if(day_num != 3):
        if(Age<18):
            print("Your Ticket price is $8 Dollar")
        elif(Age>=18):
            print("Your Ticket price is $12 Dollar")
    if(day_num == 3):
        if(Age<18):
            print("Your Ticket price is $6 Dollar")
        elif(Age>=18):
            print("Your Ticket price is $10 Dollar")
Movie_Price()