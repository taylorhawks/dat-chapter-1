def thirtythree(numbers):
	def divisiblebythirtythree(x):
		if x %33 == 0:
			print(x)
	print( [ divisiblebythirtythree(y) for y in numbers ] )
