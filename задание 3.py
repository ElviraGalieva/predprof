file = open('vacancy.csv', encoding = "UTF-8")
st = []
for i in file:
    st.append(i.split(','))

while True:
    flag = False
    zapros = input('Введите запрос -')
    if zapros == 'None':
        break
    else:
        for i in range(len(st)):
            if st[i][4] == zapros:
                buf = st[i][1].split()
                print('В', st[i][4], 'найдена вакансия:', st[1][0] + '.', 'З/п составит:', st[i][0][:-1])
                flag = True
        if not(flag):
            print('К сожалению, ничего не удалось найти.')

File.close()
