#Terminal Commands zum Installieren von Blibliotheken die benötigt sind 
        #pip install flask matplotlib
        #pip install psutil 
        #pip install plotly


import psutil
import time

import plotly
import plotly.graph_objects as go 
import plotly._subplots as sp

import smtplib
from email.mime.text import MIMEText

#Schwellenwerte angeben 
CRITICAL_CPU_THRESHOLD = 3.0 
CRITICAL_DISK_THRESHOLD = 85.0
CRITICAL_MEMORY_THRESHOLD = 80.0

#Funktion zum Überwachen der CPU-Auslastung
def monitor_cpu():
    cpu_info = []
    cpu_usage = psutil.cpu_percent(interval=1)
   

    cpu_info.append("CPU-Auslastung:")
    cpu_info.append(f" Gesamte CPU-Auslastung: {psutil.cpu_percent(interval=1)}%")
    cpu_info.append(f" CPU-Kerne: {psutil.cpu_count(logical=True)}")
    cpu_info.append(f" CPU-Frequenz: {psutil.cpu_freq().current} MHZ\n")

    #Warnung bei zu hoher CPU Auslastung 
    if cpu_usage >=CRITICAL_CPU_THRESHOLD:
        warning_message = f"!!! WARNUNG: CPU-Auslastung hat {CRITICAL_CPU_THRESHOLD}% überschritten ({cpu_usage}%) !!!"
        cpu_info.append(warning_message)
        print(warning_message) #Gib die Warnung in der Konsole aus
        send_email_alert("CPU Warnung", warning_message) #HIER Der MAIL befehl
        return "\n".join(cpu_info), warning_message #Rückgabe der CPU-Information und der Warnung
    
    return "\n".join(cpu_info), None #keine Warunung, nur CPU Daten zurückgeben

#Funktion zum Überachen der Festplatte
def monitor_disk():
    disk = psutil.disk_usage('/')
    disk_info = []

    disk_info.append("Festplatteninformation:")
    disk_info.append(f"  Gesamter Speicherplatz: {disk.total / (1024**3):.2f} GB")
    disk_info.append(f"  Verfügbarer Speicherplatz: {disk.free / (1024**3):.2f} GB")
    disk_info.append(f"  Speicherplatz-Auslastung: {disk.percent}%\n")

    #Warnung bei wenig Restspeicher der Festplatte
    if disk.percent >=CRITICAL_DISK_THRESHOLD:
        warning_message = f"!!! WARNUNG: DISK-Speicher hat {CRITICAL_DISK_THRESHOLD}% erreicht ({disk.percent}%) !!!"
        disk_info.append(warning_message)
        print(warning_message) #Gibt die Warnung in der Konsole aus 
        return "\n".join(disk_info), warning_message # Rückgabe des Speicherstandes und der Warnung
    
    return "\n".join(disk_info), None #Keine Warnung, nur Memory Daten zurückgeben

#Funktion zum überwachen des Arbeitsspeichers
def monitor_memory():
    memory = psutil.virtual_memory()
    memory_info = []

    memory_info.append("Arbeitsspeicher:")
    memory_info.append(f" Gesamter RAM: {memory.total / (1024**3):.2f} GB")
    memory_info.append(f" Verfügbarer RAM: {memory.available / (1024**3):.2f} GB")
    memory_info.append(f" RAM-Auslastung: {memory.percent}%\n")

    #Warnung bei zu Hohem RAM verbrauch
    if memory.percent >=CRITICAL_MEMORY_THRESHOLD:
        warning_message = f"!!! WARNUNG: RAM-Auslastung hat{CRITICAL_MEMORY_THRESHOLD}% überschritten ({memory.percent}%) !!!"
        memory_info.append(warning_message)
        send_email_alert("RAM-Warnung", warning_message)
        print(warning_message) #Gibt die Warnung in der Konsole aus 
        
        return "\n".join(memory_info), warning_message #Rückgabe der RAM INFO und der Warnung 
    
    return "\n".join(memory_info), None #Keine Warnung, nur Memory Daten zurückgeben

#Funktion zum Überwachen des Netzwerks 
def monitor_network():
    net_io = psutil.net_io_counters()
    net_info = []
    net_info.append("Netzwerkdaten:")
    net_info.append(f" Gesendete Daten: {net_io.bytes_sent / (1024**2):.2f} MB")
    net_info.append(f" Empfange Daten: {net_io.bytes_recv / (1024**2):.2f} MF\n")
    return "\n".join(net_info)

#Mail angabe sender und reciver (Empfänger Liste kann auch als Liste erstellt werden)
def send_email_alert(subject, body):
    sender_mail = "marten.rosinski@gmail.com" # Absender adresse hier würde ich meine Firmen Mail nehmen
    receiver_mail = "rosinskimarten@gmail.com" # Receiver Mail ( maybe hier die Privatadressen)
    password = "NeuealteFreunde" # Hier muss das Passwort der Absender Adresse rein (maybe App specific Passwort)
    
    #MIME Struktur der Mail
    msg = MIMEText(body)
    msg['From'] = sender_mail
    msg['To'] = receiver_mail
    msg['Subject'] = subject

#Verbindung zum SMTP Server 
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #    server.starttls() #Sichere VErbindung mit TLS (Transport Layer Security)
        server.connect()
        server.ehlo()
        server.login(sender_mail, password)#Login mit Mail und Passwort
        text = msg.as_string() # Konvertiere das Email Objekt in eine Zeichenkette
        server.send_message(msg) # EMail senden
        server.close()# Verbindung zum Server trennen
        server.quit()
        print("Warnung per E-Mail versendet!")

    except Exception as e:
       print(f"Fehler beim Versenden der Mail: {e}")
       
#Hauptüberwachungsfunktion mit eingabe(&Warnungen) in eine Datei
def monitor_system():
    #Anzahl der Überwachungszyklen
    max_interations = 1 #nur 5 Durchläufe, dann stoppen 
    current_interation = 0 

    with open("monitoring_results.txt", "w") as file:
      while current_interation < max_interations:
        file.write("_" * 40+"\n")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n" ) #aktuelle Zeit wird hinzugefügt

        #Überwache CPU und speichere evtl.Warnung 
        cpu_data, cpu_warning = monitor_cpu()
        file.write(cpu_data)

        #CPU-Warnung in die Datei schreiben, falls vorhanden
        if cpu_warning:
            file.write(cpu_warning + "\n")
        
        #überwache RAM und speichere evtl.Warnung
        memory_data, memory_warning = monitor_memory()
        file.write(memory_data)

        #RAM-Warnung in die Datei schreiben, falls vorhanden
        if memory_warning:
            file.write(memory_warning + "\n")
           
        
        #überwache Festplatte und speicher evtl.Warnung
        disk_data, disk_warning = monitor_disk()
        file.write(disk_data)

        #DISK Warnung in die Datei schreiben, falls vorhanden
        if disk_warning:
            file.write(disk_warning + "\n")

        #Überwachung des Netzwerks
        file.write(monitor_network())
        file.write("_" * 40 + "\n\n")

        #iterationszähler erhöhen
        current_interation +=1

        #Wartezeit von 15 Sekunden
        time.sleep(15)
        

 # CPU-Nutzungsdiagramm
def plot_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    fig_cpu = go.Figure([go.Bar(x=list(range(len(cpu_usage))), y=cpu_usage, marker_color='green')])  # Balken in Grün
    fig_cpu.update_layout(
        title= 'CPU Usage per Core',
        xaxis_title='CPU Core',
        yaxis_title='Usage(%)',
        template='plotly_white',  # Hintergrund Weiß
        title_font=dict(color='black'),  # Schwarze Schrift für Titel
        font=dict(color='black'),  # Schwarze Schrift für Achsenbeschriftungen
        plot_bgcolor='white',  # Weißer Hintergrund für den Plot
        paper_bgcolor='#f0f0f0',  # Weißer Papierhintergrund
        xaxis=dict(showline=True, linecolor='black'),  # Schwarze Achsenlinien
        yaxis=dict(showline=True, linecolor='black')
    )
    return fig_cpu

# RAM-Nutzungsdiagramm
def plot_ram_usage():
    ram = psutil.virtual_memory()
    labels = ['Used', 'Availible']
    values = [ram.used / (1024**3), ram.available / (1024**3)]  # in GB
    fig_ram = go.Figure([go.Pie(labels=labels, values=values, hole=0.3, marker_colors=['green', 'blue'])])  # Grün & Blau
    fig_ram.update_layout(
        title='RAM Usage (GB)',
        template='plotly_white',  # Hintergrund Weiß
        title_font=dict(color='black'),  # Schwarze Schrift für Titel
        font=dict(color='black'),  # Schwarze Schrift für Beschriftungen
        plot_bgcolor='white',  # Weißer Hintergrund für den Plot
        paper_bgcolor='#f0f0f0'  # Weißer Papierhintergrund
    )
    return fig_ram

# Festplattennutzungsdiagramm
def plot_disk_usage():
    disk = psutil.disk_usage('/')
    labels = ['Used', 'Free']
    values = [disk.used / (1024**3), disk.free / (1024**3)]  # in GB
    fig_disk = go.Figure([go.Pie(labels=labels, values=values, hole=0.3, marker_colors=['green', 'blue'])])  # Grün & Blau
    fig_disk.update_layout(
        title='Disk Usage (GB)',
        template='plotly_white',  # Hintergrund Weiß
        title_font=dict(color='black'),  # Schwarze Schrift für Titel
        font=dict(color='black'),  # Schwarze Schrift für Beschriftungen
        plot_bgcolor='white',  # Weißer Hintergrund für den Plot
        paper_bgcolor='#f0f0f0'  # Weißer Papierhintergrund
    )
    return fig_disk

# Netzwerkdiagramm
def plot_network_usage():
    net_io = psutil.net_io_counters()
    labels = ['Bytes Sent', 'Bytes received']
    values = [net_io.bytes_sent / (1024**2), net_io.bytes_recv / (1024**2)]  # in MB
    fig_net = go.Figure([go.Bar(x=labels, y=values, marker_color=['green', 'blue'])])  # Balken in Grün & Blau
    fig_net.update_layout(
        title='Network Usage (MB)',
        xaxis_title='Network Activity',
        yaxis_title='Data(MB)',
        template='plotly_white',  # Hintergrund Weiß
        title_font=dict(color='black'),  # Schwarze Schrift für Titel
        font=dict(color='black'),  # Schwarze Schrift für Achsenbeschriftungen
        plot_bgcolor='white',  # Weißer Hintergrund für den Plot
        paper_bgcolor='#f0f0f0',  # Weißer Papierhintergrund
        xaxis=dict(showline=True, linecolor='black'),  # Schwarze Achsenlinien
        yaxis=dict(showline=True, linecolor='black')
    )
    return fig_net

import os

# Funktion zum Speichern der Plots in einem bestimmten Ordner
def save_plots_to_folder(fig, filename, folder='Python Monitoring System'):
    # Prüfe, ob der Ordner existiert, andernfalls erstelle ihn
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Erstelle den vollständigen Pfad (Ordner + Dateiname)
    filepath = os.path.join(folder, filename)
    
    # Speichere das Diagramm als HTML-Datei
    fig.write_html(filepath)
    #print(f"Diagramm gespeichert unter: {filepath}") (kommentiert da Terminal ausgabe)

# Funktion zum Anzeigen aller Diagramme
def show_all_plots():
    fig_cpu = plot_cpu_usage()
    fig_ram = plot_ram_usage()
    fig_disk = plot_disk_usage()
    fig_net = plot_network_usage()
    
    # Einzelne Diagramme anzeigen (rausgenommen da diese sich immer im browser geöffnet haben)
   # fig_cpu.show()
   # fig_ram.show()
   # fig_disk.show()
   # fig_net.show()
    
    # Speichere die Diagramme als HTML in dem spezifischen Ordner
    save_plots_to_folder(fig_cpu, "cpu_usage_plot.html")
    save_plots_to_folder(fig_ram, "ram_usage_plot.html")
    save_plots_to_folder(fig_disk, "disk_usage_plot.html")
    save_plots_to_folder(fig_net, "network_usage_plot.html")
    

#Start
if __name__ == "__main__":
    monitor_system() #monitor system starten
    show_all_plots() #Diagramme zeigen und abspeichern
