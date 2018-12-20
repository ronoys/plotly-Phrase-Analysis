import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
init_notebook_mode(connected=True)

# Enter String to be Analyzed
analyzed_string = "A B B C C C D D D D E E E E E F F F F G G G H H I"

# Creates list of original string chars
char_list = analyzed_string.split(" ")

elements = set(char_list) # Separates into unique elements


string_plot = dict.fromkeys(elements, 0)

for i in char_list:
    string_plot[i] = string_plot[i]+1

trace = {'type': 'bar', 'x': list(elements), 'y': list(string_plot.values())}
 
plotly.offline.plot({'data': [trace]})

