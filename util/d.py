import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

pg.mkQApp()
pw = pg.PlotWidget()
pw.setWindowTitle('pyqtgraph example: MultiplePlotAxes')
pw.show()

#--- prepare viewboxes ---
pi_1 = pw.plotItem
vb_1 = pi_1.getViewBox() # use original viewbox
vb_1.setBorder('#777')
vb_2 = pg.ViewBox() # prepare additional viewbox 2
vb_3 = pg.ViewBox()
pi_1.scene().addItem(vb_2)
pi_1.scene().addItem(vb_3)

#--- prepare all axes in the layout of PlotItem pi_1 ---
ax_x = pi_1.getAxis('bottom')
ax_x.setLabel('x-axis')
ax_x.setLogMode(True)

pi_1.getAxis('left').hide() # we are putting all y-axes on the right, so we do not need this one.
ax_1 = pi_1.getAxis('right') # use original right axis of pi_1
ax_1.setLabel('linear axis 1', color='#e33')
ax_1.setLogMode(False)
ax_1.show() # the right side axis is hidden by default

ax_2 = pg.AxisItem('right') # prepare axis 2...
ax_2.setLabel('logarithmic axis 2', color='#3e3')
ax_2.setLogMode(True)
ax_2.linkToView(vb_2) # ...assign it to viewbox 2...
pi_1.layout.addItem(ax_2, 2, 3) # ...and add it to the right of the original axis

ax_3 = pg.AxisItem('right') # prepare axis 3...
ax_3.setLabel('logarithmic axis 3', color='#33e')
ax_3.setLogMode(True)
ax_3.linkToView(vb_3) # ...assign it to viewbox 3...
pi_1.layout.addItem(ax_3, 2, 4) # ...and add it to the right of the second axis

# --- Handle view resizing ---
def updateViews():
    ## view has resized; update auxiliary views to match
    global vb_1, vb_2, vb_3
    vb_2.setGeometry(vb_1.sceneBoundingRect())
    vb_3.setGeometry(vb_1.sceneBoundingRect())
    ## update linked axes, may not be necessary anymore.
    ## (probably this should be handled in ViewBox.resizeEvent)
    # vb_2.linkedViewChanged(vb_1, vb_2.XAxis)
    # vb_3.linkedViewChanged(vb_1, vb_3.XAxis)

updateViews() # make sure all viewboxes are drawn in the same place...
vb_1.sigResized.connect(updateViews) # ... and get realigned after any resize.

#--- Add plot data ---
pdi_1 = pg.PlotDataItem([1,2,4,8,16,32], pen='#e33')
pdi_1.setLogMode(True, False) # y is linear
vb_1.addItem( pdi_1 )

pdi_2 = pg.PlotDataItem([10,20,40,80,40,20], pen='#3e3')
pdi_2.setLogMode(True, True) # y is logarithmic
vb_2.addItem( pdi_2 )
vb_2.setXLink(vb_1)  

pdi_3 = pg.PlotDataItem([3200,1600,800,400,200,100], pen='#33e')
pdi_3.setLogMode(True, True) # y is logarithmic
vb_3.addItem( pdi_3 )
vb_3.setXLink(vb_1)  

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
