suma = 0
sumb = 0

for overall in moves: #from list(moves), adding each value
  suma = suma + overall

for average in level:
  sumb = sumb+average #from list(level), adding difficulty choices

sumb = sumb / len(level)

if winlose['CPU'] or winlose['No One']>0:
  suma = suma + sumb * (winlose['Player']/(2*winlose['CPU']+winlose['No One']))

else: suma = suma + sumb

denominator = winlose['Player']+winlose['CPU'] #rating is out of total games played multiplied by 10

print('Player Ranking Based on Skill: ',suma,' out of ',denominator*10)
