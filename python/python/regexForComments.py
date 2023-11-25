import re

s = """

"LOADING" = "LOADING";
"OK" = "OK";
"MORE" = "MORE";
"YES" = "Yes";
"NO" = "No";
"BACK" = "Back";
"EXIT" = "Exit";

"""

string = " ll/*asdasd*/$hahahaha$hahahaha hello"


co = re.findall(r"(\/\*)\s*(.*?)\s*(\*\/)", s, re.DOTALL)
# ss = re.sub(r"(\/\*)\s*(.*?)\s*(\*/)", "", s)

# print(co)

cm = re.compile(r"(\/\*)\s*(.*?)\s*(\*\/)", re.DOTALL)
m = re.sub(cm, "", s)
print(m)
