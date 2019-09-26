# Colton Syndergaard, A02202106
# CS 1400 - 002
# Assn 16 . 1

from card import Card
from deck import Deck

def main():
	deck = Deck()
	deck.shuffle()

	getHand = []
	hand = []
	sortType = -1

	for i in range(20):
		newCard = deck.draw()
		getHand.append(newCard)

	nickNamePrinter(getHand)

	print("1. Bubble sort")
	print("2. Insertion Sort")

	while sortType != 1 and sortType != 2:
		sortType = int(input("What kind of sort would you like to do, 1 or 2? "))
		if sortType != 1 and sortType != 2:
			print("Nope, that doesn't make any sense. Choose 1 or 2.")

	if sortType == 1:
		bubbleSort(getHand)
	else:
		insertionSort(getHand)

def bubbleSort(inputList):
	didSwap = True
	while didSwap:
		didSwap = False
		for i in range(len(inputList) - 1):
			if inputList[i].getCardValue() > inputList[i + 1].getCardValue():
				inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
				didSwap = True
		nickNamePrinter(inputList)

def insertionSort(inputList):
	for i in range(1, len(inputList)):
		currElement = inputList[i]
		j = i - 1
		while j >= 0 and inputList[j].getCardValue() > currElement.getCardValue():
			inputList[j + 1] = inputList[j]
			j -= 1

		inputList[j + 1] = currElement
		nickNamePrinter(inputList)

def nickNamePrinter(inputCardList):
	hand = []
	for i in inputCardList:
		nickName = i.getNickName()
		hand.append(nickName)
	print(hand)


main()
