x=input("enter the month")
y=int(input("enter the date"))

if (x=="march" and y>19) or x=="april" or x=="may" or (x=="june" and y<21):
    print("the season is summer")
elif(x=="june" and y>21) or x=="july" or x=="august" or (x=="september" and y<22):
    print("the season is spring")
elif(x=="september" and y>22) or x=="october" or x=="novemder" or(x=="december" and y<21):
    print("the season is fall")
else:
    print("the season is winter")
