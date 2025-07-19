s = [ '1', '2', 'a', '3']
lst = [ int(i) for i in s if i.isdigit()]
print(lst)

# str.isdigit() = 숫자인것만 TRUE!