import webbrowser, sys, pyperclip

directions = False

if len(sys.argv) > 1:
    # Get address from command line.
	address = ""
	for arg in sys.argv[1:]:
		if arg.endswith(";"):
			if not directions:
				directions = True
			arg = arg[:-1]
			address += arg + ' ' + "/"
		else:
			address += arg + ' '
else:
    # Get address from clipboard.
    address = pyperclip.paste()

if directions:
	webbrowser.open('https://www.google.com/maps/dir/' + address)
else:
	webbrowser.open('https://www.google.com/maps/place/' + address)