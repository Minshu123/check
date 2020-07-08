
import smtplib
sender_email="minshudwarika@gmail.com"
rec_email="minshunitrkl@gmail.com"
password="resonance"
message="hey ,Something wrong with the code or  the set up .please check out.  "
server=smtplib.SMTP("smtp.gmail.com",587) 
server.starttls()
server.login(sender_email,password)
print("Login success")
server.sendmail(sender_email,rec_email,message)
