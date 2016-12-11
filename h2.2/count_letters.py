def count_letters(str, ch, start):
	count = 0
	for char in str[start:]:
		if char == ch:
			count += 1

	return count

print(count_letters("eeeeasfgdvxdeecbhb","e",2))