import pandas as pd

stock_data = pd.read_csv("tata.csv",index_col=0,parse_dates=True)
stock = stock_data.drop(stock_data.columns[0], axis=1)
stock = stock.dropna()
print("\n")

dfResample = stock.resample('5min').ohlc()
#print(dfResample)
def findMaxAndMin(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  MaximumValue = highValues.max()
  MinimumValue = lowValues.min()

  return MaximumValue, MinimumValue
MaximumValue, MinimumValue = findMaxAndMin(dfResample)
print("The maximum value of stock is : ", MaximumValue)
print("The minimum value of stock is : ", MinimumValue, '\n')
def timeStampOfMaxMin(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  MaximumValue, MinimumValue = findMaxAndMin(dfResample)

  timestampOfMaxValue = dfResample.index[highValues == MaximumValue][0]
  timestampOfMinValue = dfResample.index[lowValues == MinimumValue][0]

  return timestampOfMaxValue, timestampOfMinValue
timestampOfMaxValue, timestampOfMinValue = timeStampOfMaxMin(dfResample)
print("The Timestamp of maximum value  stock is : ", timestampOfMaxValue)
print("The Timestamp of minimum value  stock is : ", timestampOfMinValue, end='\n\n')

def findCandleWithMaxMove(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  candleMovement = []
  dataLength = len(dfResample.index)

  for i in range(dataLength):
    candleMovement.append(highValues[i] - lowValues[i])

  dfResample[(stockName, 'candle movement')] = candleMovement

  candleValues = dfResample[(stockName, 'candle movement')]
  candleWithMaxMove = candleValues.max()
  maxMovedCandleDetails = dfResample.loc[dfResample.index[candleValues == candleWithMaxMove]]

  return maxMovedCandleDetails
  #print the Candle with maximum movement
maxMovedCandleDetails = findCandleWithMaxMove(dfResample)
print("Candle with maximum movement is : ", maxMovedCandleDetails, sep='\n\n')