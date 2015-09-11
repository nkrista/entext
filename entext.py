"""
A simple text editor with font options.
"""

import sys
from PyQt4 import QtGui

class Editor(QtGui.QMainWindow):
	
	def __init__(self):
		super(Editor, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.text = QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)
		self.setWindowTitle("EnText")
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fontMenu = menubar.addMenu('&Font')
		
		openFile = QtGui.QAction('Open...', self)
		openFile.setShortcut('Ctrl+o')
		openFile.triggered.connect(self.fileOpener)
		
		saveFile = QtGui.QAction('Save As...', self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.triggered.connect(self.fileSaver)
		
		chooseFont = QtGui.QAction('Font...', self)
		chooseFont.triggered.connect(self.fontChooser)
		chooseFont.setShortcut('Shift+Ctrl+F')
		
		fileMenu.addAction(openFile)
		fileMenu.addAction(saveFile)
		fontMenu.addAction(chooseFont)
		
		self.resize(1000,1000)
		# self.move(1,1)
		self.center()
		self.show()
		
	def center(self):
		
		frame_g = self.frameGeometry()
		centre = QtGui.QDesktopWidget().availableGeometry().center()
		self.move(frame_g.topLeft())
		
	def fileOpener(self):
	
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', \
                '/home')
		
		chosen_file = open(filename, 'r')
		
		with chosen_file:
			data = chosen_file.read()
			self.textEdit.setText(data)
			
	def fileSaver(self):
		savename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
		outfile = open(savename, 'w')
		data = self.txt.toPlainText()
		outfile.write(data)
		outfile.close()
			
	def fontChooser(self):
		
		font, ok = QtGui.QFontDialog.getFont()
		
		if ok:
			self.text.setFont(font)
			# self.text.setCurrentFont(font)
	
def main():
	app = QtGui.QApplication(sys.argv)
	textedit = Editor()
	sys.exit(app.exec_())
	

if __name__ == '__main__':
	main()
	
