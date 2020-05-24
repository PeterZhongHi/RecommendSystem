# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecommendFast.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./image/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.display_result_label = QtWidgets.QTextBrowser(self.groupBox_2)
        self.display_result_label.setObjectName("display_result_label")
        self.gridLayout_2.addWidget(self.display_result_label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 3)
        self.row_read_times_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.row_read_times_spinBox.setObjectName("row_read_times_spinBox")
        self.gridLayout_3.addWidget(self.row_read_times_spinBox, 3, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(74, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 4, 0, 1, 2)
        self.select_algo_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.select_algo_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.select_algo_comboBox.setAutoFillBackground(False)
        self.select_algo_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.select_algo_comboBox.setObjectName("select_algo_comboBox")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.select_algo_comboBox.addItem("")
        self.gridLayout_3.addWidget(self.select_algo_comboBox, 0, 1, 1, 3)
        self.display_process_label = QtWidgets.QTextBrowser(self.groupBox)
        self.display_process_label.setObjectName("display_process_label")
        self.gridLayout_3.addWidget(self.display_process_label, 5, 0, 1, 4)
        self.config_ok_btn = QtWidgets.QPushButton(self.groupBox)
        self.config_ok_btn.setObjectName("config_ok_btn")
        self.gridLayout_3.addWidget(self.config_ok_btn, 4, 3, 1, 1)
        self.mse_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.mse_checkBox.setChecked(True)
        self.mse_checkBox.setObjectName("mse_checkBox")
        self.gridLayout_3.addWidget(self.mse_checkBox, 2, 1, 1, 1)
        self.fcp_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.fcp_checkBox.setObjectName("fcp_checkBox")
        self.gridLayout_3.addWidget(self.fcp_checkBox, 2, 3, 1, 1)
        self.rmse_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.rmse_checkBox.setChecked(True)
        self.rmse_checkBox.setObjectName("rmse_checkBox")
        self.gridLayout_3.addWidget(self.rmse_checkBox, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.mae_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.mae_checkBox.setObjectName("mae_checkBox")
        self.gridLayout_3.addWidget(self.mae_checkBox, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.import_data_btn = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./image/图标-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_data_btn.setIcon(icon1)
        self.import_data_btn.setObjectName("import_data_btn")
        self.select_model_btn = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./image/图标-03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_model_btn.setIcon(icon2)
        self.select_model_btn.setObjectName("select_model_btn")
        self.recommed_result_btn = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./image/图标-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recommed_result_btn.setIcon(icon3)
        self.recommed_result_btn.setObjectName("recommed_result_btn")
        self.clean_context_btn = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./image/图标-07.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clean_context_btn.setIcon(icon4)
        self.clean_context_btn.setObjectName("clean_context_btn")
        self.save_result_btn = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./image/图标-04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_result_btn.setIcon(icon5)
        self.save_result_btn.setObjectName("save_result_btn")
        self.need_help_btn = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./image/图标-08.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.need_help_btn.setIcon(icon6)
        self.need_help_btn.setObjectName("need_help_btn")
        self.toolBar.addAction(self.import_data_btn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.select_model_btn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.recommed_result_btn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.save_result_btn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.clean_context_btn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.need_help_btn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recommender"))
        self.groupBox_2.setTitle(_translate("MainWindow", "显示结果"))
        self.groupBox.setTitle(_translate("MainWindow", "系统配置"))
        self.label_2.setText(_translate("MainWindow", "隔行读取次数："))
        self.select_algo_comboBox.setItemText(0, _translate("MainWindow", "SVD"))
        self.select_algo_comboBox.setItemText(1, _translate("MainWindow", "SVD++"))
        self.select_algo_comboBox.setItemText(2, _translate("MainWindow", "NMF"))
        self.select_algo_comboBox.setItemText(3, _translate("MainWindow", "Slope One"))
        self.select_algo_comboBox.setItemText(4, _translate("MainWindow", "k-NN"))
        self.select_algo_comboBox.setItemText(5, _translate("MainWindow", "Centered k-NN"))
        self.select_algo_comboBox.setItemText(6, _translate("MainWindow", "k-NN Baseline"))
        self.select_algo_comboBox.setItemText(7, _translate("MainWindow", "Co-Clustering"))
        self.select_algo_comboBox.setItemText(8, _translate("MainWindow", "Baseline"))
        self.select_algo_comboBox.setItemText(9, _translate("MainWindow", "Random"))
        self.config_ok_btn.setText(_translate("MainWindow", "确认"))
        self.mse_checkBox.setText(_translate("MainWindow", "mse"))
        self.fcp_checkBox.setText(_translate("MainWindow", "fcp"))
        self.rmse_checkBox.setText(_translate("MainWindow", "rmse"))
        self.label_3.setText(_translate("MainWindow", "评价指标："))
        self.mae_checkBox.setText(_translate("MainWindow", "mae"))
        self.label.setText(_translate("MainWindow", "推荐模型："))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.import_data_btn.setText(_translate("MainWindow", "导入数据"))
        self.import_data_btn.setToolTip(_translate("MainWindow", "导入数据"))
        self.select_model_btn.setText(_translate("MainWindow", "生成模型"))
        self.select_model_btn.setToolTip(_translate("MainWindow", "生成模型"))
        self.recommed_result_btn.setText(_translate("MainWindow", "推荐结果"))
        self.recommed_result_btn.setToolTip(_translate("MainWindow", "推荐结果"))
        self.clean_context_btn.setText(_translate("MainWindow", "清空内容"))
        self.clean_context_btn.setToolTip(_translate("MainWindow", "清空内容"))
        self.save_result_btn.setText(_translate("MainWindow", "保存结果"))
        self.save_result_btn.setToolTip(_translate("MainWindow", "保存结果"))
        self.need_help_btn.setText(_translate("MainWindow", "获取帮助"))
        self.need_help_btn.setToolTip(_translate("MainWindow", "获取帮助"))
