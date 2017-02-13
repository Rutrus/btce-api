#!/usr/bin/python3
import btceapi

mainPage = btceapi.scrapeMainPage()
for message in mainPage.messages:
    msgId, user, time, text = message
    print("%s %s: %s" % (time, user, text))

<<<<<<< HEAD
<<<<<<< HEAD
print

print "dev online: %s" % ('yes' if mainPage.devOnline else 'no')
print "support online: %s" % ('yes' if mainPage.supportOnline else 'no')
print "admin online: %s" % ('yes' if mainPage.adminOnline else 'no')
=======
=======
>>>>>>> 5e0f0f15ad5a57ec0b7cd6dd3e7e9cbfe68c1f31
print()
if mainPage.reserves24change is not None:
    print ("24change reserves: %d USD" % mainPage.reserves24change)
else:
    print ("24change reserves: ?? USD")

if mainPage.reservesALFAcashier is not None:
    print ("ALFAcashier reserves: %d USD" % mainPage.reservesALFAcashier)
else:
    print ("ALFAcashier reserves: ?? USD")

print ("%d users online" % mainPage.usersOnline)
print ("%d bots online" % mainPage.botsOnline)
print ("dev online: %s" % ('yes' if mainPage.devOnline else 'no'))
print ("support online: %s" % ('yes' if mainPage.supportOnline else 'no'))
print ("admin online: %s" % ('yes' if mainPage.adminOnline else 'no'))
<<<<<<< HEAD
>>>>>>> 5e0f0f15ad5a57ec0b7cd6dd3e7e9cbfe68c1f31
=======
>>>>>>> 5e0f0f15ad5a57ec0b7cd6dd3e7e9cbfe68c1f31
