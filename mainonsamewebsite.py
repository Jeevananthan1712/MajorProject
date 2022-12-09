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
    countrev = 0
    for tag in tags:
        sentence = tag.text
        num = tag.text.split()[1].split(" ")[-1]
        conditions =  tag.text.split()[0]
        print(sentence)
        print(num)
        print(conditions)
        # print(f'{ta} last_number {t}')
        if(conditions == 'Paid' or  conditions == 'Sent'):
            countpaid = countpaid + 1
        else:
            countrev = countrev + 1
        print(countpaid)
        print(f'{countrev} r')