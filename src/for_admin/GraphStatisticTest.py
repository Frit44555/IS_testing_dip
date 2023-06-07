from PyQt5.QtWidgets import QWidget, QVBoxLayout  # , QApplication
# import sys

import pyqtgraph as pg


class GraphStatisticTest(QWidget):
    def __init__(self, ordinate, parent=None):
        super().__init__(parent)

        # Переменные________________________________
        ordinate = [i * 100 for i in ordinate]
        abscissa = [i for i in range(1, len(ordinate) + 1)]
        # ________________________________

        # Объекты компоновки________________________________
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.setObjectName("vertical_layout")
        # ________________________________

        # ________________________________График________________________________

        self.__plot = pg.plot()

        # Стилизация________________________________
        self.__plot.setBackground('w')
        styles = {'color': 'black', 'font-size': '13px'}
        self.__plot.setLabel('left', 'Процент решивших', **styles)
        self.__plot.setLabel('bottom', 'Задания', **styles)
        self.__plot.showGrid(x=False, y=True)
        self.__plot.setYRange(0, 100)
        # ________________________________

        # Создал pyqt5graph гистограмма  (bar graph)
        # ширина = 0.6
        # цвет = orange
        bargraph = pg.BarGraphItem(x=abscissa, height=ordinate, width=0.6, brush='orange')

        # добавил гистограмму на график
        self.__plot.addItem(bargraph)

        # добавил на layout
        self.vertical_layout.addWidget(self.__plot)

# if __name__ == '__main__':
#     # create pyqt5 app
#     App = QApplication(sys.argv)
#
#     # create list for y-axis
#     y = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
#
#     # create horizontal list i.e x-axis
#     x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     # create the instance of our Window
#     window = GraphStatisticTest(x, y)
#     window.show()
#
#     # start the app
#     sys.exit(App.exec())
