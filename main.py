from summation import sum_
from multiplication import mult

if __name__ == "__main__":
    x = int(input("Enter an integer: "))
    y = int(input("Enter an integer: "))
    print(f"SUM of X: {x} and Y: {y} is: {sum_(x,y)}")
    print(f"MULTIPLICATION of X: {x} and Y: {y} is: {mult(x,y)}")