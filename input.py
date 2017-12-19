#!/usr/bin/python

import cgi

print "content-type:text/html"
print ""

webdata=cgi.FieldStorage()

service=webdata.getvalue('n')

if service == 'sa' :

	print "<meta http-equiv='refresh' content=0;http://127.0.0.1/saas.html>"

elif service == 'ia' :
	print "<meta http-equiv='refresh' content=0;http://127.0.0.1/iaas.html>"

else  :
	print "wrong input"
	
