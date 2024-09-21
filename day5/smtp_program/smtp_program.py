#https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps

'''
To send mail 
    enable in gmail the 2 step verification 
Then 
    use below link to create app password
    with app password and your mail id try to run the below code

    #https://support.google.com/accounts/answer/185833?hl=en
'''
import smtplib as smtp
connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
 
email_addr = 'pystud19@gmail.com' #Add your email here
email_passwd = 'yaxb hoco fihc prnn' #password given by google
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='mtd.nithin@gmail.com', msg=" TYPE YOUR MAIL CONTENT HERE")
connection.close()
print('Mail sent successfully')