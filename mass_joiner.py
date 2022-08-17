try:
	import os
	import requests
	from plyer import notification
except:
	exit("[!] ERROR Install 'plyer' and 'requests'")

def read_tokens(filedir):
	f=open(filedir,'r')
	lines=f.readlines()
	f.close()

	return lines

def join_server(token,server_url):
	response = requests.post("https://discord.com/api/v9/invites/" + server_url, headers={"Authorization" : token})
	return response.text if response.status_code == 200 else False

def joiner():
	server = input(f"[?] Server Url: ")

	if '/' in server:
		s = server.split('/')
		server = s[len(s)-1]

	print('[+] Reading Tokens File')

	tokens = []

	while len(tokens) == 0:
		try:
			tokens = read_tokens(os.getcwd() + '\\' + "tokens.txt")
		except FileNotFoundError:
			open(os.getcwd() + '\\' + "tokens.txt","w+")
		input("[!] No Tokens Found\n[>] Put tokens into 'tokens.txt'")

	working_joins = []

	print(f'[+] Joining {len(tokens)} Tokens to {server}')

	for tkn in tokens:
		tkn = tkn.strip('\n')

		if tkn in working_joins: continue

		worked = join_server(tkn,server)

		if not worked:
			print(f"[-] {tkn}")
			continue

		print(f"[+] {tkn}")
		working_joins.append(tkn)

	print('[+] Finished with {} valid joins'.format(len(working_joins)))

if __name__ == "__main__":
	joiner()

	if settings.notify: notification.notify(title="Discord Mass Joiner", message="Finished joining servers!", app_icon=None, timeout=5)
	input('[?] Press ENTER to close script')