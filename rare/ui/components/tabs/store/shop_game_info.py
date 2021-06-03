# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop_game_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shop_info(object):
    def setupUi(self, shop_info):
        shop_info.setObjectName("shop_info")
        shop_info.resize(702, 468)
        self.gridLayout = QtWidgets.QGridLayout(shop_info)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(shop_info)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.price = QtWidgets.QLabel(shop_info)
        self.price.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 1, 1, 1, 1)
        self.title = QtWidgets.QLabel(shop_info)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.image = QtWidgets.QLabel(shop_info)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.dev = QtWidgets.QLabel(shop_info)
        self.dev.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dev.setObjectName("dev")
        self.gridLayout.addWidget(self.dev, 2, 1, 1, 1)

        self.retranslateUi(shop_info)
        QtCore.QMetaObject.connectSlotsByName(shop_info)

    def retranslateUi(self, shop_info):
        _translate = QtCore.QCoreApplication.translate
        shop_info.setWindowTitle(_translate("shop_info", "Form"))
        self.pushButton.setText(_translate("shop_info", "Buy Game in Epic Games Store"))
        self.price.setText(_translate("shop_info", "TextLabel"))
        self.title.setText(_translate("shop_info", "Error"))
        self.image.setText(_translate("shop_info", "TextLabel"))
        self.dev.setText(_translate("shop_info", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shop_info = QtWidgets.QWidget()
    ui = Ui_shop_info()
    ui.setupUi(shop_info)
    shop_info.show()
    sys.exit(app.exec_())
