with open("/Users/bmosley/Desktop/storefront.txt", "r") as f:
	aaa = f.readlines()

for a in aaa:
	b = a.split("\t")
	bb = a.split("\t")

	b_parts = b[0].split()
	if len(b_parts) > 1:
		firstCase = b_parts[0].lower() + ''.join(i.capitalize() for i in b_parts[1:])

	else:
		firstCase = b[0].lower()

	print(f"""case {firstCase.strip()} = "{bb[1]}" """.strip())