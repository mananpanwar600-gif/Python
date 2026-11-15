#  Write a python function which converts inches to cms.

def inches_to_cms(inch):
    cm = inch * 2.54
    return cm

inches = int(input("Enter length in inches : "))
print(f"{inches} inch/inches is {inches_to_cms(inches)} cm/cms")