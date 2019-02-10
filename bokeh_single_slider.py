from bokeh.io import curdoc
from  bokeh.layouts import widgetbox
from bokeh.models import Slider

# create slider
slider = Slider(title = 'my slider', start = 0, end = 10, step = 0.1, value=2)

# create widgetbox layout

layout = widgetbox(slider)

curdoc().add_root(layout)