import random

from sys import argv
from PyQt4.QtGui import QApplication

from pyqt.main_window import AsteroidsMainWindow
from util.config import ConfigManager, FontManager


def start_pyasteroids():
    random.seed()
    
    app = QApplication(argv)
    
    # Load the config files in memory 
    ConfigManager()
    
    # Add the custom fonts to the Qt database
    FontManager()

    # Creates the window (GLWidget is created there)
    win = AsteroidsMainWindow()

    # Pop-up the window    
    win.show()

    # Faster processing
    try:
        import psyco
        psyco.full()
    except:
        print 'You currently do not have the Psyco module in your PYTHONPATH.'
        print 'It is highly advisable to install it for a much better gaming performance.'
        print 'Official site: http://psyco.sourceforge.net/'

    # Gives control to Qt
    app.exec_()
    

if __name__ == '__main__':
    print '# PyAsteroids3D #\n'
    
    start_pyasteroids()
    
    print 'Leaving...'
    