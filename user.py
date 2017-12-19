#!/usr/bin/python

import cgi

print "content-type:text/html"
print ""

webdata=cgi.FieldStorage()

username=webdata.getvalue('u')
password=webdata.getvalue('p')

if username == 'root' and password == 'redhat' :
	print "<meta http-equiv='refresh' content='0;http://127.0.0.1/service.html'>"

else :
	print "OPPS Authentication failure"
	print "<a href='http://127.0.0.1/index.html'>"
	print "<img src='http://127.0.0.1/try'>"
	print "</a>"
