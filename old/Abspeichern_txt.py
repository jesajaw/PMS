import psutil
import time
import cpu_monitoring as cpum
import memory_monitoring as mm
import disk_monitoring as dm
import network_monitoring as nm


#Hauptüberwachungsfunktion mit eingabe(&Warnungen) in eine Datei
def monitor_system():
    #Anzahl der Überwachungszyklen
    max_interations = 5 #nur 5 Durchläufe, dann stoppen 
    current_interation = 0 

    with open("monitoring_results.txt", "a") as file:
      while current_interation < max_interations:
        file.write("_" * 40+"\n")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n" ) #aktuelle Zeit wird hinzugefügt

        #Überwache CPU und speichere evtl.Warnung 
        cpu_data, cpu_warning = cpum.monitor_cpu()
        file.write(cpu_data)

        #CPU-Warnung in die Datei schreiben, falls vorhanden
        if cpu_warning:
            file.write(cpu_warning + "\n")
        
        #überwache RAM und speichere evtl.Warnung
        memory_data, memory_warning = mm.monitor_memory()
        file.write(memory_data)

        #RAM-Warnung in die Datei schreiben, falls vorhanden
        if memory_warning:
            file.write(memory_warning + "\n")
           
        
        #überwache Festplatte und speicher evtl.Warnung
        disk_data, disk_warning = dm.monitor_disk()
        file.write(disk_data)

        #DISK Warnung in die Datei schreiben, falls vorhanden
        if disk_warning:
            file.write(disk_warning + "\n")

        #Überwachung des Netzwerks
        file.write(nm.monitor_network())
        file.write("_" * 40 + "\n\n")

        #iterationszähler erhöhen
        current_interation +=1

        #Wartezeit von 15 Sekunden
        time.sleep(15)