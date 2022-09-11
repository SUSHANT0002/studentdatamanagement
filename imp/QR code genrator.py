#########                                            QR code
# import qrcode
# img=qrcode.make("https://www.instagram.com/")
# img.save('IGQR.jp')
###########################                          ip address
# import socket
# Host = socket.gethostname()
# local_ip = socket.gethostbyname(Host)
# print(local_ip)
##############################                        pie chart
import matplotlib.pyplot as pc
shares = [32,41,11,8,8]
lables = ['python','perl','swift','c','c++']
pc.pie(shares,labels=lables)
pc.show()     