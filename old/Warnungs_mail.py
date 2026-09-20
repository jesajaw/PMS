import smtplib
from email.mime.text import MIMEText

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