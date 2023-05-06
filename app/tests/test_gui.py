import os, sys
sys.path.append(os.path.abspath('./app'))
sys.path.append(os.path.abspath('./'))
from gui import GUI

def main():
    a = GUI()
    a.mainloop()

if __name__ == "__main__":
    main()