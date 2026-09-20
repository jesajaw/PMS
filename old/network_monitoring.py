import psutil

#Funktion zum Überwachen des Netzwerks 
def monitor_network():
    net_io = psutil.net_io_counters()
    net_info = []
    net_info.append("Netzwerkdaten:")
    net_info.append(f" Gesendete Daten: {net_io.bytes_sent / (1024**2):.2f} MB")
    net_info.append(f" Empfange Daten: {net_io.bytes_recv / (1024**2):.2f} MF\n")
    return "\n".join(net_info)