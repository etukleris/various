def reverse(text):
  tmp=""
  for i in range(len(text)-1,-1,-1):
    tmp =tmp+ text[i] 
  print (tmp)
  return (tmp)

reverse("Johnsnow")
