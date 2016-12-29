### 1. Pull MTG collection into memory in python interpreter
### 2. For each card in the collection, add a "True" or "False" value (Card Name or ID will be the Key)

### https://mtgjson.com/json/EMN-x.json

import urllib, json, sys

### get data for a selected expansion set (EMN), cards only
link = 'https://mtgjson.com/json/EMN-x.json'
file = urllib.urlopen(link).read()
emnx = json.loads(file)
cards = emnx['cards']

### remove extra data
### http://mtgjson.com/documentation.html for reference
# extras = ['id', 'flavor', 'artist', 'multiverseid', 'variations', 'imageName', 'watermark', 'timeshifted', 'reserved', 'releaseDate', 'starter', 'rulings', 'foreignNames', 'printings', 'originalText', 'originalType', 'legalities']
# for card in cards:
	# for key in extras:
		# try:
			# del card[key]
		# except KeyError:
			# continue

### create a list of all cards by name, sort alphabetically
allcards = []
for i in range(len(cards)):
	allcards.append(cards[i]["name"])
allcards.sort()

ownedcards = {}


### following functions provide simple user interaction (console)
def add_cards():
	print "Write DONE to finish"
	while True:
		name = raw_input('Card name (case sensitive): ')
		if name == 'DONE':
			print "Returning to main menu"
			return
		elif name not in allcards:
			print "Card not found!"
		else:
			if name in ownedcards:
				current = ownedcards[name]
			else:
				current = 0
			quantity = raw_input("Total owned (current: %s): " % current)
			
			ownedcards[name] = quantity
			print "Card added!\n"
	
def view_collection():
	print "Total cards in Eldritch Moon:", len(allcards)
	print "Total cards owned:", len(ownedcards)
	print ""
	owned_sorted = [] #sorting cards alphabetically
	for i in ownedcards:
		owned_sorted.append(i)
	owned_sorted.sort()
	for card in owned_sorted:
		print "%s: %s" % (card, ownedcards[card])
		
def main():
	print "Welcome to MTG collection manager for the Eldritch Moon expansion"
	print "Type in ADD to add cards, VIEW to see current collection or EXIT to quit"
	
	while True:	
		action = raw_input()
		if action == "EXIT":
			break
		elif action == "ADD":
			add_cards()
		elif action == "VIEW":
			view_collection()
		else:
			print "Action not recognised"
	

main()
sys.exit()


### notes for later use
#print cards[0]['type'].encode('cp437', 'ignore')
#https://docs.python.org/2.7/library/codecs.html#codec-base-classes