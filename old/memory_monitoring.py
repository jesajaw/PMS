import psutil
import Warnungs_mail as wm
#Schwellenwert definieren
CRITICAL_MEMORY_THRESHOLD = 80.0


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
        wm.send_email_alert("RAM-Warnung", warning_message)
        print(warning_message) #Gibt die Warnung in der Konsole aus 
        
        return "\n".join(memory_info), warning_message #Rückgabe der RAM INFO und der Warnung 
    
    return "\n".join(memory_info), None #Keine Warnung, nur Memory Daten zurückgeben