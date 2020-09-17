import random
def main():
    smaller=int(input("Enter the smaller number:"))
    larger=int(input ("Enter the larger number:"))
    mynumber= random.randit(smaller,larger)
    count=0
    while True:
        count+=1
        usernumber=int(input("Enter your guess:"))
        if usernumber < mynumber:
           print("To small.")
        elif usernumber > mynumber:
            print("To large")
        else:
            print("Your right.")
            break