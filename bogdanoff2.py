from tradingview_ta import TA_Handler, Interval, Exchange

import coinbasepro as cbp
client = cbp.PublicClient()

from time import sleep

import cryptocompare, pickle, requests, schedule, time

coinlist = ["BTCEUR", "ETHEUR", "LINKEUR", "LTCEUR", "BCHEUR", "XLMEUR", "AAVEEUR", "EOSEUR", "XTZEUR", "SNXEUR", "FILEUR", "GRTEUR", "ETCEUR", "ALGOEUR", "UMAEUR", "OMGEUR", "BANDEUR", "BNTEUR", "NMREUR", "CGLDEUR", "SNXEUR", "NUEUR", "ZRXEUR", "ETHBTC", "LTCBTC", "BCHBTC", "EOSBTC", "DASHBTC", "MKRBTC", "XLMBTC", "ATOMBTC", "XTZBTC", "ETCBTC", "OMGBTC", "ZECBTC", "LINKBTC", "REPBTC", "ZRXBTC", "ALGOBTC", "KNCBTC", "COMPBTC", "BANDBTC", "NMRBTC", "CGLDBTC", "UMABTC", "LRCBTC", "YFIBTC", "UNIBTC", "RENBTC", "WBTCBTC", "BALBTC", "NUBTC", "FILBTC", "AAVEBTC", "GRTBTC", "BNTBTC", "SNXBTC", "BTCUSD", "BTCGBP", "ETHUSD", "ETHGBP", "LTCUSD", "LTCGBP", "BCHUSD", "BCHGBP", "EOSUSD", "DASHUSD", "OXTUSD", "MKRUSD", "XLMUSD", "ATOMUSD", "XTZUSD", "XTZGBP", "ETCUSD", "ETCGBP", "OMGUSD", "OMGGBP", "ZECUSD", "LINKUSD", "LINKGBP", "REPUSD", "ZRXUSD", "ALGOUSD", "ALGOGBP", "DAIUSD", "KNCUSD", "COMPUSD", "BANDUSD", "BANDGBP", "NMRUSD", "NMRGBP", "CGLDUSD", "CGLDGBP", "UMAUSD", "UMAGBP", "LRCUSD", "YFIUSD", "UNIUSD", "RENUSD", "BALUSD", "WBTCUSD", "NUUSD", "NUGBP", "FILUSD", "FILGBP", "AAVEUSD", "GRTUSD", "GRTGBP", "BNTUSD", "BNTGBP", "SNXUSD", "SNXGBP", "BTCUSDC", "ETHUSDC", "ZECUSDC", "BATUSDC", "DAIUSDC", "GNTUSDC", "MANAUSDC", "LOOMUSDC", "CVCUSDC", "DNTUSDC", "LINKETH", "BATETH"]
converter = {"BTCEUR":"BTC-EUR", "ETHEUR":"ETH-EUR", "LINKEUR":"LINK-EUR", "LTCEUR":"LTC-EUR", "BCHEUR":"BCH-EUR", "XLMEUR":"XLM-EUR", "AAVEEUR":"AAVE-EUR", "EOSEUR":"EOS-EUR", "XTZEUR":"XTZ-EUR", "SNXEUR":"SNX-EUR", "FILEUR":"FIL-EUR", "GRTEUR":"GRT-EUR", "ETCEUR":"ETC-EUR", "ALGOEUR":"ALGO-EUR", "UMAEUR":"UMA-EUR", "OMGEUR":"OMG-EUR", "BANDEUR":"BAND-EUR", "BNTEUR":"BNT-EUR", "NMREUR":"NMR-EUR", "CGLDEUR":"CGLD-EUR", "SNXEUR":"SNX-EUR", "NUEUR":"NU-EUR", "ZRXEUR":"ZRX-EUR", "ETHBTC":"ETH-BTC", "LTCBTC":"LTC-BTC", "BCHBTC":"BCH-BTC", "EOSBTC":"EOS-BTC", "DASHBTC":"DASH-BTC", "MKRBTC":"MKR-BTC", "XLMBTC":"XLM-BTC", "ATOMBTC":"ATOM-BTC", "XTZBTC":"XTZ-BTC", "ETCBTC":"ETC-BTC", "OMGBTC":"OMG-BTC", "ZECBTC":"ZEC-BTC", "LINKBTC":"LINK-BTC", "REPBTC":"REP-BTC", "ZRXBTC":"ZRX-BTC", "ALGOBTC":"ALGO-BTC", "KNCBTC":"KNC-BTC", "COMPBTC":"COMP-BTC", "BANDBTC":"BAND-BTC", "NMRBTC":"NMR-BTC", "CGLDBTC":"CGLD-BTC", "UMABTC":"UMA-BTC", "LRCBTC":"LRC-BTC", "YFIBTC":"YFI-BTC", "UNIBTC":"UNI-BTC", "RENBTC":"REN-BTC", "WBTCBTC":"WBTC-BTC", "BALBTC":"BAL-BTC", "NUBTC":"NU-BTC", "FILBTC":"FIL-BTC", "AAVEBTC":"AAVE-BTC", "GRTBTC":"GRT-BTC", "BNTBTC":"BNT-BTC", "SNXBTC":"SNX-BTC", "BTCUSD":"BTC-USD", "BTCGBP":"BTC-GBP", "ETHUSD":"ETH-USD", "ETHGBP":"ETH-GBP", "LTCUSD":"LTC-USD", "LTCGBP":"LTC-GBP", "BCHUSD":"BCH-USD", "BCHGBP":"BCH-GBP", "EOSUSD":"EOS-USD", "DASHUSD":"DASH-USD", "OXTUSD":"OXT-USD", "MKRUSD":"MKR-USD", "XLMUSD":"XLM-USD", "ATOMUSD":"ATOM-USD", "XTZUSD":"XTZ-USD", "XTZGBP":"XTZ-GBP", "ETCUSD":"ETC-USD", "ETCGBP":"ETC-GBP", "OMGUSD":"OMG-USD", "OMGGBP":"OMG-GBP", "ZECUSD":"ZEC-USD", "LINKUSD":"LINK-USD", "LINKGBP":"LINK-GBP", "REPUSD":"REP-USD", "ZRXUSD":"ZRX-USD", "ALGOUSD":"ALGO-USD", "ALGOGBP":"ALGO-GBP", "DAIUSD":"DAI-USD", "KNCUSD":"KNC-USD", "COMPUSD":"COMP-USD", "BANDUSD":"BAND-USD", "BANDGBP":"BAND-GBP", "NMRUSD":"NMR-USD", "NMRGBP":"NMR-GBP", "CGLDUSD":"CGLD-USD", "CGLDGBP":"CGLD-GBP", "UMAUSD":"UMA-USD", "UMAGBP":"UMA-GBP", "LRCUSD":"LRC-USD", "YFIUSD":"YFI-USD", "UNIUSD":"UNI-USD", "RENUSD":"REN-USD", "BALUSD":"BAL-USD", "WBTCUSD":"WBTC-USD", "NUUSD":"NU-USD", "NUGBP":"NU-GBP", "FILUSD":"FIL-USD", "FILGBP":"FIL-GBP", "AAVEUSD":"AAVE-USD", "GRTUSD":"GRT-USD", "GRTGBP":"GRT-GBP", "BNTUSD":"BNT-USD", "BNTGBP":"BNT-GBP", "SNXUSD":"SNX-USD", "SNXGBP":"SNX-GBP", "BTCUSDC":"BTC-USDC", "ETHUSDC":"ETH-USDC", "ZECUSDC":"ZEC-USDC", "BATUSDC":"BAT-USDC", "DAIUSDC":"DAI-USDC", "GNTUSDC":"GNT-USDC", "MANAUSDC":"MANA-USDC", "LOOMUSDC":"LOOM-USDC", "CVCUSDC":"CVC-USDC", "DNTUSDC":"DNT-USDC", "LINKETH":"LINK-ETH", "BATETH":"BAT-ETH"}
marketlist = {"USD":["BTCUSD", "ETHUSD", "LTCUSD", "BCHUSD", "EOSUSD", "DASHUSD", "OXTUSD", "MKRUSD", "XLMUSD", "ATOMUSD", "XTZUSD", "ETCUSD", "OMGUSD", "OMGGBP", "ZECUSD", "LINKUSD", "REPUSD", "ZRXUSD", "ALGOUSD", "DAIUSD", "KNCUSD", "COMPUSD", "BANDUSD", "NMRUSD", "CGLDUSD", "UMAUSD", "LRCUSD", "YFIUSD", "UNIUSD", "RENUSD", "BALUSD", "WBTCUSD", "NUUSD", "FILUSD", "AAVEUSD", "GRTUSD", "BNTUSD", "SNXUSD"], "BTC":["ETHBTC", "LTCBTC", "BCHBTC", "EOSBTC", "DASHBTC", "MKRBTC", "XLMBTC", "ATOMBTC", "XTZBTC", "ETCBTC", "OMGBTC", "ZECBTC", "LINKBTC", "REPBTC", "ZRXBTC", "ALGOBTC", "KNCBTC", "COMPBTC", "BANDBTC", "NMRBTC", "CGLDBTC", "UMABTC", "LRCBTC", "YFIBTC", "UNIBTC", "RENBTC", "WBTCBTC", "BALBTC", "NUBTC", "FILBTC", "AAVEBTC", "GRTBTC", "BNTBTC", "SNXBTC"], "EUR":["BTCEUR", "ETHEUR", "LINKEUR", "LTCEUR", "BCHEUR", "XLMEUR", "AAVEEUR", "EOSEUR", "XTZEUR", "SNXEUR", "FILEUR", "GRTEUR", "ETCEUR", "ALGOEUR", "UMAEUR", "OMGEUR", "BANDEUR", "BNTEUR", "NMREUR", "CGLDEUR", "SNXEUR", "NUEUR", "ZRXEUR"], "GBP":["BTCGBP", "ETHGBP", "LTCGBP", "BCHGBP", "XTZGBP", "ETCGBP", "OMGGBP", "LINKGBP", "ALGOGBP", "BANDGBP", "NMRGBP", "CGLDGBP", "UMAGBP", "FILGBP", "GRTGBP", "BNTGBP", "SNXGBP"], "USDC":["ZECUSDC", "BATUSDC", "DAIUSDC", "GNTUSDC", "MANAUSDC", "LOOMUSDC", "CVCUSDC", "DNTUSDC"], "ETH":["LINKETH", "BATETH"]}

def load_object(file_name):
	file_handler = open('{}.pickle'.format(file_name), 'rb')
	loaded_object = pickle.load(file_handler)
	file_handler.close()
	return loaded_object

def save_object(object, file_name):
	file_handler = open('{}.pickle'.format(file_name), 'wb')
	pickle.dump(object, file_handler)
	file_handler.close()

def perslist(user):
	try:
		personal_list = load_object(user)
		return personal_list
	except:
		personal_list = []
		save_object(personal_list, user)
		return personal_list

def telegram_bot_sendtext(bot_message, bot_chatID):
	bot_token = 'YOUR_TELEGRAM_BOT_API_TOKEN'
	send_text= 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	response = requests.get(send_text)
	return response.json()

def coinbasecheck(coin):
	datalijst = client.get_product_ticker(converter[coin])
	return datalijst['price']

def stoploss_calc(coin):
 handler = TA_Handler (
        symbol=coin,
        exchange="COINBASE",
        screener="crypto",
        interval=Interval.INTERVAL_1_HOUR
 )

 price = coinbasecheck(coin)
 price_5P = float(price) * 1.05
 price_5M = float(price) * 0.95
 analysis = handler.get_analysis()
 
 fib_mid = analysis.indicators['Pivot.M.Fibonacci.Middle']
 fib_r1 = analysis.indicators['Pivot.M.Fibonacci.R1']
 fib_r2 = analysis.indicators['Pivot.M.Fibonacci.R2']
 fib_r3 = analysis.indicators['Pivot.M.Fibonacci.R3']
 fib_s1 = analysis.indicators['Pivot.M.Fibonacci.S1']
 fib_s2 = analysis.indicators['Pivot.M.Fibonacci.S2']
 fib_s3 = analysis.indicators['Pivot.M.Fibonacci.S3']
 
 if fib_mid < price < fib_r1:
 	return fib_s1, fib_mid, fib_r2
 elif fib_r1 < price < fib_r2:
 	return fib_mid, fib_r1, fib_r3
 elif fib_r2 < price < fib_r3:
 	return fib_r1, fib_r2, price_5P
 elif fib_r3 < price:
 	return fib_r2, fib_r3, price_5P
 elif fib_s1 < price < fib_mid:
 	return fib_s2, fib_s1, fib_r1
 elif fib_s2 < price < fib_s1:
 	return fib_s3, fib_s2, fib_mid
 elif fib_s3 < price < fib_s2:
 	return fib_s3, fib_s3, fib_s1
 elif price < fib_s3:
 	return price_5M, price, fib_s2

def ADX_prev(coin):
 handler = TA_Handler (
        symbol=coin,
        exchange="COINBASE",
        screener="crypto",
        interval=Interval.INTERVAL_1_HOUR
 )

 analysis = handler.get_analysis()
 ADX = analysis.indicators['ADX']
 ADX_prev = load_object("adx_prev")
 ADX_prev[coin] = ADX
 save_object(ADX_prev, "adx_prev")
 return ADX

def vraag(coin):
 handler = TA_Handler (
        symbol=coin,
        exchange="COINBASE",
        screener="crypto",
        interval=Interval.INTERVAL_1_HOUR
 )

 price = coinbasecheck(coin)
 analysis = handler.get_analysis()
 
 try:
 	ADX_load = load_object("adx_prev")
 	ADX_old = ADX_load[coin]
 	#print("Previous ADX is "+str(ADX_old))
 except:
 	ADX_old = ADX_prev(coin)
 	#print("Excepting ADX old.")
 
 ADX = analysis.indicators['ADX']
 MACD = analysis.indicators['MACD.macd']
 signal = analysis.indicators['MACD.signal']
 RSI = analysis.indicators['RSI']
 RSI1 = analysis.indicators['RSI[1]']
 VWMA = analysis.indicators['VWMA']
 ADX_POS_DI = analysis.indicators['ADX+DI']
 ADX_POS_DI_1 = analysis.indicators['ADX+DI[1]']
 ADX_NEG_DI = analysis.indicators['ADX-DI']
 ADX_NEG_DI_1 = analysis.indicators['ADX-DI[1]']
 SMA20 = analysis.indicators['SMA20']

 if (ADX < 25 or 45 < RSI < 55):
 	advies = "Hold eet."
 elif (((ADX_POS_DI > ADX_NEG_DI and ADX < ADX_old) or (ADX_NEG_DI_1 < ADX_POS_DI_1 and ADX_NEG_DI > ADX_POS_DI)) and ((SMA20 >= VWMA and ADX > 35) or (RSI > 70 and RSI1 > RSI) or MACD < signal)):
        advies = "Sell eet."
 elif (((ADX_POS_DI < ADX_NEG_DI and ADX < ADX_old) or (ADX_NEG_DI_1 > ADX_POS_DI_1 and ADX_NEG_DI < ADX_POS_DI)) and ((SMA20 <= VWMA and ADX > 35) or (RSI < 30 and RSI1 < RSI) or MACD > signal)):
        advies = "Buy eet."
 else:
        advies = "Hold eet."
 return advies
	
def procent(a, b):
	a = int(a*1000000000)
	b = int(b*1000000000)
	if a == b:
		result = 0
	else:
		result = ((b - a) * 100 / a)
	percentage = format(result, '.2f')
	return percentage

def checker():
	try:
		prijslijst_prev = load_object("prijslijst_prev")
		users = load_object("userlist")
		vorig_advies = load_object("vorige_adviezen")
		prijslijst_hourly = load_object("prijslijst_hourly")
	
		for user in users:
			for x in perslist(user):
				prijs = coinbasecheck(x)
				stoploss = stoploss_calc(x)[0]
				exit = stoploss_calc(x)[1]
				target = stoploss_calc(x)[2]
				try:
					print(vorig_advies[x])
				except:
					vorig_advies[x] = vraag(x)
				print("Checking for " + user)
				if (vraag(x) == "Sell eet." and vorig_advies[x] != vraag(x)):
					print("Load the " + x +" FUD.")
					telegram_bot_sendtext("Load the "+ x +" FUD.", user)
					telegram_bot_sendtext("For confirmation set " +str(exit)+" as nouveau stoploss.", user)
				elif (vraag(x) == "Buy eet." and vorig_advies[x] != vraag(x)):
					print("Prepare " + x + " for liftoff.")
					telegram_bot_sendtext("Prepare "+ x +" for liftoff.", user)
					telegram_bot_sendtext("Buying now with a stoploss of " +str(stoploss)+" and a target of "+str(target)+" would either result in a "+str(procent(prijs, target))+"%"+" increase or "+str(procent(stoploss, prijs))+"%"+" decrease in value.", user)
				elif (vraag(x) == "Hold eet." and vorig_advies[x] == "Sell eet."):
					telegram_bot_sendtext("He sold " +x+ "? If not, ze moment has passed.", user)
				elif (vraag(x) == "Hold eet." and vorig_advies[x] == "Buy eet."):
					telegram_bot_sendtext("He missed ze " +x+" bottom? Hold eet.", user)
				print("Finished checking " +x)
		
		for user in users:
			for x in perslist(user):
				prijs = coinbasecheck(x)
				vorig_advies[x] = vraag(x)
				prijslijst_prev[x] = prijs
				save_object(prijslijst_prev, "prijslijst_prev")
				save_object(vorig_advies, "vorige_adviezen")
		print("Done.")
	except:
		try:
			telegram_bot_sendtext("I was unable to do ze 5 minute cheque.", 'BOT_ADMIN_CHAT_ID')
		except:
			print("Internet was down.")
def hourly():
	try:
		prijslijst_hourly = load_object("prijslijst_hourly")
		users = load_object("userlist")
		ADX_old = load_object("adx_prev")
		for user in users:
			for x in perslist(user):
				print("Doing hourly check for " +x)
				prijs = float(coinbasecheck(x))
				try:
					five_pos_buffer = prijslijst_hourly[x] * 1.05
					five_neg_buffer = prijslijst_hourly[x] * 0.95
					percentage = procent(prijslijst_hourly[x], prijs)
					if prijs_int > five_pos_buffer:
						telegram_bot_sendtext("Succesfully pumped "+x+" for "+ str(percentage) +"%", user)
					elif prijs_int < five_neg_buffer:
						telegram_bot_sendtext("Powering ze " +x+ " FUD. Hiting ze price with "+ str(percentage) +"%", user)
				except:
					five_pos_buffer = prijs * 1.05
					five_neg_buffer = prijs * 0.95
					percentage = procent(prijs, prijs)
		for user in users:
			for x in perslist(user):
				prijs = coinbasecheck(x)
				ADX_old[x] = ADX_prev(x)
				prijslijst_hourly[x] = prijs
				save_object(ADX_old, "adx_prev")
				save_object(prijslijst_hourly, "prijslijst_hourly")
	except:
		try:
			telegram_bot_sendtext("I was unable to do ze hourly cheque.", 'BOT_ADMIN_CHAT_ID')
		except:
			print("Internet was down.")
schedule.every(5).minutes.do(checker)
schedule.every().hour.at(":00").do(hourly)

while True:
	schedule.run_pending()
	time.sleep(1)
