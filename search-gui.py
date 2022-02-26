from PyQt5 import QtCore, QtGui, QtWidgets
from Search import *
import pyvis.network
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 901)
        MainWindow.setStyleSheet("QToolTip\n"
                                 "{\n"
                                 "     border: 1px solid black;\n"
                                 "     background-color: #ffa02f;\n"
                                 "     padding: 1px;\n"
                                 "     border-radius: 3px;\n"
                                 "     opacity: 100;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView, QListView\n"
                                 "{\n"
                                 "    background-color: silver;\n"
                                 "    margin-left: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:hover\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
                                 "    color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:selected\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:selected\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "    border: 1px solid #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:pressed\n"
                                 "{\n"
                                 "    background: #444;\n"
                                 "    border: 1px solid #000;\n"
                                 "    background-color: QLinearGradient(\n"
                                 "        x1:0, y1:0,\n"
                                 "        x2:0, y2:1,\n"
                                 "        stop:1 #212121,\n"
                                 "        stop:0.4 #343434/*,\n"
                                 "        stop:0.2 #343434,\n"
                                 "        stop:0.1 #ffaa00*/\n"
                                 "    );\n"
                                 "    margin-bottom:-1px;\n"
                                 "    padding-bottom:1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu\n"
                                 "{\n"
                                 "    border: 1px solid #000;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item\n"
                                 "{\n"
                                 "    padding: 2px 20px 2px 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item:selected\n"
                                 "{\n"
                                 "    color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:disabled\n"
                                 "{\n"
                                 "    color: #808080;\n"
                                 "    background-color: #323232;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractItemView\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:focus\n"
                                 "{\n"
                                 "    /*border: 1px solid darkgray;*/\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
                                 "    padding: 1px;\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                 "    border-width: 1px;\n"
                                 "    border-color: #1e1e1e;\n"
                                 "    border-style: solid;\n"
                                 "    border-radius: 6;\n"
                                 "    padding: 3px;\n"
                                 "    font-size: 12px;\n"
                                 "    padding-left: 5px;\n"
                                 "    padding-right: 5px;\n"
                                 "    min-width: 40px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox\n"
                                 "{\n"
                                 "    selection-background-color: #ffaa00;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:hover,QPushButton:hover\n"
                                 "{\n"
                                 "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QComboBox:on\n"
                                 "{\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-left: 4px;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "    selection-background-color: #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView\n"
                                 "{\n"
                                 "    border: 2px solid darkgray;\n"
                                 "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down\n"
                                 "{\n"
                                 "     subcontrol-origin: padding;\n"
                                 "     subcontrol-position: top right;\n"
                                 "     width: 15px;\n"
                                 "\n"
                                 "     border-left-width: 0px;\n"
                                 "     border-left-color: darkgray;\n"
                                 "     border-left-style: solid; /* just a single line */\n"
                                 "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                 "     border-bottom-right-radius: 3px;\n"
                                 " }\n"
                                 "\n"
                                 "QComboBox::down-arrow\n"
                                 "{\n"
                                 "     image: url(:/dark_orange/img/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox\n"
                                 "{\n"
                                 "    border: 1px solid darkgray;\n"
                                 "    margin-top: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox:focus\n"
                                 "{\n"
                                 "    border: 1px solid darkgray;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit:focus\n"
                                 "{\n"
                                 "    border: 1px solid darkgray;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:horizontal {\n"
                                 "     border: 1px solid #222222;\n"
                                 "     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                 "     height: 7px;\n"
                                 "     margin: 0px 16px 0 16px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                 "      min-height: 20px;\n"
                                 "      border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:horizontal {\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "      width: 14px;\n"
                                 "      subcontrol-position: right;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal {\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "      width: 14px;\n"
                                 "     subcontrol-position: left;\n"
                                 "     subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
                                 "{\n"
                                 "      border: 1px solid black;\n"
                                 "      width: 1px;\n"
                                 "      height: 1px;\n"
                                 "      background: white;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                 "{\n"
                                 "      background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                 "      width: 7px;\n"
                                 "      margin: 16px 0 16px 0;\n"
                                 "      border: 1px solid #222222;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                 "      min-height: 20px;\n"
                                 "      border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical\n"
                                 "{\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "      height: 14px;\n"
                                 "      subcontrol-position: bottom;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:vertical\n"
                                 "{\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
                                 "      height: 14px;\n"
                                 "      subcontrol-position: top;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                 "{\n"
                                 "      border: 1px solid black;\n"
                                 "      width: 1px;\n"
                                 "      height: 1px;\n"
                                 "      background: white;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                 "{\n"
                                 "      background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QPlainTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section\n"
                                 "{\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:disabled\n"
                                 "{\n"
                                 "color: #414141;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::title\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button, QDockWidget::float-button\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 1px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
                                 "{\n"
                                 "    background: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
                                 "{\n"
                                 "    padding: 1px -1px -1px 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator\n"
                                 "{\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #4c4c4c;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator:hover\n"
                                 "{\n"
                                 "\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QToolBar::handle\n"
                                 "{\n"
                                 "     spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "     background: url(:/dark_orange/img/handle.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::separator\n"
                                 "{\n"
                                 "    height: 2px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    margin-left: 10px;\n"
                                 "    margin-right: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar\n"
                                 "{\n"
                                 "    border: 2px solid grey;\n"
                                 "    border-radius: 5px;\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar::chunk\n"
                                 "{\n"
                                 "    background-color: #d7801a;\n"
                                 "    width: 2.15px;\n"
                                 "    margin: 0.5px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab {\n"
                                 "    color: #b1b1b1;\n"
                                 "    border: 1px solid #444;\n"
                                 "    border-bottom-style: none;\n"
                                 "    background-color: #323232;\n"
                                 "    padding-left: 10px;\n"
                                 "    padding-right: 10px;\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    margin-right: -1px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget::pane {\n"
                                 "    border: 1px solid #444;\n"
                                 "    top: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:last\n"
                                 "{\n"
                                 "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:first:!selected\n"
                                 "{\n"
                                 " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "\n"
                                 "\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:!selected\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    border-bottom-style: solid;\n"
                                 "    margin-top: 3px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected\n"
                                 "{\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    margin-bottom: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:!selected:hover\n"
                                 "{\n"
                                 "    /*border-top: 2px solid #ffaa00;\n"
                                 "    padding-bottom: 3px;*/\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked\n"
                                 "{\n"
                                 "    background-color: qradialgradient(\n"
                                 "        cx: 0.5, cy: 0.5,\n"
                                 "        fx: 0.5, fy: 0.5,\n"
                                 "        radius: 1.0,\n"
                                 "        stop: 0.25 #ffaa00,\n"
                                 "        stop: 0.3 #323232\n"
                                 "    );\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    width: 9px;\n"
                                 "    height: 9px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator\n"
                                 "{\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
                                 "{\n"
                                 "    border: 1px solid #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked\n"
                                 "{\n"
                                 "    image:url(:/dark_orange/img/checkbox.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
                                 "{\n"
                                 "    border: 1px solid #444;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QSlider::groove:horizontal {\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    height: 8px;\n"
                                 "    background: #201F1F;\n"
                                 "    margin: 2px 0;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal {\n"
                                 "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 14px;\n"
                                 "    height: 14px;\n"
                                 "    margin: -4px 0;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:vertical {\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 8px;\n"
                                 "    background: #201F1F;\n"
                                 "    margin: 0 0px;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:vertical {\n"
                                 "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
                                 "      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 14px;\n"
                                 "    height: 14px;\n"
                                 "    margin: 0 -4px;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox {\n"
                                 "    padding-top: 2px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    border: 1px solid darkgray;\n"
                                 "\n"
                                 "    border-radius: 2px;\n"
                                 "    min-width: 50px;\n"
                                 "}\n"
                                 "\n"
                                 "")
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 50, 61, 31))
        self.label.setAutoFillBackground(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 50, 61, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 40, 141, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(770, 40, 141, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        with open("allCities.txt", 'r') as f:
            for k in f:
                self.comboBox.addItem("")
                self.comboBox_2.addItem("")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(19, 360, 1091, 501))
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 90, 1101, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.bfs = QtWidgets.QPushButton(self.centralwidget)
        self.bfs.setGeometry(QtCore.QRect(370, 120, 93, 28))
        self.bfs.setObjectName("bfs")
        self.ucs = QtWidgets.QPushButton(self.centralwidget)
        self.ucs.setGeometry(QtCore.QRect(510, 120, 93, 28))
        self.ucs.setObjectName("ucs")
        self.its = QtWidgets.QPushButton(self.centralwidget)
        self.its.setGeometry(QtCore.QRect(650, 120, 93, 28))
        self.its.setObjectName("its")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 170, 1101, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 300, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 300, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(760, 300, 55, 16))
        self.label_6.setObjectName("label_6")
        self.path = QtWidgets.QTextBrowser(self.centralwidget)
        self.path.setEnabled(True)
        self.path.setGeometry(QtCore.QRect(150, 190, 921, 71))
        self.path.setObjectName("path")
        self.distance = QtWidgets.QTextBrowser(self.centralwidget)
        self.distance.setEnabled(True)
        self.distance.setGeometry(QtCore.QRect(150, 280, 222, 40))
        self.distance.setObjectName("distance")
        self.total = QtWidgets.QTextBrowser(self.centralwidget)
        self.total.setEnabled(True)
        self.total.setGeometry(QtCore.QRect(500, 280, 222, 40))
        self.total.setObjectName("total")
        self.max = QtWidgets.QTextBrowser(self.centralwidget)
        self.max.setEnabled(True)
        self.max.setGeometry(QtCore.QRect(850, 280, 222, 40))
        self.max.setObjectName("max")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "search methods"))
        self.label.setText(_translate("MainWindow", "city 1"))
        self.label_2.setText(_translate("MainWindow", "city 2"))
        self.bfs.setText(_translate("MainWindow", "BFS"))
        self.ucs.setText(_translate("MainWindow", "UCS"))
        self.its.setText(_translate("MainWindow", "IDS"))
        self.label_3.setText(_translate("MainWindow", "Path:"))
        self.label_4.setText(_translate("MainWindow", "Distance"))
        self.label_5.setText(_translate("MainWindow", "Total"))
        self.label_6.setText(_translate("MainWindow", "Max"))
        self.path.setFontPointSize(15)
        self.distance.setFontPointSize(15)
        self.total.setFontPointSize(15)
        self.max.setFontPointSize(15)

        counter = -1
        with open("allCities.txt", 'r') as f:
            for k in f:
                counter = counter + 1
                self.comboBox.setItemText(counter, _translate("MainWindow", k.strip()))
                self.comboBox_2.setItemText(counter, _translate("MainWindow", k.strip()))
        self.bfs.clicked.connect(lambda: self.bfsMethod())
        self.ucs.clicked.connect(lambda: self.ucsMethod())
        self.its.clicked.connect(lambda: self.itsMethod())

    def bfsMethod(self):
        nameOfGraph = "bfs.html"
        pyvis_graph = pyvis.network.Network(notebook=True, height="100%", width="100%", bgcolor="#222222",
                                            font_color="#FFFFFF")
        a, b, c, d = BreadthFirstSearch(dict_graph, self.comboBox.currentText(), self.comboBox_2.currentText())

        with open("cities.txt", 'r') as f:
            for l in f:
                color = "red"
                color1 = "red"
                color2 = "red"
                x, y, z = l.split()
                if x in a:
                    color1 = "green"
                if y in a:
                    color2 = "green"
                pyvis_graph.add_node(x, label=x, title=x, color=color1)
                pyvis_graph.add_node(y, label=y, title=y, color=color2)
                if x in a and y in a:
                    color = "green"
                pyvis_graph.add_edge(x, y, label=z, title=z, color=color)
        # t = "Path: {n1} ,distance: {n2} ,total: {n3} ,max: {n4}".format(n1=a, n2=b, n3=c, n4=d)
        pyvis_graph.force_atlas_2based()
        pyvis_graph.show(nameOfGraph)
        self.path.setPlainText(str(a))
        self.distance.setPlainText(str(b))
        self.total.setPlainText(str(c))
        self.max.setPlainText(str(d))
        directory = os.getcwd()
        directory = directory.replace('\\', '/')
        print(directory)
        url = "file:///{dir}/{name}".format(dir=directory, name=nameOfGraph)
        self.widget.setUrl(QtCore.QUrl(url))

    def ucsMethod(self):
        nameOfGraph = "ucs.html"
        pyvis_graph = pyvis.network.Network(notebook=True, height="100%", width="100%", bgcolor="#222222",
                                            font_color="#FFFFFF")
        a, b, c, d = ucs(dict_graph, self.comboBox.currentText(), self.comboBox_2.currentText())

        with open("cities.txt", 'r') as f:
            for l in f:
                color = "red"
                color1 = "red"
                color2 = "red"
                x, y, z = l.split()
                if x in a:
                    color1 = "green"
                if y in a:
                    color2 = "green"
                pyvis_graph.add_node(x, label=x, title=x, color=color1)
                pyvis_graph.add_node(y, label=y, title=y, color=color2)
                if x in a and y in a:
                    color = "green"
                pyvis_graph.add_edge(x, y, label=z, title=z, color=color)
        # t = "Path: {n1} ,distance: {n2} ,total: {n3} ,max: {n4}".format(n1=a, n2=b, n3=c, n4=d)
        # t = t.replace("Path:",termcolor.colored("Path:","blue"))
        # t = t.replace("distance:",termcolor.colored("distance:","blue"))
        # t = t.replace("total:",termcolor.colored("total:","blue"))
        # t = t.replace("max:",termcolor.colored("max:","blue"))
        # print(t)
        pyvis_graph.force_atlas_2based()
        pyvis_graph.show(nameOfGraph)
        # self.textEdit.setPlainText(t)
        self.path.setPlainText(str(a))
        self.distance.setPlainText(str(b))
        self.total.setPlainText(str(c))
        self.max.setPlainText(str(d))
        directory = os.getcwd()
        directory = directory.replace('\\', '/')
        print(directory)
        url = "file:///{dir}/{name}".format(dir=directory, name=nameOfGraph)
        self.widget.setUrl(QtCore.QUrl(url))

    def itsMethod(self):
        nameOfGraph = "its.html"
        pyvis_graph = pyvis.network.Network(notebook=True, height="100%", width="100%", bgcolor="#222222",
                                            font_color="#FFFFFF")
        a, b, c, d = IterativeDeepening(dict_graph, self.comboBox.currentText(), self.comboBox_2.currentText())

        with open("cities.txt", 'r') as f:
            for l in f:
                color = "red"
                color1 = "red"
                color2 = "red"
                x, y, z = l.split()
                if x in a:
                    color1 = "green"
                if y in a:
                    color2 = "green"
                pyvis_graph.add_node(x, label=x, title=x, color=color1)
                pyvis_graph.add_node(y, label=y, title=y, color=color2)
                if x in a and y in a:
                    color = "green"
                pyvis_graph.add_edge(x, y, label=z, title=z, color=color)
        # t = "Path: {n1} ,distance: {n2} ,total: {n3} ,max: {n4}".format(n1=a, n2=b, n3=c, n4=d)
        pyvis_graph.force_atlas_2based()
        pyvis_graph.show(nameOfGraph)
        # self.textEdit.setPlainText(t)
        self.path.setPlainText(str(a))
        self.distance.setPlainText(str(b))
        self.total.setPlainText(str(c))
        self.max.setPlainText(str(d))
        directory = os.getcwd()
        directory = directory.replace('\\', '/')
        print(directory)
        url = "file:///{dir}/{name}".format(dir= directory,name=nameOfGraph)
        self.widget.setUrl(QtCore.QUrl(url))


from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
