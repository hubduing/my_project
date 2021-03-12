import re

pattern = r"a[abc]c"
string = 'abc'
match_object = re.match(pattern, string)
print(match_object)

string = "abc, acc, aac"
all_inclussions = re.findall(pattern, string)
print(all_inclussions)

fixe_typos = re.sub(pattern, 'abc', string)
print(fixe_typos)
print()

pattern = r"a[ab]+a" # ищем жадным способом
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))
print()

pattern = r"a[ab]+?a" # ищем не жадным способом
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))