from resource.inventory import person, skill, stringable
from resource.requirement import position
from resource.workdetail import work
from resource.teamdetail import team

print('Start..')

s1 = skill(name = '.Net', category = 'Tech', proficiencyLevel = 2)
s2 = skill(name = 'Java', category = 'Tech', proficiencyLevel = 2)


matchPct = s1.compare(s2)
print('Match Score: ' + str(matchPct))


print('End')

#print('Person...........')
#P1 = person()
#print(p1.toString())
#print('End Person...........')

#print('Position...........')
#p2 = position()
#print(p2.toString())
#print('End Position...........')

#print('Work.................')
#w1:stringable = work()
#print(w1.toString())
#print ('End Work.......................')

#print('Team..........')
#t1 = team()
#print(t1.toString())
#print('End Team............')

#print('Skill Compare.............')
#s1 = skill()
#s2 = skill()
#s1.compare(s2)
#print('Skill Compare End.........')