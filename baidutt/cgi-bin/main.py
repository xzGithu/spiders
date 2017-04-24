import cgi,cgitb
from tt import *


# print 'Content-type:text/html \n\n'
# print img("../views/1.png")
# # form1 = cgi.FieldStorage()
# # name = form1.getvalue("name")
#
# # print 'Content-type:text/html \n\n'
# # print 'hello web development \n\n'
# # print '\n\n'
# # print 'hello '+name
#

form1 = cgi.FieldStorage()
num1 = form1.getvalue("Num1")
num2 = form1.getvalue("Num2")
num3 = None
if not num1 is None and not num2 is None:

    num1 = int(num1)
    num2 = int(num2)

    num3 = num1+num2

print start_response()
print start_div("center","margin-top:40px")
print img("../views/1.png")
print end_div()


print start_div("center","margin-top:60px")
print start_form()
print input_label("Num1","adder-1")
print '+'
print input_label("Num2","adder-2")
print '='
if num3 is None:

    print input_label("Num3","Result","","readonly")
else:
    print input_label("Num3","Result",str(num3),"readonly")
print end_form()
print end_div()