from abc import ABC, abstractclassmethod
from datetime import date, timedelta

## Abstract class to provice common output method
class stringable(ABC):

    @abstractclassmethod
    def toString(self) -> str:
        pass

## Class to represent an existing skill
class skill(stringable):
    name = 'none'
    category = 'none'
    proficiencyLevel = 1
    aging = 0

    ## Constructor
    def __init__(self, name = 'none', category = 'none', proficiencyLevel = 1, aging = 0) -> None:
        self.name = name
        self.category = category
        self.proficiencyLevel = proficiencyLevel
        self.aging = aging

    ## Override base class function
    def toString(self) -> str:
        msg = 'Skill Name: ' + self.name + ' Category: ' + self.category + ' Proficiency: ' + \
                str(self.proficiencyLevel) + ' Aging: ' + str(self.aging) + ' day(s)'
        return msg

## Class to represent a resource along with skills through association
## Resource's allocation to different teams will be catered in the Team representation
## Allocation End date represent release date from account
class person(stringable):
    name = 'none'
    skills = []
    experience = 0
    allocationEndDate = date.today() + timedelta(days=365)

    ## Constructor
    def __init__(self, name = 'none', skills = [skill()], experience =0, \
        allocationEndDate = date.today() + timedelta(days=365) ) -> None:
        self.name = name
        self.skills = skills
        self.experience = experience

    ## Override base class function
    def toString(self) -> str:
        msg = 'Resource Name: ' + self.name + ' Total Experience: ' + str(self.experience) + ' yrs ' \
            + ' Allocationd Ends: ' + self.allocationEndDate.strftime("%d/%m/%Y") + ' '

        for oneSkill in self.skills:
            msg += oneSkill.toString()

        return msg


