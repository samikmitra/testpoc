from abc import ABC, abstractclassmethod
from datetime import date, timedelta
from typing import Type

## Abstract class to provice common output method
class stringable(ABC):

    @abstractclassmethod
    def toString(self) -> str:
        pass

class comparable(ABC):

    @abstractclassmethod
    def compare(self, inObj) -> int:
        pass

## Class to represent an existing skill
class skill(stringable, comparable):
    name = 'none'; category = 'none'; proficiencyLevel = 1; aging = 0; weightage = 0

    ## Constructor
    def __init__(self, name = 'none', category = 'none', proficiencyLevel = 1, \
         aging = 0, weightage = 0) -> None:
        self.name = name; self.category = category; self.proficiencyLevel = proficiencyLevel
        self.aging = aging; self.weightage = weightage

    ## Override base class function
    def toString(self) -> str:
        msg = 'Skill Name: ' + self.name + ' Category: ' + self.category + ' Proficiency: ' + \
                str(self.proficiencyLevel) + ' Aging: ' + str(self.aging) + ' day(s) ' + \
                    ' Weightage: ' + str(self.weightage)
        return msg

    ## Override compare method
    ## Use position as self and resource as target
    def compare(self, inObj) -> int:
        score = 0; obj : skill = inObj
        if type(self) != type(inObj):
            return score
        else:
            if self.name == obj.name and self.category == obj.category:
                ## if the skill actually matches, check for proficiency
                if self.proficiencyLevel == obj.proficiencyLevel:
                    ## evrything matches: skill level exact match
                    score = 10
                elif (self.proficiencyLevel - obj.proficiencyLevel) == 1:
                    ## resource has little lower than expected, grooming will help
                    score = 7
                elif (self.proficiencyLevel - obj.proficiencyLevel) > 1:
                    ## resource is way lower than expected, grooming will take lot of time
                    score = 4
                elif (obj.proficiencyLevel - self.proficiencyLevel) == 1:
                    ## Resource having more skill than required, can be a good thing as 
                    ## business may go up with a little risk of resource dissatisfaction
                    score = 8
                elif (obj.proficiencyLevel - self.proficiencyLevel) > 1:
                    ## Resource having way more skill than required, going to cause 
                    ## resource dissatisfaction and more planning required
                    score = 6
                else:
                    ## Catch all, cannot be a good match
                    score = 3

            ## By defult score is set to 0, meaning no match
            return score


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


