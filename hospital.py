import hashlib

class Patient(object):
    def __init__(self, name, allergies):
        self.id = hashlib.sha256(name+allergies).hexdigest()[-8:]
        self.name = name
        self.allergies = allergies
        self.bed_num = "none"


class Hospital(object):
    def __init__(self, name):
        self.patients = []
        self.name = name
        self.capacity = 6
        self.hosp_bed = []
        for x in range(self.capacity):
            self.hosp_bed.append(100+x)

    def admit(self, patient):
        if(self.capacity < 1):
            print "Send then to County General!!!!"
        else:
            self.patients.append(patient)
            self.capacity -= 1
            for x in range(len(self.hosp_bed)):
                if(self.hosp_bed[x] > 0):
                    patient.bed_num = self.hosp_bed[x]
                    self.hosp_bed.pop(x)
                    print "Admission Successful!!"
                    print
                    break
        return self

    def discharge(self, look):
        for i in range(len(self.patients)-1):
            if(self.patients[i].name == look):
                self.capacity += 1
                self.hosp_bed.append(self.patients[i].bed_num)
                self.patients[i].bed_num = "none"
                self.patients.pop(i)
        return self
    def roster(self):
        for i in range(len(self.patients)):
            print "Patient Id: "+str(self.patients[i].id)
            print "Patient Name: "+self.patients[i].name
            print "Patient Allergies: "+self.patients[i].allergies
            print "Patient Bed Number: " + str(self.patients[i].bed_num)
            print
        print "Hospital current capacity: " + str(self.capacity)
        print "List of available beds: "+ str(self.hosp_bed)
        print
        return self

Temple = Hospital("Childrens Hospital")
Temple.admit(Patient("Edger", "penicillin"))
Temple.admit(Patient("Susie", "anything green"))
Temple.admit(Patient("Butch", "Tylenol"))
Temple.admit(Patient("Elmo", "peanuts"))
Temple.discharge("Susie")
Temple.admit(Patient("Red Ranger", "dairy"))



Temple.roster()

