def conversion(l):
    return l * 0.21997
    
def mpg(m_travelled, gal_used):
    return m_travelled / gal_used

print "Please enter the amount of litres you have put in your tank: "
litres = raw_input('>>  ')

gallons = conversion(int(litres))

print "Please enter how many miles you travelled."
miles = raw_input('>>  ')

journey_mpg = mpg(int(miles), gallons)

print "\nToday you covered: %r miles to the gallon" % round(journey_mpg, 2)

print "Thats some pretty good mileage!"
