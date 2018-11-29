#!/usr/bin/env python

import praw,random,time,requests,wifi,os,smtplib
from email.mime.text import MIMEText
from ctypes import *
from sys import exit

words2check=[]
comments1=[]
comments2=[]
cache=[]
usernames=[]

                                                                
def LinuxWlanConnector(SEEKED_SSID,SEEKED_PASSPHRASE):
	if __name__ == "__main__":
    	bus = dbus.SystemBus()
	    manager_bus_object = bus.get_object("org.freedesktop.NetworkManager","/org/freedesktop/NetworkManager")
 	    manager = dbus.Interface(manager_bus_object,"org.freedesktop.NetworkManager")
 	    manager_props = dbus.Interface(manager_bus_object,"org.freedesktop.DBus.Properties")
 	    was_wifi_enabled = manager_props.Get("org.freedesktop.NetworkManager","WirelessEnabled")
	    if not was_wifi_enabled:
	    	print("[-]Wifi not enabled")
 	   	    manager_props.Set("org.freedesktop.NetworkManager", "WirelessEnabled",True)
 	        time.sleep(10)
 	   device_path = manager.GetDeviceByIpIface("wlan0")
 	   device = dbus.Interface(bus.get_object("org.freedesktop.NetworkManager",device_path),"org.freedesktop.NetworkManager.Device.Wireless")
   	   accesspoints_paths_list = device.GetAccessPoints()
 	   our_ap_path = None
 	   for  ap_path in accesspoints_paths_list:
    	    ap_props = dbus.Interface(bus.get_object("org.freedesktop.NetworkManager", ap_path),"org.freedesktop.DBus.Properties")
        	ap_ssid = ap_props.Get("org.freedesktop.NetworkManager.AccessPoint","Ssid")
        	str_ap_ssid = "".join(chr(i) for i in ap_ssid)
        	if str_ap_ssid == SEEKED_SSID:
        	    our_ap_path = ap_path
            	break
        	exit(2)
	    connection_params = {
    	    "802-11-wireless": {
        	    "security": "802-11-wireless-security",
    	    },
    	    "802-11-wireless-security": {
        	    "key-mgmt": "wpa-psk",
        	    "psk": SEEKED_PASSPHRASE
        	},
    	}
	    settings_path, connection_path = manager.AddAndActivateConnection(connection_params, device_path, our_ap_path)
	    print("[-]Connected to Wifi")
	    NM_ACTIVE_CONNECTION_STATE_ACTIVATED = 2
	    connection_props = dbus.Interface(bus.get_object("org.freedesktop.NetworkManager", connection_path),"org.freedesktop.DBus.Properties")
	    state = 0
	    while True:
	        state = connection_props.Get("org.freedesktop.NetworkManager.Connection.Active", "State")
	        if state == NM_ACTIVE_CONNECTION_STATE_ACTIVATED:
	            break
	        time.sleep(0.001)
	    time.sleep(5)

def Cache(cache):
	with open('cache.txt','a+') as f :
		for line in f:
			if line not in cache:
				cache.append(line.strip())
		f.close()

def Usernames(usernames):
	with open('usernames.txt','a+') as e :
		for line in e:
			if line not in usernames:
				usernames.append(line.strip())
		e.close()

def RAOCbot(USERNAME,PASSWORD):
	r=praw.Reddit(user_agent="Mozilla/5.0 (X11; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0")
	r.login(USERNAME,PASSWORD,disable_warning=True)
	time.sleep(10)
	results=r.search('flair:offer',subreddit='RandomActsofCards', sort='new', syntax=None, period='hour')
	print("[-]searching for offers")
	randomcomment=random.randint(0,len(comments)-1)
	for result in results:
		if result.id not in cache :
			username = result.author
 			if username not in usernames:
 				print("[-]New sender !")
				result.add_comment(comments1[randomcomment])
				print("[-]commenting a random comment")
				f = open('cache.txt','a+')
				for line in f :
					if len(line) == 0 :
						f.write(result.id)
						f.close()
				for line in e :
					if len(line) == 0 :
						e.write(username.id)
						e.close()
				Cache(cache)
				cache.append(result.id)
				Usernames(usernames)
				usernames.append(username.id)
				msg = 'Hello' 
				r.user.send_message(username, msg)
			else:
				print("[-]known sender .")
				result.add_comment(comments1[randomcomment])
				print("[-]commenting a random comment")
				f = open('cache.txt','a+')
				for line in f :
					if len(line) == 0 :
						f.write(result.id)
						f.close()
				Cache(cache)
				cache.append(result.id)
				msg = 'Hello' 
				r.user.send_message(username, msg)
	while True :
		print("[-]sleeping for 15 minutes")
		time.sleep(900)
		RAOCbot

get_comment_replies(*args, **kwargs)  
print(author.name)  # The username


def gmailsender(USERNAME,PASSWORD,MAILTO):
	msg = MIMEText('This is the body of the email')
	msg['Subject'] = 'The email subject'
	msg['From'] = USERNAME
	msg['To'] = MAILTO

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo_or_helo_if_needed()
	server.starttls()
	server.ehlo_or_helo_if_needed()
	server.login(USERNAME,PASSWORD)
	server.sendmail(USERNAME, MAILTO, msg.as_string())
	return print("email sent to ",MAILTO)

