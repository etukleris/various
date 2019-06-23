x = [{'key': 'badges', 'value': None}, {'key': 'color', 'value': '#79008F'}, {'key': 'display-name', 'value': 'talkman_'}, {'key': 'emotes', 'value': None}, {'key': 'flags', 'value': None}, {'key': 'id', 'value': '22695ae0-ea5b-4cc6-b030-a8cbd8788d6c'}, {'key': 'mod', 'value': '0'}, {'key': 'room-id', 'value': '270315289'}, {'key': 'subscriber', 'value': '0'}, {'key': 'tmi-sent-ts', 'value': '1540816743867'}, {'key': 'turbo', 'value': '0'}, {'key': 'user-id', 'value': '42552035'}, {'key': 'user-type', 'value': None}]

for dic in x:
	if dic['key'] == 'display-name':
		print (dic['value'])
 
#same outcome as 
print(x[2]['value'])