from bs4 import BeautifulSoup

#aqui ele abre o arquivo apenas lendo o que tem nele e printa todo o conteudo
with open('home_aula.html', 'r') as html_file:
    content = html_file.read()
    print(content)

    print('')

    #printa o html de forma mais agradável
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())

    print('')

    tags = soup.find('h5')  #printa apenas a primeira tag h5 que achar
    print(tags)
    
    print('')

    #retorna uma lista com todos os h5
    course_html_tags = soup.find_all('h5')
    for course in course_html_tags:  #for each para pegar apenas os cursos dentro da lista
        print(course.text)     

    print('') 

    course_cards = soup.find_all('div', class_='card') #acha toda div que tem como classe card
    for course in course_cards: 
        course_name = course.h5.text #pega todos os nomes dos cursos
        course_price = course.a.text.split()[-1] #pega apenas o valor numérico do curso

        print(f'{course_name} costs {course_price}') #printa o nome do curso e quanto custa