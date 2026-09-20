import psutil
import Warnungs_mail as wm

#Schwellenwert definieren
CRITICAL_CPU_THRESHOLD = 3.0 

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
        wm.send_email_alert("CPU Warnung", warning_message) #HIER Der MAIL befehl
        return "\n".join(cpu_info), warning_message #Rückgabe der CPU-Information und der Warnung
    
    return "\n".join(cpu_info), None #keine Warunung, nur CPU Daten zurückgeben

