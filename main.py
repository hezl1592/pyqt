import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.Ui_window import Ui_Dialog


class MyMainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.create_items()

    def start_process(self):
        print("x")
        self.show_list()

    def show_list(self):
        select_list = self.listWidget.selectedItems()
        for select_item in select_list:
            print(select_item.text())

    def create_items(self):
        self.listWidget.setSortingEnabled(False)
        for i in range(9):
            self.listWidget.addItem("item{}".format(i))
        self.listWidget.setSortingEnabled(self.listWidget.isSortingEnabled())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
