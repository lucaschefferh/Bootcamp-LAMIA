from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that are you not familiar with') #pergunta se tem alguma skill que voce nao é familiriaziado
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs(): #definicao funcao
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=%22Python%22%2C&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml') #recebe o html do site
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') #cria uma lista com todos os empregos
    for index, job in enumerate(jobs): #for para passar de emprego em emprego
        published_date = ' '.join(job.find('span', class_ = 'sim-posted').text.split()) #pega a data de publicacao
        if 'few' in published_date: #filtra por few days ago
            company_name = ' '.join(job.find('h3', class_ = 'joblist-comp-name').text.split()) #recebe o nome da empresa
            skills = '-'.join(job.find('div', class_ = 'more-skills-sections').text.split()) #recebe as habilidades requeridas 
            more_info = job.header.h2.a['href'] #pega o link para a descrição do emprego

            if unfamiliar_skill not in skills: #filtra com as habilidades não familiarizadas
                with open(f'{index}.txt', 'w') as f: #abre o arquivo numerando ele 
                    f.write(f'Company name: {company_name}\n') #escreve no arquivo a empresa 
                    f.write(f'Required Skills: {skills}\n') #escreve as habilidades requeridas 
                    f.write(f'More info: {more_info}\n') #escreve o link 
            print(f'File saved: {index}') 

if __name__ == '__main__':  #se o arquivo for executado direto fica atualizando a cada 10 minutos.
        find_jobs() #executa a função
        time_wait = 10 
        print(f'Waiting {time_wait} minutes...') 
        time.sleep(time_wait * 60) #tempo de 10 minutos
        