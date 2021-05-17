import sys
from PyQt5.QtWidgets import *
from methods.FacialRecognition import *

def main():
    for i in sys.path:
        print(i)
        
    if __name__ == "__main__":        
        app = QApplication(sys.argv)
        MainWindow = Ui_MainWindow()
        MainWindow.show() 
        sys.exit(app.exec_())
main()
