import smtplib as s
ob = s.SMTP("smtp.gmail.com",  587)

ob.starttls()

ob.login("sg131019@gmail.com", "")

subject="hello all"
body="my name is swati"

message = "Subject:{}\n\n{}".format(subject, body)
# print(message)
listOfAddress = ["sg131019@gmail.com"]

ob.sendmail("sg131019@gmail.com", listOfAddress, message)
print("send successfully.....")
ob.quit()
