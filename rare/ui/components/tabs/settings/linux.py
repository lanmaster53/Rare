# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/settings/linux.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LinuxSettings(object):
    def setupUi(self, LinuxSettings):
        LinuxSettings.setObjectName("LinuxSettings")
        LinuxSettings.resize(109, 138)
        self.linux_layout = QtWidgets.QVBoxLayout(LinuxSettings)
        self.linux_layout.setObjectName("linux_layout")
        self.wine_groupbox = QtWidgets.QGroupBox(LinuxSettings)
        self.wine_groupbox.setObjectName("wine_groupbox")
        self.wine_layout = QtWidgets.QFormLayout(self.wine_groupbox)
        self.wine_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wine_layout.setObjectName("wine_layout")
        self.prefix_label = QtWidgets.QLabel(self.wine_groupbox)
        self.prefix_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prefix_label.setObjectName("prefix_label")
        self.wine_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.prefix_label)
        self.prefix_layout = QtWidgets.QVBoxLayout()
        self.prefix_layout.setObjectName("prefix_layout")
        self.wine_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.prefix_layout)
        self.exec_label = QtWidgets.QLabel(self.wine_groupbox)
        self.exec_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.exec_label.setObjectName("exec_label")
        self.wine_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.exec_label)
        self.exec_layout = QtWidgets.QVBoxLayout()
        self.exec_layout.setObjectName("exec_layout")
        self.wine_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.exec_layout)
        self.linux_layout.addWidget(self.wine_groupbox)
        self.overlay_layout = QtWidgets.QVBoxLayout()
        self.overlay_layout.setObjectName("overlay_layout")
        self.linux_layout.addLayout(self.overlay_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.linux_layout.addItem(spacerItem)

        self.retranslateUi(LinuxSettings)
        QtCore.QMetaObject.connectSlotsByName(LinuxSettings)

    def retranslateUi(self, LinuxSettings):
        _translate = QtCore.QCoreApplication.translate
        LinuxSettings.setWindowTitle(_translate("LinuxSettings", "LinuxSettings"))
        self.wine_groupbox.setTitle(_translate("LinuxSettings", "Wine Settings"))
        self.prefix_label.setText(_translate("LinuxSettings", "Prefix"))
        self.exec_label.setText(_translate("LinuxSettings", "Executable"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LinuxSettings = QtWidgets.QWidget()
    ui = Ui_LinuxSettings()
    ui.setupUi(LinuxSettings)
    LinuxSettings.show()
    sys.exit(app.exec_())
