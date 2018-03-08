import hashlib
from operator import itemgetter

class Call(object):
    def __init__(self, name, phone, time_of_call, reason):
        self.id = hashlib.sha256(name+str(phone)+str(time_of_call)+reason).hexdigest()[-8:]
        self.name = name
        self.phone = phone
        self.time_of_call = time_of_call
        self.reason = reason
    def display_call(self):
        print "Call Id: " + str(self.id)
        print "Caller Name: " + self.name
        print "From Phone #: " + str(self.phone)
        print "Time of Call: " + str(self.time_of_call) + " hours"
        print "Reason for call: " + self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def add(self, call):
        self.calls.append(call)
        self.queue += 1
        return self
    def remove(self):
        self.calls.pop()
        self.queue -=1
        return self
    def info(self):
        for i in range(len(self.calls)):
            print self.calls[i].id
            print self.calls[i].name
            print self.calls[i].phone
            print self.calls[i].time_of_call
            print self.calls[i].reason
        print self.queue
        return self
    def phone_remove(self,look):
        for i in range(len(self.calls)-1):
            if(self.calls[i].phone == look):
                self.calls.pop(i)
                self.queue -= 1
        return self
    def sort_queue(self):
        self.calls = sorted(self.calls, key=lambda x: x.time_of_call)


Omaha = CallCenter()
Omaha.add(Call("Bob Marley", 5556667777, 1345, "To check on EXTRA-LARGE Underwear order"))
Omaha.add(Call("Bart", 2345678901, 1659, "Cowa Bunga!"))
Omaha.add(Call("Ed", 4445556666, 1350, "Coordinate a return"))
Omaha.add(Call("Tom", 1112223333, 1500, "Nuts"))
Omaha.add(Call("Homer", 1234567890, 1601, "Doh!"))

Omaha.phone_remove(1112223333)
Omaha.sort_queue()

Omaha.info()


