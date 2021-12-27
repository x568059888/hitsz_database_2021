# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 14pt \"宋体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 12pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.current_username_label = QtWidgets.QLabel(self.centralwidget)
        self.current_username_label.setStyleSheet("font: 12pt \"宋体\";")
        self.current_username_label.setObjectName("current_username_label")
        self.horizontalLayout.addWidget(self.current_username_label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 12pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.current_role_label = QtWidgets.QLabel(self.centralwidget)
        self.current_role_label.setStyleSheet("font: 12pt \"宋体\";")
        self.current_role_label.setObjectName("current_role_label")
        self.horizontalLayout.addWidget(self.current_role_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line_2.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(1, 5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "肘，跟我干饭！"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Menu"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "👀 主页"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "🍚 点餐"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "🏪 荔园一食堂"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "一楼"))
        self.treeWidget.topLevelItem(1).child(0).child(0).child(0).setText(0, _translate("MainWindow", "🐠 酸菜鱼"))
        self.treeWidget.topLevelItem(1).child(0).child(0).child(1).setText(0, _translate("MainWindow", "🥗 西北风味"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "🏪 荔园二食堂"))
        self.treeWidget.topLevelItem(1).child(1).child(0).setText(0, _translate("MainWindow", "一楼"))
        self.treeWidget.topLevelItem(1).child(1).child(0).child(0).setText(0, _translate("MainWindow", "🍮 豆花"))
        self.treeWidget.topLevelItem(1).child(1).child(0).child(1).setText(0, _translate("MainWindow", "🥘 经典小炒"))
        self.treeWidget.topLevelItem(1).child(1).child(1).setText(0, _translate("MainWindow", "二楼"))
        self.treeWidget.topLevelItem(1).child(1).child(1).child(0).setText(0, _translate("MainWindow", "👨🏻‍🍳 东北菜"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "💰 订单管理"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "🔍 关于"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "🥳 Help yourself!"))
        self.label_2.setText(_translate("MainWindow", "用户:"))
        self.current_username_label.setText(_translate("MainWindow", "张三"))
        self.label_4.setText(_translate("MainWindow", "角色:"))
        self.current_role_label.setText(_translate("MainWindow", "普通用户"))
        self.pushButton.setText(_translate("MainWindow", "返回"))