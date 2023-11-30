import requests
from bs4 import BeautifulSoup 

def carteira():
    busca = input("Qual preço de fii deseja encontrar ? ")
    site = f"https://www.fundsexplorer.com.br/funds/{busca}"
    fiis = requests.get(site)
    if fiis.status_code == 200:
        fii = fiis.content
        dados = BeautifulSoup(fii, "html.parser")
        precofind = dados.find("div", attrs={"class" : "headerTicker__content__price"})
        preco = precofind.find("p")
        print("o preco é de: "+ preco.text) 
        dadofind = dados.findAll("div", attrs={"class" : "indicators__box"})
        for td in dadofind:
            nome = td.find("p")
            print(nome.text)
            numeros = td.find("b")    
            print(numeros.text)
    else:
        print("fiis não encontrado")

if __name__ == "__main__":
    carteira()