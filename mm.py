password = 'a123456'
x = 3
while True:
	password1 = input('请输入密码：')
	if password == password1:
		print('系统登入成功！')
		break
	else:
		x = x - 1
		print('密码错误，还有',x,'次机会')
		if x == 0:
			print('登入失败')
			break