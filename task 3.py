import collections

lst = open('data/users.txt').read().split('\n')
ID, NAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User","username id name middlename, surname, department")

def gen_username(name, surname,usernames):
	username = name[0] + surname
	count = 1
	while username in usernames:
		username = "{0}{1}".format(username, count)
		count += 1
	usernames.add(username)
	return username

def process(field, usernames):
	field = field.split(':') 
	username = gen_username(field[NAME], field[SURNAME], usernames)
	user = User(username,field[ID],field[NAME],field[MIDDLENAME],field[SURNAME],field[DEPARTMENT])
	return user

def main():
	usernames = set()
	users = []
	for field in lst[0:len(lst)-2]:
		users.append(process(field, usernames))
	return users

def printing():
	users = main()
	namewidth = 32
	usernamewidth = 9
	print("{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
	print("{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth))
	for user in users:
		initial = ""
		if user.middlename:
			initial = " " + user.middlename[0]
		name = "{0.surname}, {0.name}{1}".format(user, initial)
		print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))

printing()