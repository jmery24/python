#!usr/bin/python
list = ['hammer', 'lantern', 'screwdriver', 'drill']
print list
for each_item in list:
    print each_item
    if each_item == "drill":
       print "Don't forget to light your lantern"
       print "once you're down there"
raw_input("Hit enter too continue")
