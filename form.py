#!/usr/bin/python

print "Content-Type:text/html"
print ""

import cgi

form=cgi.FieldStorage()
name=form.getvalue('fname')

print "name of the user is:-",name
