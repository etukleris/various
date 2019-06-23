def median(lst):
  if len(lst) > 1: 
    nlst = sorted(lst)
    print (lst)
    print (nlst)
    if len(nlst)%2 != 0:
      return nlst[(len(nlst)-1)/2]
    else:
      return float(nlst[len(nlst)/2] + nlst[(len(nlst)/2) -1])/2
     # return 4.5
  else:
    return lst[0]
