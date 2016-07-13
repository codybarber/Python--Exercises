name = 'Cody Barber'
age = 31
height = 74 # inches
weight = 295 # pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's very heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
