from tradingview_ta import TA_Handler, Interval, Exchange

import coinbasepro as cbp
client = cbp.PublicClient()

import cryptocompare, pickle

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='YOUR_TELEGRAM_BOT_API_TOKEN', use_context=True)
dispatcher = updater.dispatcher

coinlist = ["BTCEUR", "ETHEUR", "LINKEUR", "LTCEUR", "BCHEUR", "XLMEUR", "AAVEEUR", "EOSEUR", "XTZEUR", "SNXEUR", "FILEUR", "GRTEUR", "ETCEUR", "ALGOEUR", "UMAEUR", "OMGEUR", "BANDEUR", "BNTEUR", "NMREUR", "CGLDEUR", "SNXEUR", "NUEUR", "ZRXEUR", "ETHBTC", "LTCBTC", "BCHBTC", "EOSBTC", "DASHBTC", "MKRBTC", "XLMBTC", "ATOMBTC", "XTZBTC", "ETCBTC", "OMGBTC", "ZECBTC", "LINKBTC", "REPBTC", "ZRXBTC", "ALGOBTC", "KNCBTC", "COMPBTC", "BANDBTC", "NMRBTC", "CGLDBTC", "UMABTC", "LRCBTC", "YFIBTC", "UNIBTC", "RENBTC", "WBTCBTC", "BALBTC", "NUBTC", "FILBTC", "AAVEBTC", "GRTBTC", "BNTBTC", "SNXBTC", "BTCUSD", "BTCGBP", "ETHUSD", "ETHGBP", "LTCUSD", "LTCGBP", "BCHUSD", "BCHGBP", "EOSUSD", "DASHUSD", "OXTUSD", "MKRUSD", "XLMUSD", "ATOMUSD", "XTZUSD", "XTZGBP", "ETCUSD", "ETCGBP", "OMGUSD", "OMGGBP", "ZECUSD", "LINKUSD", "LINKGBP", "REPUSD", "ZRXUSD", "ALGOUSD", "ALGOGBP", "DAIUSD", "KNCUSD", "COMPUSD", "BANDUSD", "BANDGBP", "NMRUSD", "NMRGBP", "CGLDUSD", "CGLDGBP", "UMAUSD", "UMAGBP", "LRCUSD", "YFIUSD", "UNIUSD", "RENUSD", "BALUSD", "WBTCUSD", "NUUSD", "NUGBP", "FILUSD", "FILGBP", "AAVEUSD", "GRTUSD", "GRTGBP", "BNTUSD", "BNTGBP", "SNXUSD", "SNXGBP", "BTCUSDC", "ETHUSDC", "ZECUSDC", "BATUSDC", "DAIUSDC", "GNTUSDC", "MANAUSDC", "LOOMUSDC", "CVCUSDC", "DNTUSDC", "LINKETH", "BATETH"]
converter = {"BTCEUR":"BTC-EUR", "ETHEUR":"ETH-EUR", "LINKEUR":"LINK-EUR", "LTCEUR":"LTC-EUR", "BCHEUR":"BCH-EUR", "XLMEUR":"XLM-EUR", "AAVEEUR":"AAVE-EUR", "EOSEUR":"EOS-EUR", "XTZEUR":"XTZ-EUR", "SNXEUR":"SNX-EUR", "FILEUR":"FIL-EUR", "GRTEUR":"GRT-EUR", "ETCEUR":"ETC-EUR", "ALGOEUR":"ALGO-EUR", "UMAEUR":"UMA-EUR", "OMGEUR":"OMG-EUR", "BANDEUR":"BAND-EUR", "BNTEUR":"BNT-EUR", "NMREUR":"NMR-EUR", "CGLDEUR":"CGLD-EUR", "SNXEUR":"SNX-EUR", "NUEUR":"NU-EUR", "ZRXEUR":"ZRX-EUR", "ETHBTC":"ETH-BTC", "LTCBTC":"LTC-BTC", "BCHBTC":"BCH-BTC", "EOSBTC":"EOS-BTC", "DASHBTC":"DASH-BTC", "MKRBTC":"MKR-BTC", "XLMBTC":"XLM-BTC", "ATOMBTC":"ATOM-BTC", "XTZBTC":"XTZ-BTC", "ETCBTC":"ETC-BTC", "OMGBTC":"OMG-BTC", "ZECBTC":"ZEC-BTC", "LINKBTC":"LINK-BTC", "REPBTC":"REP-BTC", "ZRXBTC":"ZRX-BTC", "ALGOBTC":"ALGO-BTC", "KNCBTC":"KNC-BTC", "COMPBTC":"COMP-BTC", "BANDBTC":"BAND-BTC", "NMRBTC":"NMR-BTC", "CGLDBTC":"CGLD-BTC", "UMABTC":"UMA-BTC", "LRCBTC":"LRC-BTC", "YFIBTC":"YFI-BTC", "UNIBTC":"UNI-BTC", "RENBTC":"REN-BTC", "WBTCBTC":"WBTC-BTC", "BALBTC":"BAL-BTC", "NUBTC":"NU-BTC", "FILBTC":"FIL-BTC", "AAVEBTC":"AAVE-BTC", "GRTBTC":"GRT-BTC", "BNTBTC":"BNT-BTC", "SNXBTC":"SNX-BTC", "BTCUSD":"BTC-USD", "BTCGBP":"BTC-GBP", "ETHUSD":"ETH-USD", "ETHGBP":"ETH-GBP", "LTCUSD":"LTC-USD", "LTCGBP":"LTC-GBP", "BCHUSD":"BCH-USD", "BCHGBP":"BCH-GBP", "EOSUSD":"EOS-USD", "DASHUSD":"DASH-USD", "OXTUSD":"OXT-USD", "MKRUSD":"MKR-USD", "XLMUSD":"XLM-USD", "ATOMUSD":"ATOM-USD", "XTZUSD":"XTZ-USD", "XTZGBP":"XTZ-GBP", "ETCUSD":"ETC-USD", "ETCGBP":"ETC-GBP", "OMGUSD":"OMG-USD", "OMGGBP":"OMG-GBP", "ZECUSD":"ZEC-USD", "LINKUSD":"LINK-USD", "LINKGBP":"LINK-GBP", "REPUSD":"REP-USD", "ZRXUSD":"ZRX-USD", "ALGOUSD":"ALGO-USD", "ALGOGBP":"ALGO-GBP", "DAIUSD":"DAI-USD", "KNCUSD":"KNC-USD", "COMPUSD":"COMP-USD", "BANDUSD":"BAND-USD", "BANDGBP":"BAND-GBP", "NMRUSD":"NMR-USD", "NMRGBP":"NMR-GBP", "CGLDUSD":"CGLD-USD", "CGLDGBP":"CGLD-GBP", "UMAUSD":"UMA-USD", "UMAGBP":"UMA-GBP", "LRCUSD":"LRC-USD", "YFIUSD":"YFI-USD", "UNIUSD":"UNI-USD", "RENUSD":"REN-USD", "BALUSD":"BAL-USD", "WBTCUSD":"WBTC-USD", "NUUSD":"NU-USD", "NUGBP":"NU-GBP", "FILUSD":"FIL-USD", "FILGBP":"FIL-GBP", "AAVEUSD":"AAVE-USD", "GRTUSD":"GRT-USD", "GRTGBP":"GRT-GBP", "BNTUSD":"BNT-USD", "BNTGBP":"BNT-GBP", "SNXUSD":"SNX-USD", "SNXGBP":"SNX-GBP", "BTCUSDC":"BTC-USDC", "ETHUSDC":"ETH-USDC", "ZECUSDC":"ZEC-USDC", "BATUSDC":"BAT-USDC", "DAIUSDC":"DAI-USDC", "GNTUSDC":"GNT-USDC", "MANAUSDC":"MANA-USDC", "LOOMUSDC":"LOOM-USDC", "CVCUSDC":"CVC-USDC", "DNTUSDC":"DNT-USDC", "LINKETH":"LINK-ETH", "BATETH":"BAT-ETH"}
marketlist = {"USD":["BTCUSD", "ETHUSD", "LTCUSD", "BCHUSD", "EOSUSD", "DASHUSD", "OXTUSD", "MKRUSD", "XLMUSD", "ATOMUSD", "XTZUSD", "ETCUSD", "OMGUSD", "OMGGBP", "ZECUSD", "LINKUSD", "REPUSD", "ZRXUSD", "ALGOUSD", "DAIUSD", "KNCUSD", "COMPUSD", "BANDUSD", "NMRUSD", "CGLDUSD", "UMAUSD", "LRCUSD", "YFIUSD", "UNIUSD", "RENUSD", "BALUSD", "WBTCUSD", "NUUSD", "FILUSD", "AAVEUSD", "GRTUSD", "BNTUSD", "SNXUSD"], "BTC":["ETHBTC", "LTCBTC", "BCHBTC", "EOSBTC", "DASHBTC", "MKRBTC", "XLMBTC", "ATOMBTC", "XTZBTC", "ETCBTC", "OMGBTC", "ZECBTC", "LINKBTC", "REPBTC", "ZRXBTC", "ALGOBTC", "KNCBTC", "COMPBTC", "BANDBTC", "NMRBTC", "CGLDBTC", "UMABTC", "LRCBTC", "YFIBTC", "UNIBTC", "RENBTC", "WBTCBTC", "BALBTC", "NUBTC", "FILBTC", "AAVEBTC", "GRTBTC", "BNTBTC", "SNXBTC"], "EUR":["BTCEUR", "ETHEUR", "LINKEUR", "LTCEUR", "BCHEUR", "XLMEUR", "AAVEEUR", "EOSEUR", "XTZEUR", "SNXEUR", "FILEUR", "GRTEUR", "ETCEUR", "ALGOEUR", "UMAEUR", "OMGEUR", "BANDEUR", "BNTEUR", "NMREUR", "CGLDEUR", "SNXEUR", "NUEUR", "ZRXEUR"], "GBP":["BTCGBP", "ETHGBP", "LTCGBP", "BCHGBP", "XTZGBP", "ETCGBP", "OMGGBP", "LINKGBP", "ALGOGBP", "BANDGBP", "NMRGBP", "CGLDGBP", "UMAGBP", "FILGBP", "GRTGBP", "BNTGBP", "SNXGBP"], "USDC":["ZECUSDC", "BATUSDC", "DAIUSDC", "GNTUSDC", "MANAUSDC", "LOOMUSDC", "CVCUSDC", "DNTUSDC"], "ETH":["LINKETH", "BATETH"]}

def save_object(object, file_name):
	file_handler = open('{}.pickle'.format(file_name), 'wb')
	pickle.dump(object, file_handler)
	file_handler.close()

def load_object(file_name):
	file_handler = open('{}.pickle'.format(file_name), 'rb')
	loaded_object = pickle.load(file_handler)
	file_handler.close()
	return loaded_object
	
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

def procent(a, b):
	a = int(a*1000000000)
	b = int(b*1000000000)
	if a == b:
		result = 0
	else:
		result = ((b - a) * 100 / a)
	percentage = format(result, '.2f')
	return percentage

def kansen(coin):
 handler = TA_Handler (
        symbol=coin,
        exchange="COINBASE",
        screener="crypto",
        interval=Interval.INTERVAL_1_HOUR
 )

 price = coinbasecheck(coin)
 analysis = handler.get_analysis()
 
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
 elif ((ADX_NEG_DI_1 < ADX_POS_DI_1 and ADX_NEG_DI > ADX_POS_DI) and ((SMA20 >= VWMA and ADX > 35) or (RSI > 70 and RSI1 > RSI) or MACD < signal)):
        advies = "Sell eet."
 elif ((ADX_NEG_DI_1 > ADX_POS_DI_1 and ADX_NEG_DI < ADX_POS_DI) and ((SMA20 <= VWMA and ADX > 35) or (RSI < 30 and RSI1 < RSI) or MACD > signal)):
        advies = "Buy eet."
 else:
        advies = "Hold eet."
 return advies

def vraag(coin):
 handler = TA_Handler (
        symbol=coin,
        exchange="COINBASE",
        screener="crypto",
        interval=Interval.INTERVAL_1_HOUR
 )

 price = coinbasecheck(coin)
 analysis = handler.get_analysis()
 
 ADX = analysis.indicators['ADX']
 MACD = analysis.indicators['MACD.macd']
 signal = analysis.indicators['MACD.signal']
 RSI = analysis.indicators['RSI']
 VWMA = analysis.indicators['VWMA']
 ADX_POS_DI = analysis.indicators['ADX+DI']
 ADX_POS_DI_1 = analysis.indicators['ADX+DI[1]']
 ADX_NEG_DI = analysis.indicators['ADX-DI']
 ADX_NEG_DI_1 = analysis.indicators['ADX-DI[1]']
 SMA20 = analysis.indicators['SMA20']

 if (ADX > 20 and ADX_POS_DI > ADX_NEG_DI and RSI > 50 and VWMA > SMA20 and MACD > signal):
        advies = "Pump eet."
 elif (ADX > 20 and ADX_NEG_DI > ADX_POS_DI and RSI < 50 and VWMA < SMA20 and MACD < signal):
 	advies = "Dump eet."
 else:
 	advies = "Push eet sideways."
 return advies

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=(update.message.text + "?"))

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def stoploss(update, context):
	try:
		coin = ' '.join(context.args).upper()
		context.bot.send_message(chat_id=update.effective_chat.id, text=stoploss_calc(coin)[0])
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat coin ees not valid. Try: BTCEUR, BTCUSD, BTCUSDC, BTCGBP, etc.")

stoploss_handler = CommandHandler('stoploss', stoploss)
dispatcher.add_handler(stoploss_handler)

def exit(update, context):
	coin = ' '.join(context.args).upper()
	exit_strat = ((stoploss_calc(coin)[0] + stoploss_calc(coin)[1]) / 2)
	try:
		context.bot.send_message(chat_id=update.effective_chat.id, text=exit_strat)
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat coin ees not valid. Try: BTCEUR, BTCUSD, BTCUSDC, BTCGBP, etc.")

exit_handler = CommandHandler('exit', exit)
dispatcher.add_handler(exit_handler)

def target(update, context):
	coin = ' '.join(context.args).upper()
	try:
		context.bot.send_message(chat_id=update.effective_chat.id, text=stoploss_calc(coin)[2])
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat coin ees not valid. Try: BTCEUR, BTCUSD, BTCUSDC, BTCGBP, etc.")

target_handler = CommandHandler('target', target)
dispatcher.add_handler(target_handler)

def bogdanoff(update, context):
	try:
		coin = ' '.join(context.args).upper()
		prijs = coinbasecheck(coin)
		stoploss = stoploss_calc(coin)[0]
		exit = stoploss_calc(coin)[1]
		target = stoploss_calc(coin)[2]
		context.bot.send_message(chat_id=update.effective_chat.id, text=vraag(coin))
		context.bot.send_message(chat_id=update.effective_chat.id, text="Buying now with a realistic stoploss of " +str(stoploss)+" and target of "+str(target)+" would either result in a "+str(procent(prijs, target))+"%"+" increase or "+str(procent(stoploss, prijs))+"%"+" decrease in value.")
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat coin ees not valid. Try: BTCEUR, BTCUSD, BTCUSDC, BTCGBP, etc.")

bogdanoff_handler = CommandHandler('bogdanoff', bogdanoff)
dispatcher.add_handler(bogdanoff_handler)

def pumps(update, context):
	try:
		market = ' '.join(context.args).upper()
		context.bot.send_message(chat_id=update.effective_chat.id, text="Let me contemplate...")
		pump_check = 0
		for x in marketlist[market]:
			if (vraag(x) == "Pump eet."):
				context.bot.send_message(chat_id=update.effective_chat.id, text=x)
				pump_check = 1

		if (pump_check == 1):
			context.bot.send_message(chat_id=update.effective_chat.id, text="Zat ees eet.")
		else:
			context.bot.send_message(chat_id=update.effective_chat.id, text="Zer are none.")
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat market ees invalid. Try: USD, EUR, GBP, BTC, ETH or USDC.")
pumps_handler = CommandHandler('pumps', pumps)
dispatcher.add_handler(pumps_handler)

def dumps(update, context):
	try:
		market = ' '.join(context.args).upper()
		context.bot.send_message(chat_id=update.effective_chat.id, text="Let me contemplate...")
		dump_check = 0
		for x in marketlist[market]:
			if (vraag(x) == "Dump eet."):
				context.bot.send_message(chat_id=update.effective_chat.id, text=x)
				dump_check = 1
		if (dump_check == 1):
			context.bot.send_message(chat_id=update.effective_chat.id, text="That ees eet.")
		else:
			context.bot.send_message(chat_id=update.effective_chat.id, text="Zer are none.")
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat market ees invalid. Try: USD, EUR, GBP, BTC, ETH or USDC.")
dumps_handler = CommandHandler('dumps', dumps)
dispatcher.add_handler(dumps_handler)

def subscribe(update, context):
	coin = ' '.join(context.args).upper()
	try:
		sublijst = load_object(str(update.effective_chat.id))
	except:
		sublijst = []
	if coin in coinlist and coin not in sublijst:
		sublijst.append(coin)
		save_object(sublijst, str(update.effective_chat.id))
		context.bot.send_message(chat_id=update.effective_chat.id, text=("We have put "+coin+" on your list."))
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text="You can not bog ze Bogdanoffs.")

subscribe_handler = CommandHandler('subscribe', subscribe)
dispatcher.add_handler(subscribe_handler)

def suball(update, context):
	try:
		sublijst = load_object(str(update.effective_chat.id))
	except:
		sublijst = []
	try:
		market = ' '.join(context.args).upper()
		context.bot.send_message(chat_id=update.effective_chat.id, text="Adding all "+str(market)+" coins...")
		for coin in marketlist[market]:
			if coin in coinlist and coin not in sublijst:
				sublijst.append(coin)
		save_object(sublijst, str(update.effective_chat.id))
		context.bot.send_message(chat_id=update.effective_chat.id, text="Done eet.")
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zer was an unexpected bog.")
suball_handler = CommandHandler('suball', suball)
dispatcher.add_handler(suball_handler)

def unsuball(update, context):
	try:
		sublijst = load_object(str(update.effective_chat.id))
	except:
		sublijst = []
	try:
		market = ' '.join(context.args).upper()
		context.bot.send_message(chat_id=update.effective_chat.id, text="Removing all "+str(market)+" coins...")
		for coin in marketlist[market]:
			if coin in coinlist and coin in sublijst:
				sublijst.remove(coin)
		save_object(sublijst, str(update.effective_chat.id))
		context.bot.send_message(chat_id=update.effective_chat.id, text="Done eet.")
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zer was an unexpected bog.")
unsuball_handler = CommandHandler('unsuball', unsuball)
dispatcher.add_handler(unsuball_handler)

def unsubscribe(update, context):
	coin = ' '.join(context.args).upper()
	try:
		sublijst = load_object(str(update.effective_chat.id))
	except:
		sublijst = []
	if coin in sublijst:
		sublijst.remove(coin)
		save_object(sublijst, str(update.effective_chat.id))
		context.bot.send_message(chat_id=update.effective_chat.id, text=("We have bogged "+coin+" for you."))
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text="You can only bog what ees not yet bogged.")

unsubscribe_handler = CommandHandler('unsubscribe', unsubscribe)
dispatcher.add_handler(unsubscribe_handler)

def sublist(update, context):
	try:
		sublijst = load_object(str(update.effective_chat.id))
	except:
		sublijst = []
	if (sublijst == []):
		context.bot.send_message(chat_id=update.effective_chat.id, text="Your sublist ees empty.")
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text=sublijst)

sublist_handler = CommandHandler('sublist', sublist)
dispatcher.add_handler(sublist_handler)

def identify(update, context):
	users = load_object("userlist")
	if str(update.effective_chat.id) not in users:
		users.append(str(update.effective_chat.id))
		save_object(users, "userlist")
		context.bot.send_message(chat_id=update.effective_chat.id, text="Confirmed.")
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text="We already know eet all.")

identify_handler = CommandHandler('identify', identify)
dispatcher.add_handler(identify_handler)

def moons(update, context):
	try:
		market = ' '.join(context.args).upper()
		context.bot.send_message(chat_id=update.effective_chat.id, text="Let me contemplate...")
		moon_check = 0
		for x in marketlist[market]:
			if (kansen(x) == "Buy eet."):
				context.bot.send_message(chat_id=update.effective_chat.id, text=x)
				moon_check = 1
		if (moon_check == 1):
			context.bot.send_message(chat_id=update.effective_chat.id, text="Zat ees eet.")
		else:
			context.bot.send_message(chat_id=update.effective_chat.id, text="Zer are none.")
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat market ees invalid. Try: USD, EUR, GBP, BTC, ETH or USDC.")
moons_handler = CommandHandler('moons', moons)
dispatcher.add_handler(moons_handler)

def fuds(update, context):
	try:
		market = ' '.join(context.args).upper()
		context.bot.send_message(chat_id=update.effective_chat.id, text="Let me contemplate...")
		fud_check = 0
		for x in marketlist[market]:
			if (kansen(x) == "Sell eet."):
				context.bot.send_message(chat_id=update.effective_chat.id, text=x)
				fud_check = 1
		if (fud_check == 1):
			context.bot.send_message(chat_id=update.effective_chat.id, text="Zat ees eet.")
		else:
			context.bot.send_message(chat_id=update.effective_chat.id, text="Zer are none.")
	except:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Zat market ees invalid. Try: USD, EUR, GBP, BTC, ETH or USDC.")
fuds_handler = CommandHandler('fuds', fuds)
dispatcher.add_handler(fuds_handler)

updater.start_polling()
