class Member:
    def __init__(self, full_name):
        self.full_name = full_name

    def intro(self):
        print(f'Hi, my name is {self.full_name}!')

new_member = Member('Jimmy John')

# print(new_member.full_name)
# new_member.intro()

class Student(Member): 
    def __init__(self, full_name):
        super().__init__(full_name)
    
    def reason(self, answer):
        print(f'I want to attend Codebar because {answer}')

benjamin = Student('Benjamin Closson')
print(benjamin.full_name)
benjamin.reason('I want to be a great programmer!')

amy = Student('Amy Lillard')
amy.reason('Programming is cool!')

dax = Student('Daxson Dee')
dax.reason('I want to build video games!')

class Instructor(Member):
    def __init__(self, full_name):
        super().__init__(full_name)

        self.skills = []

    def bio(self, background):
        print(f'My experience is {background}')
    
    def add_skill(self, skill):
        return self.skills.append({skill})
    

tim = Instructor('Timmothy Closson')
tim.bio('25 years of front end development')
tim.add_skill('python, javascript, c++')
print(tim.skills)

mark = Instructor('Mark Closson')
mark.bio('I am an industrial engineer, and now am a solutions architect')
mark.add_skill('system design, system implementation, project management')

liz = Instructor('Elizabeth Closson')
liz.bio('I am a psycologist with specialization in though process and rational understanding')
liz.add_skill('thought process, logical thinking, soft skill training')

class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, member):
        if member == Instructor:
            return self.instructors.append(member)
        else: 
            return self.students.append(member)
    def print_details(self):
        print()

workshop = Workshop('12/03/2014', 'Java')

print(workshop.date)

workshop.add_participant(liz)
workshop.add_participant(mark)
workshop.add_participant(tim)
workshop.add_participant(benjamin)
workshop.add_participant(dax)
workshop.add_participant(amy)