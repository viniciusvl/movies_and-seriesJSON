import json 
from itertools import chain
from operator import itemgetter

class Trilha:
    def __init__(self, file, data):
        self.file = file
        self.data = data

    def divide_questao(self):
        self.file.write('\n' + '=' * 60 + '\n')

    def questao_1(self):
        self.file.write('Extraia todos os nomes de filmes disponíveis no JSON.\n\n')
    
        lista = list(chain.from_iterable(data['data'].values())) 
        #data['data] é uma lista que contem duas listas, itertools.chain.from_iterable() serve para juntá-las
        #chain.from_interable junta os dois dicionarios em uma única lista que contém dicionarios
        for c in lista:
            self.file.write(f'{c.get('title')}\n')

        self.divide_questao()

    def questao_2(self):
        self.file.write('Obtenha os títulos de todas as séries presentes no JSON.\n\n')

        series = data.get('data', {}).get('series', {}) #retorna uma lista 
        self.file.write(f'{series[0].get('title')}\n')

        self.divide_questao()
    
    def questao_3(self):
        self.file.write('Identifique qual filme ou série possui o maior valor de rating.\n\n')

        movies = list(chain(data.get('data', {}).get('movies', {}), data.get('data').get('series')))
        #junta as duas listas em uma só, chain = corrente
        rating = -1

        for m in movies:
            if (m.get('rating') > rating):
                rating = m.get('rating')
                nome_maior = m.get('title')
        
        self.file.write(f'{nome_maior} {rating}\n')

        self.divide_questao()

    def questao_4(self):
        self.file.write('Extraia e combine todos os gêneros (genres) sem duplicações.\n\n')

        movies = list(chain(data.get('data',[]).get('movies',[]), data.get('data', {}).get('series', []))) #junta as duas listas em uma
        genres = set()

        for m in movies:
            genres.update(m.get('genres', [])) #adiciona os elementos da lista no set e n adiciona repetidos

        for g in genres:
            self.file.write(f'{g}\n')
        
        self.divide_questao()

    def questao_5(self):
        self.file.write('Conte quantos filmes e quantas séries existem no JSON.\n\n')

        #junta as listas dos filmes e series em uma só
        all = list(chain(data.get('data', []).get('movies', []), data.get('data', []).get('series', []))) 
        actors = []
        previous_movies = []
        quant_movies = len(data.get('data').get('movies'))
        quant_series = len(data.get('data').get('series'))


        for m in all: #itera sobre cada filme e série
            self.file.write(f'{m.get('title')}, {m.get('releaseYear')}\n')
            #adiciona os atores de um filme em uma lista 
            actors.extend(m.get('cast')) 

        for a in actors: 
            if 'previousMovies' in a:
                #salva previousMovies em uma lista
                previous_movies.extend(a.get('previousMovies')) 
                #adiciona na quantidade de filmes existentes
                quant_movies += len(a.get('previousMovies'))
            elif 'previousShows' in a:
                #salva previousShows em uma lista
                previous_movies.extend(a.get('previousShows'))
                quant_series += len(a.get('previousShows'))

        for p in previous_movies: #itera sobre uma lista que contém previousMovies
            self.file.write(f'{p.get('title')}, {p.get('year')}\n')


        self.file.write(f'Series: {quant_series}\n')
        self.file.write(f'Filmes: {quant_movies}\n')

        self.divide_questao()

    def questao_6(self):
        self.file.write('Extraia o nome das plataformas (Netflix, Amazon Prime, HBO Max, etc.).\n\n')

        movies = list(chain(data.get('data').get('movies'), data.get('data').get('series')))
        stream_disp = set()

        for m in movies:
            stream_disp.update(m.get('streaming').keys())
        
        for s in stream_disp:
            self.file.write(f'{s}\n')

        self.divide_questao()

    def questao_7(self):
        self.file.write('Liste apenas aqueles com a resolução 4K no Netflix.\n\n')

        movies = list(chain(data.get('data', []).get('movies', []), data.get('data', []).get('series', [])))
        
        for m in movies:
            if '4K' in m.get('streaming', {}).get('Netflix', {}).get('resolution', []):
                self.file.write(f'{m.get('title')}\n')
        
        self.divide_questao()

    def questao_8(self):
        self.file.write('Para um filme como "The Shawshank Redemption", liste as plataformas disponíveis e os URLs correspondentes.\n\n')

        movies = data.get('data', {}).get('movies', [])

        for m in movies:
            if m.get('title') == "The Shawshank Redemption":
                streaming = m.get('streaming') #salvando todos os streamings em um dicionario 
                break
        
        for s in streaming: # ai iterar em cada key
            if streaming.get(s).get('available'):
                self.file.write(f'{s}: {streaming.get(s).get('url', '')}\n')
        
        self.divide_questao()

    def questao_9(self):
        self.file.write('Extraia o nome de todos os atores e seus respectivos personagens.\n\n')

        movies = list(chain(data.get('data', {}).get('movies', []), data.get('data', {}).get('series', [])))
        cast = list()

        for m in movies:
            cast.extend(m.get('cast'))

        for c in cast:
            self.file.write(f'{c.get('actor')}, {c.get('character')}\n')
        
        self.divide_questao()

    def questao_10(self):
        self.file.write('Encontre o ator que recebeu o maior valor em salary.\n\n')

        movies = list(chain(data.get('data', {}).get('movies', []), data.get('data', {}).get('series', [])))
        actors = list()

        for m in movies:
            actors.extend(m.get('cast'))

        salary = 0.0
        for a in actors:
            if a.get('salary') > salary:
                name_actor = a.get('actor')
                salary = a.get('salary')

        self.file.write(f'{name_actor}, {salary}\n')

        self.divide_questao()

    def questao_11(self):
        self.file.write('Extraia todos os locais em filmingLocations presentes no JSON.\n\n')

        movies = data.get('data', {}).get('movies', [])
        locations = list()

        for m in movies:
            locations = m.get('production', {}).get('filmingLocations', [])

            self.file.write(f'{m.get('title', '')}: {', '.join(locations)}\n') 


        self.divide_questao()

    def questao_12(self):
        self.file.write('Relacione cada filme com o(s) diretor(es).\n\n')

        movies = data.get('data', {}).get('movies', [])
        all_dicrectors = dict()

        for m in movies:
            all_dicrectors[m.get('title')] = ', '.join(m.get('directors')) #salva os diretores em uma string única

        for k, v in all_dicrectors.items():
            self.file.write(f'{k}: {v}\n')

        self.divide_questao()

    def questao_13(self):
        self.file.write('Encontre o filme com o maior valor em revenue dentro de boxOffice.\n\n')

        movies = data.get('data', {}).get('movies', [])
        revenue_max = 0

        for m in movies:
            current_revenue = m.get('production').get('boxOffice').get('revenue')

            if current_revenue > revenue_max:
                revenue_max = current_revenue
                name_max = m.get('title')

        self.file.write(f'{name_max}: {revenue_max}\n')

        self.divide_questao()

    def questao_14(self):
        self.file.write('Some os valores de profit e calcule a média para todos os filmes.\n\n')

        movies = data.get('data', {}).get('movies', [])
        totalProfit = 0

        for m in movies:
            totalProfit += m.get('production', {}).get('boxOffice', {}).get('profit', 0)

        self.file.write(f'Média de lucro dos filmes: {totalProfit/len(movies)}\n')

        self.divide_questao()
    
    def questao_15(self):
        self.file.write('Liste os valores de ticketSales.domestic e ticketSales.international para cada filme.\n\n')

        movies = data.get('data', {}).get('movies', [])

        for m in movies:
            international = m.get('production', {}).get('boxOffice', {}).get('ticketSales', {}).get('international', 0)
            domestic = m.get('production', {}).get('boxOffice', {}).get('ticketSales', {}).get('domestic')

            self.file.write(f'{m.get('title')}: international: {international}, domestic: {domestic}\n')


        self.divide_questao()

    def questao_16(self):
        self.file.write('Extraia o nome dos prêmios, o ano e as categorias associadas.\n\n')

        all = list(chain.from_iterable(data.get('data', {}).values()))
        awards = list()

        for a in all:
            awards.extend(a.get('awards', []))

        for p in awards:
            self.file.write(f'{p.get('award', '')}, {p.get('year', 0)}, {p.get('category', '')}\n')

        self.divide_questao()

    def questao_17(self):
        self.file.write('Liste todos os filmes e séries onde won é true.\n\n')

        all = list(chain.from_iterable(data.get('data', {}).values()))

        for a in all:
            if any(awards.get('won') for awards in a.get('awards')):
                self.file.write(f'{a.get('title')}\n')
        
        self.divide_questao()

    def questao_18(self):
        self.file.write('Encontre os filmes indicados para a categoria de "Best Picture" e organize-os por ano.\n\n')

        movies = data.get('data', {}).get('movies', [])
        movies_picture = dict()

        for m in movies:
            if (awards.get('category') == 'Best Picture' for awards in m.get('awards')):
                movies_picture[m.get('title')] = m.get('releaseYear')

        movies_picture = dict(sorted(movies_picture.items(), key=itemgetter(1)))

        for k, v in movies_picture.items():
            self.file.write(f'{k}: {v}\n')

        self.divide_questao()

    def questao_19(self):
        self.file.write('Encontre o comentário com o maior valor em helpfulVotes.\n\n')

        all = list(chain.from_iterable(data.get('data').values()))
        all_reviews = list()

        for a in all:
            all_reviews.extend(a.get('reviews'))

        helpfulVotes = 0
        for r in all_reviews:
            if r.get('details', {}).get('helpfulVotes') > helpfulVotes:
                nome = r.get('user')
                comment = r.get('comment')

        self.file.write(f'User: {nome}\nComment: {comment}\n')
        
        self.divide_questao()

    def questao_20(self):
        self.file.write('Calcule a média das notas (rating) de todos os filmes.\n\n')

        movies = data.get('data', {}).get('movies', [])
        rating_total = 0

        for m in movies:
            rating_total += m.get('rating')
        
        self.file.write(f'Média: {rating_total/len(movies)}\n')

        self.divide_questao()

    def questao_21(self):
        self.file.write('Liste apenas as avaliações onde a data (date) é anterior a 2022.\n\n')

        all = list(chain.from_iterable(data.get('data', {}).values()))
        all_reviews = list()

        for a in all:
            all_reviews.extend(a.get('reviews'))

        for r in all_reviews:
            year = int(r.get('details', {}).get('date', '')[:4])

            if year < 2022:
                self.file.write(f'{r.get('user')}: {r.get('comment')}\n')

        self.divide_questao()



caminhoResposta = r'C:\Users\Vinícius\Desktop\Projeto Trilha\trilhaAnswer.txt'
caminhoJson = r'C:\Users\Vinícius\Desktop\Projeto Trilha\movies_and_series.json'

with open(caminhoJson, 'r') as arq:
    data = json.load(arq)

    with open(caminhoResposta, 'a', encoding='utf-8') as file:
        trilha = Trilha(file, data)

        trilha.questao_1()
        trilha.questao_2()
        trilha.questao_3()
        trilha.questao_4()
        trilha.questao_5()
        trilha.questao_6()
        trilha.questao_7()
        trilha.questao_8()
        trilha.questao_9()
        trilha.questao_10()
        trilha.questao_11()
        trilha.questao_12()
        trilha.questao_13()
        trilha.questao_14()
        trilha.questao_15()
        trilha.questao_16()
        trilha.questao_17()
        trilha.questao_18()
        trilha.questao_19()
        trilha.questao_20()
        trilha.questao_21()
