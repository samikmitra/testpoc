from ast import List
from .workdetail import work
from .inventory import stringable
from .requirement import position

## Class to hold team : work and position
## There will be a way to predict the effectiveness of the team
class team(stringable):
    name = 'none'; workload = work(); positions =[]; effectivenessRating = 0

    ## Construction
    def __init__(self, name = 'none', workload = work(), positions = [position()]) -> None:
        super().__init__()
        self.workload = workload; self.positions = positions

    ## Override base class function
    def toString(self) -> str:
        msg = ' Team Name: ' + self.name
        msg += '\n  Work: ' + self.workload.toString()
        for pos in self.positions:
            msg += '\n Position: ' + pos.toString()
        return msg

    ## Function to calculate efectiveness between 1 and 10
    def calculateEffectiveness(self) -> int:
        self.effectivenessRating = 0
        return 1
