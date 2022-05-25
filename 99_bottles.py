def bottle_song(num):
	original = num
	
	for i in reversed(range(0, num+1)):
		if i == 0:
			print('No more bottles of beer on the wall, no more bottles of beer.')
			if original != 1:
				print(f'Go to the store and buy some more, {original} bottles of beer on the wall.')
			else:
				print(f'Go to the store and buy some more, {original} bottle of beer on the wall.')
		else:
			if i >= 2:
				bottle = 'bottles'
				reduced_i = i-1
				if reduced_i != 1:
					new_bottle = 'bottles'
				else:
					new_bottle = 'bottle'
			if i == 1:
				bottle = 'bottle'
				reduced_i = 'no more'
				new_bottle = 'bottles'
			print(f'{i} {bottle} of beer on the wall, {i} {bottle} of beer.')
			print(f'Take one down and pass it around, {reduced_i} {new_bottle} of beer on the wall.')

bottle_song(1)