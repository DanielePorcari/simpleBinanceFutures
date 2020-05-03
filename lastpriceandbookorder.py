import simpleBinanceFut

coppia=input("Insert asset: ")
#last price on Futures Binance asset
print("Last price: ",simpleBinanceFut.fbin_ultimo_prezzo(coppia))
book=simpleBinanceFut.fbin_book(coppia)
#all the prices and volumes book orders for the asset
for i in range(len(book['bids'])):
    print(i,"Bids - Price: ",book['bids'][i][0]," Vol.: ",book['bids'][i][1])
for i in range(len(book['asks'])):
    print(i,"Asks - Price: ",book['asks'][i][0]," Vol.: ",book['asks'][i][1])
