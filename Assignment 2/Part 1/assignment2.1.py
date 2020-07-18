# first_half
def first_half(str):
	return str[:len(str) / 2]
	
# without_end
def without_end(str):
	return str[1:len(str) - 1]
	
# caught_speeding
def caught_speeding(speed,is_birthday):
	def bump(bool):
		if bool == 0:
			return 0
		else:
			return 5
	low_limit = 61 + bump(is_birthday)
	high_limit = 81 + bump(is_birthday)
	if speed in range(low_limit):
		return 0
	if speed in range(low_limit,high_limit):
		return 1
	else:
		return 2

# alarm_clock
def alarm_clock(day,vacation):
	if day in range(1,6) and vacation == 0:
		return "7:00"
	elif day in [0,6] and vacation == 1:
		return "off"
	else:
		return "10:00"

# near_ten
def near_ten(num):
	if num >= 0:
		if num % 10 in [0,1,2,8,9]:
			return True
		else:
			return False