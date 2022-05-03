password = 'a123456'
i = 0
while i < 3:
    pw = input('輸入密碼: ')
    if pw == password:
        print('登入成功')
        break
    else:
        if i == 2:
            break
        else:
            print('密碼錯誤！還有', 2-i, '次機會')
            i = i + 1
        