#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt4 import  QtGui


class Dialog(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()

        self.createMenu()
        
        
        

        self.mainLayout = QtGui.QVBoxLayout()
        
        self.mainLayout.setMenuBar(self.menuBar)
        
        w1=self.createGridGroupBox()
        w2=self.createGridGroupBox()
        w3=self.createGridGroupBox()
        w4=self.createGridGroupBox()
        w5=self.createGridGroupBox()
        
        
        
        
        myAwesomeScrollArea = QtGui.QScrollArea()
        myAwesomeScrollArea.setWidgetResizable(True)
        myAwesomeScrollArea.setEnabled(True)
        myAwesomeScrollArea.setMaximumSize(375, 300)  # optional
        
        
        self.mainLayout.addWidget(w1)
        self.mainLayout.addWidget(w2)
        self.mainLayout.addWidget(w3)
        self.mainLayout.addWidget(w4)
        self.mainLayout.addWidget(w5)
        
        self.mainLayout.addWidget(myAwesomeScrollArea)
        
        
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Basic Layouts")

    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()
        

    def createGridGroupBox(self):
        gridGroupBox = QtGui.QGroupBox("Grid layout")
        layout = QtGui.QGridLayout()

        for i in range(Dialog.NumGridRows):
            label = QtGui.QLabel("Line %d:" % (i + 1))
            lineEdit = QtGui.QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(lineEdit, i + 1, 1)

        smallEditor = QtGui.QTextEdit()
        smallEditor.setPlainText("This widget takes up about two thirds ""of the grid layout.")

        layout.addWidget(smallEditor, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        gridGroupBox.setLayout(layout)
        
        return gridGroupBox
        
        


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
