import cryptocompare



while True :

	choix = input ("Appuyez sur 'L' pour afficher la liste de cryptomonnaie, sinon, Ecrivez le nom de la Cryptomonnaie que vous voulez afficher (BTC, EUR, ETH etc...), appuyez sur 'x' pour quitter :  ")


	if choix =='L':
		print (cryptocompare.get_coin_list(format=True))

		


	elif choix == 'x' :
		break;

	else :
		currency = cryptocompare.get_price(choix)
		print (currency)
