password = 'a123456'
i = 3
while i > 0:
	pwd = input('please enter password:')
	if pwd == password:
		print ('log in succeed')
		break
	else:
		i = i - 1
		print('invalid password, please retry, you have', i, 'attemps left' )
	
		