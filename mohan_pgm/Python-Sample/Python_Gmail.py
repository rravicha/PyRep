
import smtplib
 
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
 

s.login("mohangokulcse@gmail.com", "dhonikohli")

message = "Ji check for the output"
 
s.sendmail("mohangokulcse@gmail.com", "heyitsak@gmail.com", message)

s.quit()


#Go to this link and select Turn On
#https://www.google.com/settings/security/lesssecureapps
