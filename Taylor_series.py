import os

from TaylorSeries import TaylorSeries
from Color import bgColor
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Welcome to Taylor series  by Marko Polo ")


class Main:
    interrupter = True
    global taylorSeries

    while interrupter:
        print(bgColor.CBLUE, f"{ascii_banner}")

        print(bgColor.CYELLOW, """
                Введіть опцію обрахувння
                
                1. Sin
                
                2. Cos 
                
                3. ln(x + 1)
                
                4. Arctan
                
                5. Exit
        """)

        enterOption = int(input("Enter options : "))

        enterDegree = int(input("Enter degree : "))
        enterCountOfCycle = int(input("Enter count of cycle : "))
        taylorSeries = TaylorSeries(enterDegree, enterCountOfCycle)

        if enterOption == 1:
            print(bgColor.CBLACK, f"Sin :  {taylorSeries.sin()}")
        elif enterOption == 2:
            print(bgColor.CBLACK, f"Cos :  {taylorSeries.sin()}")
        elif enterOption == 3:
            enterX = float(input("Enter x : "))
            print(bgColor.CBLACK, f"Ln(x + 1) :  {taylorSeries.ln(enterX)}")
        elif enterOption == 4:
            print(bgColor.CBLACK, f"Arctan :  {taylorSeries.arctan()}")
        elif enterOption == 5:
            interrupter = False
            os.system("clear")


if __name__ == '__main__':
    main = Main()
