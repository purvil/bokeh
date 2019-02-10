from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import figure
from numpy.random import random


N = 300
source = ColumnDataSource(data={'x':random(N), 'y':random(N)})
plot = figure()
plot.circle('x', 'y', source=source)

slider = Slider(start = 100, end = 1000, value = N, step = 10, title = 'Number of points')

# add callbacks to widget
def callback(attr, old, new):
    '''
    attr: attribute that change
    old: old value
    new: new value
    '''
    N = slider.value
    source.data = {'x':random(N), 'y':random(N)}
    # Bokeh notice the change here and will update plot automatically

slider.on_change('value', callback) # call callback when value changes

layout = column(slider, plot)

curdoc().add_root(layout)