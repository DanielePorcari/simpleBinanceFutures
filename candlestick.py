import simpleBinanceFut
import sys
import dateparser
coppia=sys.argv[1] #asset
intervallo=sys.argv[2] #time frame
limite=sys.argv[3] #number of candles
candles=simpleBinanceFut.fbin_candlestick(coppia,intervallo,limite)
for i in range(len(candles)):
    time=candles[i][0]
    time=str(time)
    print("Time: ",dateparser.parse(time))
    print("OPEN: ",candles[i][1])
    print("HIGH: ",candles[i][2])
    print("LOW:",candles[i][3])
    print("CLOSE:",candles[i][4])
