import psutil
import old.cpu_monitoring as cm 
import old.memory_monitoring as mm
import old.disk_monitoring as dm 
import old.network_monitoring as nm 


import plotly.graph_objects as go 
import plotly._subplots as sp

# 1 CPU Auslastung pro Kern 
def plot_cpu_usage():
    cm.cpu_usage = psutil.cpu_percent(interval=1), percpu=True)
    fig_cpu = go.Figure([go.Bar(x=list(range(len(cm.cpu_usage)))), y=cpu_usage])
    