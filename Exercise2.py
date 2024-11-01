def SlamBookInfo(fname, fage, fcolor, fmovie, fnumber, fmotto):
    print("Hello, " + fname + "!")
    print("I can't believe you're", str(fage) + " This year!")
    print("I do also love " + fcolor + ". Its giving " + fmovie)
    print("Well, its nice meeting you, just gonna get your number. Its " + str(fnumber) + " right?")
    print("Just like you always say, " + fmotto + "!")


name = input("Name: ")
age = int(input("Age: "))
color = input("Favorite Color: ")
movie = input("Favorite Movie: ")
number = int(input("Enter 11-digit Mobile Number: "))
motto = input("Favorite Motto: ")

SlamBookInfo(name, age, color, movie, number, motto)


