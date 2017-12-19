#!/usr/bin/python

#import cgi
import commands

#print "content-type:text/html"
#print ""

'''webdata=cgi.FieldStorage()

insatnce_name=webdata.getvalue('instance')
port=webdata.getvalue('port')
os=webdata.getvalue('os')
ram=webdata.getvalue('ram')
cpu=webdata.getvalue('cpu')
disk=webdata.getvalue('disk')'''

commands.getoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhel7.2.qcow2  /var/lib/libvirt/images/r.qcow2')
commands.getoutput('sudo virt-install  --name red --ram 1024 --vcpu 1 --disk path=/var/lib/libvirt/images/r.qcow2 --import --graphics vnc')
