import requests
import time
from bs4 import BeautifulSoup

def exportData(listOfStocks):
    exportFile = open("stocks.csv", "w")

    #write a header row in the csv file
    headerRow = ""
    for key in listOfStocks[0]:
        headerRow += key+","
    exportFile.write(f"{headerRow}")


    for stock in listOfStocks:
        stockRecord = ""
        #write stock indicators to the file
        for indicator, value in stock.items():
            stockRecord += value+","
        exportFile.write(f"{stockRecord}\n")
    exportFile.close()

    return

def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    symbolsList = ["AJAX.AS", "BVB.DE", "JUVE.MI", "MANU", "CCP.L", "ASR", "SSL.MI", "SLBEN.LS", "OLG.PA", "ADHI"] #ajax, borrussia dortmund, juventus, man united, porto, roma, lazio, benfica, lyon, arsenal
    listOfStockDictionaries = []

    for symbol in symbolsList:
        print(f"Requesting data for {symbol} stock")
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

        #request the page
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        
        stockDictionary = {}
        stockDictionary['Symbol'] = symbol
        counter = 1
        for cell in soup.find_all('td'):
            #odd iterations are keys, so set key on odd numbered iterations
            if counter % 2 != 0:
                key = cell.text
            else:
                #enter key, value info into the dictionary on even iterations
                stockDictionary[key] = cell.text
            
            #increment counter
            counter += 1
        #append stock dictionary to the list of dictionaries
        listOfStockDictionaries.append(stockDictionary)
        #time.sleep(2)
    exportData(listOfStockDictionaries)
main()