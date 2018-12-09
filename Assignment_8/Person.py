class Person:
    def __init__(self, name, address, phone_number, dob, nationality):
        self.name, self.address, self.phone_number, self.dob, self.nationality = name, address, phone_number, dob, nationality

    def __str__(self):
        print self.name, self.address, self.phone_number, self.dob, self.nationality

class Worker(Person):
    def __init__(self, name, address, phone_number, dob, nationality, company, company_address, job_phone_number):
        Person.__init__(self, name, address, phone_number, dob, nationality)
        self.company, self.company_address, self.job_phone_number = company, company_address, job_phone_number

    def __str__(self):
        Person.__str__(self)
        print self.company, self.company_address, self.job_phone_number

class Scientist(Worker):
    def __init__(self, name, address, phone_number, dob, nationality, company, company_address, job_phone_number, scientific_discipline, type):
        Worker.__init__(self, name, address, phone_number, dob, nationality, company, company_address, job_phone_number)
        self.scientific_discipline = scientific_discipline
        self.type = type

    def __str__(self):
        Worker.__str__(self)
        print self.scientific_discipline, self.type

class Postdoc(Scientist):
    def __init__(self, name, address, phone_number, dob, nationality, company, company_address, job_phone_number, scientific_discipline, type, position):
        Scientist.__init__(self, name, address, phone_number, dob, nationality, company, company_address, job_phone_number, scientific_discipline, type)
        self.position = position

    def __str__(self):
        Scientist.__str__(self)
        print self.position


class Professor(Scientist):
    def __init__(self, name, address, phone_number, dob, nationality, company, company_address, job_phone_number,
                 scientific_discipline, type, position):
        Scientist.__init__(self, name, address, phone_number, dob, nationality, company, company_address,
                           job_phone_number, scientific_discipline, type)
        self.position = position

    def __str__(self):
        Scientist.__str__(self)
        print
        self.position

class Researcher(Scientist):
    pass

person = Person('Zack', 'test address','555-555-5555', '01/01/2018', 'China')
person.__str__()
print ''

worker = Worker('Zack', 'test address','555-555-5555', '01/01/2018', 'China', 'Google', '1 Google street', '666-666-6666')
worker.__str__()
print ''

scientist = Scientist('Zack', 'test address','555-555-5555', '01/01/2018', 'China', 'Google', '1 Google street', '666-666-6666', 'computer science', ['theoretical', 'experimental'])
scientist.__str__()
print ''

postdoc = Postdoc('Zack', 'test address','555-555-5555', '01/01/2018', 'China', 'Google', '1 Google street', '666-666-6666', 'computer science', ['theoretical', 'experimental'], 'postdoc')
postdoc.__str__()
print ''

professor = Professor('Zack', 'test address','555-555-5555', '01/01/2018', 'China', 'Google', '1 Google street', '666-666-6666', 'computer science', ['theoretical', 'experimental'], 'professor')
professor.__str__()
print ''

researcher = Researcher('Zack', 'test address','555-555-5555', '01/01/2018', 'China', 'Google', '1 Google street', '666-666-6666', 'computer science', 'experimental')
researcher.__str__()