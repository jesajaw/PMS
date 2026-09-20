import psutil

#Schwellenwert definieren
CRITICAL_DISK_THRESHOLD = 85.0

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