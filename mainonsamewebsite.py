from bs4 import BeautifulSoup

with open('myact.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('div', class_='content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1')
    # print(tags)
    # for tag in tags:
    # t = tag.find('h2')
    # print(t)
    countpaid = 0
    addingpaid = 0
    countrev = 0
    for tag in tags:
        sentence = tag.text.replace('Sent,', 'a')
        mainpart  = sentence.split("using")[0]
        num = tag.text.split(" ")[1].replace('â','₹')
        numm = num.split(".")[0]
        conditions = tag.text.split()[0]
        # print(numm)

        # print(sentence)
        print(mainpart)
        # print(num)
        # print(conditions)
        # print(f'{ta} last_number {t}')
        if(conditions == 'Paid' or  conditions == 'Sent'):
            countpaid = countpaid + 1
            # addingpaid = int(addingpaid + int( numm))
            print(numm)
            # print(addingpaid)
        else:
            countrev = countrev + 1
            print(f'{numm} received')

        # print(countpaid)
    # print(f'sent or paid someone {countpaid} times and received money from someone {countrev} times')