# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RareSettings(object):
    def setupUi(self, RareSettings):
        RareSettings.setObjectName("RareSettings")
        self.layout_rare = QtWidgets.QGridLayout(RareSettings)
        self.layout_rare.setObjectName("layout_rare")
        self.gb_img_dir = QtWidgets.QGroupBox(RareSettings)
        self.gb_img_dir.setObjectName("gb_img_dir")
        self.layout_img_dir = QtWidgets.QVBoxLayout(self.gb_img_dir)
        self.layout_img_dir.setObjectName("layout_img_dir")
        self.layout_rare.addWidget(self.gb_img_dir, 0, 0, 1, 1)
        self.gb_lang = QtWidgets.QGroupBox(RareSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_lang.sizePolicy().hasHeightForWidth())
        self.gb_lang.setSizePolicy(sizePolicy)
        self.gb_lang.setObjectName("gb_lang")
        self.layout_lang = QtWidgets.QVBoxLayout(self.gb_lang)
        self.layout_lang.setObjectName("layout_lang")
        self.select_lang = QtWidgets.QComboBox(self.gb_lang)
        self.select_lang.setObjectName("select_lang")
        self.layout_lang.addWidget(self.select_lang, 0, QtCore.Qt.AlignTop)
        self.info_lang = QtWidgets.QLabel(self.gb_lang)
        font = QtGui.QFont()
        font.setItalic(True)
        self.info_lang.setFont(font)
        self.info_lang.setWordWrap(True)
        self.info_lang.setObjectName("info_lang")
        self.layout_lang.addWidget(self.info_lang, 0, QtCore.Qt.AlignTop)
        self.layout_rare.addWidget(self.gb_lang, 0, 1, 1, 1)
        self.gb_settings = QtWidgets.QGroupBox(RareSettings)
        self.gb_settings.setObjectName("gb_settings")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_settings)
        self.gridLayout.setObjectName("gridLayout")
        self.auto_update = QtWidgets.QCheckBox(self.gb_settings)
        self.auto_update.setObjectName("auto_update")
        self.gridLayout.addWidget(self.auto_update, 1, 0, 1, 1)
        self.confirm_start = QtWidgets.QCheckBox(self.gb_settings)
        self.confirm_start.setObjectName("confirm_start")
        self.gridLayout.addWidget(self.confirm_start, 2, 0, 1, 1)
        self.sys_tray = QtWidgets.QCheckBox(self.gb_settings)
        self.sys_tray.setObjectName("sys_tray")
        self.gridLayout.addWidget(self.sys_tray, 0, 0, 1, 1)
        self.notification = QtWidgets.QCheckBox(self.gb_settings)
        self.notification.setObjectName("notification")
        self.gridLayout.addWidget(self.notification, 0, 1, 1, 1)
        self.auto_sync_cloud = QtWidgets.QCheckBox(self.gb_settings)
        self.auto_sync_cloud.setObjectName("auto_sync_cloud")
        self.gridLayout.addWidget(self.auto_sync_cloud, 3, 0, 1, 1)
        self.save_size = QtWidgets.QCheckBox(self.gb_settings)
        self.save_size.setObjectName("save_size")
        self.gridLayout.addWidget(self.save_size, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 4, 1)
        self.layout_rare.addWidget(self.gb_settings, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_rare.addItem(spacerItem1, 3, 0, 1, 2)
        self.layout_rpc = QtWidgets.QVBoxLayout()
        self.layout_rpc.setObjectName("layout_rpc")
        self.layout_rare.addLayout(self.layout_rpc, 1, 1, 1, 1)
        self.log_dir_group = QtWidgets.QGroupBox(RareSettings)
        self.log_dir_group.setObjectName("log_dir_group")
        self.log_dir_layout = QtWidgets.QVBoxLayout(self.log_dir_group)
        self.log_dir_layout.setObjectName("log_dir_layout")
        self.log_dir_open_button = QtWidgets.QPushButton(self.log_dir_group)
        self.log_dir_open_button.setObjectName("log_dir_open_button")
        self.log_dir_layout.addWidget(self.log_dir_open_button)
        self.log_dir_clean_button = QtWidgets.QPushButton(self.log_dir_group)
        self.log_dir_clean_button.setObjectName("log_dir_clean_button")
        self.log_dir_layout.addWidget(self.log_dir_clean_button)
        self.log_dir_size_label = QtWidgets.QLabel(self.log_dir_group)
        self.log_dir_size_label.setText("")
        self.log_dir_size_label.setWordWrap(True)
        self.log_dir_size_label.setObjectName("log_dir_size_label")
        self.log_dir_layout.addWidget(self.log_dir_size_label)
        self.layout_rare.addWidget(self.log_dir_group, 2, 1, 1, 1)

        self.retranslateUi(RareSettings)
        QtCore.QMetaObject.connectSlotsByName(RareSettings)

    def retranslateUi(self, RareSettings):
        _translate = QtCore.QCoreApplication.translate
        RareSettings.setWindowTitle(_translate("RareSettings", "RareSettings"))
        self.gb_img_dir.setTitle(_translate("RareSettings", "Image Cache Directory"))
        self.gb_lang.setTitle(_translate("RareSettings", "Language"))
        self.info_lang.setText(_translate("RareSettings", "Restart Rare to apply the new settings."))
        self.gb_settings.setTitle(_translate("RareSettings", "Behaviour"))
        self.auto_update.setText(_translate("RareSettings", "Update games on application startup"))
        self.confirm_start.setText(_translate("RareSettings", "Confirm game launch"))
        self.sys_tray.setText(_translate("RareSettings", "Exit to System tray"))
        self.notification.setText(_translate("RareSettings", "Show notification on download completion"))
        self.auto_sync_cloud.setText(_translate("RareSettings", "Automatically sync with cloud"))
        self.save_size.setText(_translate("RareSettings", "Restore window size on application startup"))
        self.log_dir_group.setTitle(_translate("RareSettings", "Logs"))
        self.log_dir_open_button.setText(_translate("RareSettings", "Open Log directory"))
        self.log_dir_clean_button.setText(_translate("RareSettings", "Clean Log directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RareSettings = QtWidgets.QWidget()
    ui = Ui_RareSettings()
    ui.setupUi(RareSettings)
    RareSettings.show()
    sys.exit(app.exec_())
