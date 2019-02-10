from bokeh.io import curdoc
from bokeh.models import Slider
from bokeh.layouts import widgetbox

slider1 = Slider(title='slider 1', start = 0, end = 10, value = 2,step=0.1)
slider2 = Slider(title='slider 2', start=10, end=100, value = 20, step=1)

layout = widgetbox(slider1,slider2)

curdoc().add_root(layout)