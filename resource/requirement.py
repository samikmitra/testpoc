from datetime import date
from .inventory import stringable, person, skill

## Class to hold a position
## Can be open or closed
## Can have a future open date
## Required experience
## Mapped to a resource
class position(stringable):
    name = 'none'
    status = 'open'
    openDate = date.today()
    experience = 0
    requiredSkills = [skill()]
    allocatedPerson = person()

    ## Constructor
    def __init__(self, name = 'none', status = 'open', openDate = date.today(), \
        experience = 0, allocatedPerson = person(), skills = [skill()] ) -> None:
        super().__init__()
        self.name = name; self.status = status; self.openDate = openDate
        self.experience = experience; self.allocatedPerson = allocatedPerson
        self.requiredSkills = skills

    ## Override base class functions
    def toString(self) -> str:
        msg = 'Position Name: ' + self.name + ' Status: ' + self.status + ' Open From Date: ' + \
            self.openDate.strftime("%d/%m/%Y") + ' Allocated Person: ' + \
                self.allocatedPerson.toString() + ' '
        
        for oneSkill in self.requiredSkills:
            msg += ' Required ' + oneSkill.toString()
        return msg