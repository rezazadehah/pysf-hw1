import colorama
from colorama import Back, Style

colorama.init(autoreset=True)

#background = BLUE


def sky():
    print(Back.LIGHTBLUE_EX + " " * 100)
    print(Back.LIGHTBLUE_EX + " " * 100)
    print(Back.LIGHTBLUE_EX + " " * 100)
    print(Back.LIGHTBLUE_EX + " " * 100)
    print(Back.LIGHTBLUE_EX + " " * 100)
    print(Back.LIGHTBLUE_EX + " " * 100)
def roof():
    print(Back.LIGHTBLUE_EX + " "*48 + Back.RED +" "*4 + Back.LIGHTBLUE_EX + " "*48)
    print(Back.LIGHTBLUE_EX + " "*45 + Back.RED +" "*10 + Back.LIGHTBLUE_EX + " "*45)
    print(Back.LIGHTBLUE_EX + " "*42 + Back.RED +" "*16 + Back.LIGHTBLUE_EX + " "*42)
    print(Back.LIGHTBLUE_EX + " "*40 + Back.RED +" "*20 + Back.LIGHTBLUE_EX + " "*40)
    print(Back.LIGHTBLUE_EX + " "*37 + Back.RED +" "*26 + Back.LIGHTBLUE_EX+" "*37)
    print(Back.LIGHTBLUE_EX + " "*34 + Back.RED +" "*32 + Back.LIGHTBLUE_EX+" "*34)
    print(Back.LIGHTBLUE_EX + " "*31 + Back.RED +" "*38 + Back.LIGHTBLUE_EX+" "*31)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.RED +" "*40 + Back.LIGHTBLUE_EX+" "*30)

def body():
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*24 +Back.YELLOW +" "*10 + Back.LIGHTMAGENTA_EX +" "*6+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*24 +Back.YELLOW +" "*10 + Back.LIGHTMAGENTA_EX +" "*6+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*24 +Back.YELLOW +" "*10 + Back.LIGHTMAGENTA_EX +" "*6+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*24 +Back.YELLOW +" "*10 + Back.LIGHTMAGENTA_EX +" "*6+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*40 + Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*6 +Back.LIGHTYELLOW_EX +" "*10 + Back.LIGHTMAGENTA_EX +" "*24+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*6 +Back.LIGHTYELLOW_EX +" "*10 + Back.LIGHTMAGENTA_EX +" "*24+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*6 +Back.LIGHTYELLOW_EX +" "*10 + Back.LIGHTMAGENTA_EX +" "*24+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*6 +Back.LIGHTYELLOW_EX +" "*10 + Back.LIGHTMAGENTA_EX +" "*24+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*6 +Back.LIGHTYELLOW_EX +" "*10 + Back.LIGHTMAGENTA_EX +" "*24+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.LIGHTBLUE_EX + " "*30 + Back.LIGHTMAGENTA_EX +" "*6 +Back.LIGHTYELLOW_EX +" "*10 + Back.LIGHTMAGENTA_EX +" "*24+ Back.LIGHTBLUE_EX+" "*30)
    print(Back.GREEN + " "*30 + Back.LIGHTMAGENTA_EX +" "*6 +Back.LIGHTYELLOW_EX +" "*10 + Back.LIGHTMAGENTA_EX +" "*24+ Back.GREEN+" "*30)

def gnd():
    print(Back.GREEN + " "*32 +Back.BLACK +" "*18 + Back.GREEN+" "*50)
    print(Back.GREEN + " "*34 +Back.BLACK +" "*14 + Back.GREEN+" "*52)
    print(Back.GREEN + " "*36 +Back.BLACK +" "*10 + Back.GREEN+" "*54)
    print(Back.GREEN + " " * 100)
    print(Back.GREEN + " " * 100)
    print(Back.GREEN + " " * 100)
    print(Back.GREEN + " " * 100)
    print(Back.GREEN + " " * 100)
    

sky()
roof()
body()
gnd()