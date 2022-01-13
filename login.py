username=input('Enter your username :')
password=input('Enter your password :')

if username.upper()=='admin'.upper() and password=='sonjoy':
    print(f'welcome Mr {username}')
elif username.upper()!='admin'.upper() and password=='sonjoy':
    print('invalid username')
elif username.upper()=='admin'.upper() and password!='sonjoy':
    print('invalid password')
else:
    print('invalid username and password !!!')
