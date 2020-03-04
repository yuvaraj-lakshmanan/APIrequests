
import requests 
import urllib3
from requests.auth import HTTPDigestAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# list_of_cameras = open (r"D:\\test.txt","w+")
list_of_cameras = open("D:\\test.txt",'r')
print(list_of_cameras.read())

for i in list_of_cameras:
	i = str(i)
	ip_addr = i.strip()
	print (ip_addr)

# u_name = str(input("Enter the Username:"))
# p_pass = str(input("Enter the Password:"))

json_data = requests.get('http://'+ip_addr+'/axis-cgi/admin/param.cgi?action=update&group=Image.I0.Overlay.Enabled&Image.I0.Overlay.Enabled=no', auth=HTTPDigestAuth('root','pass'), verify =False)
# # # json_data = requests.get('                    ', verify = False)
# print (json_data.status_code)
# print (json_data.content)
if json_data.status_code == 200:
	print(json_data.status_code,'Success!')
else:
	if json_data.status_code == 401:
		print(json_data.status_code,'Enter valid username and password please! and check the authentication scheme')
	elif json_data.status_code == 404:
		print (json_data.status_code , "URL NOT found")




import time
 
# Wait for 5 seconds
time.sleep(20)
# curl -X GET --header "Accept: application/json" -u 'root':'pass'  'http://10.132.18.253/axis-cgi/admin/paramlist.cgi'

# auto-py-to-exe