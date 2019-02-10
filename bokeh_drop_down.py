from bokeh.io import curdoc
from bokeh.models import Select, ColumnDataSource
from bokeh.layouts import column
from numpy.random import random, normal, lognormal
from bokeh.plotting import figure

N = 1000

source = ColumnDataSource(data={'x':random(N),'y':random(N)})

plot = figure()
plot.circle('x', 'y', source=source)

menu = Select(options=['uniform', 'normal', 'lognormal'],  value = 'uniform', title='Distribution')

layout = column(menu,plot)

def callback(attr, old, new):
    f = lognormal
    if menu.value == 'uniform': 
        f = random
    elif menu.value == 'normal':
        f = normal
    else:
        f = lognormal
    
    source.data = {'x':f(size= N), 'y':f(size=N)}
menu.on_change('value', callback)

layout = column(menu, plot)

curdoc().add_root(layout)