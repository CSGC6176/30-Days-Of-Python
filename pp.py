hello_list=list()
hello_list.append("Hello")
hello_list.append("This")
hello_list.append("Is")
hello_list.append("A")
hello_list.append("List")
print(hello_list)

hello_list[4]+="!"
print(hello_list)


hello_tuple=(21,34)
print(hello_tuple)

hello_dict={"first_name":"John","last_name":"Doe","eye_color":"Blue"}
print(hello_dict["first_name"] + " " + hello_dict["last_name"] + " has " + hello_dict["eye_color"] + " eyes ")

print("{0} {1} has {2} eyes.".format(hello_dict["first_name"],hello_dict["last_name"],hello_dict["eye_color"]))

#conditions
from cgi import test
import sys
int_condition=5
if(int_condition<6):
    sys.exit("int_condition must be >=6")
else:
    print("int condition was > = 6 - continuing")


def modify_string(original_string):
    original_string+="that has been modified"
    return original_string

test_string="This is a test string"
modify_string(test_string)
print(test_string)
     
test_string=modify_string
return(test_string)
print(test_string)