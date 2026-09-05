user_name = 'mahan'
c_password = 'masih1389'
for i in range(3):
    user = input('plz enter your user name : ')
    password = input('plz enter your password : ')
    if user_name==user and c_password==password:
        print('Login successful')
        break
    else:
        print('Wrong username or password')
        print('Atempts remaining : ',2-i)