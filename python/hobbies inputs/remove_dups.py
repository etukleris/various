def remove_duplicates(dups):
  ndups=[]
  for i in range(len(dups)):
    if dups[i] not in ndups:
      ndups.append(dups[i])
  print (ndups)
  print (dups)
  return ndups
