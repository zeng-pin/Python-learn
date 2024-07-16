import re
seach_rule='\d+\.\d+'
s=['hello 7.16 wrold','55.26lsllff']
for i in range(len(s)):
    match=re.search(seach_rule,s[i],re.I)
    print(match,match.span(),match.group(),sep='\n',end='\n\n')
