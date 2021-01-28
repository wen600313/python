#! python3
# phoneAndEmail.py 查找电话号码和E-mail地址

import re,pyperclip

phoneRegex = re.compile(r"""(
	(\d{3}|\(\d{3}\))?   #区号3位或4位数字，带括号或不带括号（匹配零次或一次）
	(\s|-|\.)?  #匹配空格或-或.（匹配零次或一次）
	(\d{3})  #匹配电话号码前三位
	(\s|-|\.)  #匹配电话号码分割字符
	(\d{4})  #最后四位电话号码
	(\s*(ext|x|ext\.)\s*(\d{2,5}))?  #分机号，任意数量的空格，ext或x或ext.，在接着是2到5位数字的分机号。
	)""",re.VERBOSE)
	
# 匹配电话号码的正则表达式

emailRegex = re.compile(r"""(
	[a-zA-Z0-9._%+-]+   #用户名
	@       #@
	[a-zA-Z0-9.-]+   #域名地址
	(\.[a-zA-Z]{2,4})  #.cn或.com等顶级域名
	)""",re.VERBOSE)

# 匹配邮件地址

text = str(pyperclip.paste())
matches = []

for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))

else:
	print('No phone numbers or E-mail addresses found.')
