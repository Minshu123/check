import smtplib
sender_email="minshudwarika@gmail.com"
rec_email="minshunitrkl@gmail.com"
password="Minshu@123"
message="Hey ,Your website has been deployed and site is working fine."
server=smtplib.SMTP("smtp.gmail.com",587) 
server.starttls()
server.login(sender_email,password)
print("Login success")
server.sendmail(sender_email,rec_email,message)
print("Email  has been sent")
