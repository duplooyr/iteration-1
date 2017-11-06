# pip install plotly
import plotly
import plotly.graph_objs as go


animals = ['giraffes', 'orangutangs', 'monkeys']
animal_counts = [20, 14, 24]

data = [go.Bar(
    x = animals,
    y = animal_counts
)]
plotly.offline.plot(data, filename='basic-bar')