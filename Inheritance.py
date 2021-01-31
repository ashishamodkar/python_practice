#inheretance in python

class studen:
    def __init__(self,fname,lname,prn):
        self.firstname = fname
        self.lastname = lname
        self.prno = prn


    def pname(self):
        print(self.firstname, self.lastname, self.prno)
s = studen("Ashish", "Amodkar", "0441800580")
s.pname()