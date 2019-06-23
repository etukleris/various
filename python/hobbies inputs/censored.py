def censor(text,word):
  end_text=""
  st = 0
  while st < len(text):
      if text[st:st+len(word)] == word:
          end_text += "*" * len(word)
          st+=len(word)
      else:
          end_text += text[st]
          st += 1
  return end_text

print (censor("hey hey hey hey hey hey","hey"))
