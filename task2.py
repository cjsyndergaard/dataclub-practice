# Colton Syndergaard, A02202106
# CS 1400 - 002
# Assn 16 . 2

from deck import Deck
import time

def main():

# Sentinel Values
	playAgain = True
	numOfPlayers = 0
	playerAccounts = []
	playerNames = []

# Get preparatory information for the game. That's what I've cleverly named the game. Kudos to me.
	makeDivision()
	print("Welcome to Fake Jack Black's Fake Blackjack Attack!")
	makeDivision()
	while numOfPlayers not in range(1,6):
		numOfPlayers = int(input("Please enter the number of players, 1-5: "))

	for i in range(numOfPlayers):
		playerAccounts.append(100)

	for i in range(numOfPlayers):
		playerNames.append("Player #" + str(i + 1))


# Start the game!
	while playAgain:

# First thing we need to do is call the class and define all variables that will be used later in the loop.
		deck = Deck()
		deck.shuffle()
		playerHands = []
		dealerPosition =  - 1
		playerScoreList = []
		playerBets = []
		hold = False
		bustValue = 21
		minBet = 5
		playerBet = 0


# Construct the lists. The dealer is the last list in each list
		for i in range(numOfPlayers + 1):
			playerHands.append([])
			for j in range(2):
				playerHands[i].append(deck.draw())

		playerScoreList = getPlayerScores(playerHands)

		for i in range(len(playerAccounts)):
			if playerAccounts[i] <= minBet:
				print(playerNames[i], " you have less than $", minBet, " so you're betting everything (", playerAccounts[i], ").")
				playerBet = playerAccounts[i]
				playerBets.append(playerBet)
			else:
				playerBet = float(input(playerNames[i] + " you have $" + format(playerAccounts[i], ".2f") + ", what is your bet? "))
				if playerBet > playerAccounts[i]:
					print(playerNames[i], " you can't bet more than you have, so you're betting everything.")
					playerBets.append(playerAccounts[i])
				elif playerBet < minBet:
					print(playerNames[i], " you can't bet less than $", format(minBet, ".2f"), ", so that's your bet.")
					playerBets.append(minBet)
				else:
					playerBets.append(playerBet)

		print("The dealer's second card was ", playerHands[dealerPosition][1])

# Here we program the hit/hold dynamic as well as the dealer's actions.
		for i in range(len(playerHands) - 1):
			makeDivision()
			print(playerNames[i], ", you have a score of", playerScoreList[i], "and your hand contains")
			for j in range(len(playerHands[i])):
				print("     ", playerHands[i][j])

			while not hold:
				action = int(input(playerNames[i]+", would you like to hit or hold? Enter 1 for hit, 2 for hold: "))

				if action == 1:
					newCard = deck.draw()
					print("You drew a(n)", newCard)
					playerHands[i].append(newCard)
					playerScoreList = getPlayerScores(playerHands)
					if playerScoreList[i] <= bustValue:
						print(playerNames[i], ", you have a score of", playerScoreList[i], "and your hand consists of ")
						for j in range(len(playerHands[i])):
							print("     ", playerHands[i][j])
					else:
						print(playerNames[i], ", you went bust! Your score was", playerScoreList[i])
						break
				elif action == 2:
					break
		makeDivision()
		print("The dealer's score is ", playerScoreList[dealerPosition], "and his hand contains")
		for j in range(len(playerHands[dealerPosition])):
			print("     ", playerHands[dealerPosition][j])

		while not hold:
			if playerScoreList[dealerPosition] < 17:
				time.sleep(1)
				newCard = deck.draw()
				print("The dealer drew a(n)", newCard)
				playerHands[dealerPosition].append(newCard)
				playerScoreList = getPlayerScores(playerHands)
				print("The dealer's score is ", playerScoreList[dealerPosition], "and his hand contains")
				for j in range(len(playerHands[dealerPosition])):
					print("     ", playerHands[dealerPosition][j])
			elif playerScoreList[dealerPosition] in range(17, 22):
				time.sleep(1)
				print("The dealer holds.")
				break
			else:
				time.sleep(1)
				print("The dealer went bust with a score of", playerScoreList[dealerPosition])
				break
		makeDivision()


# Calculate and display the payouts
		if playerScoreList[dealerPosition] > 21:
			for i in range(len(playerAccounts)):
				if playerScoreList[i] <= 21:
					playerAccounts[i] += playerBets[i]
				else:
					playerAccounts[i] -= playerBets[i]
		else:
			for i in range(len(playerAccounts)):
				if playerScoreList[i] in range(playerScoreList[dealerPosition] + 1, 22):
					playerAccounts[i] += playerBets[i]
				elif playerScoreList[i] == playerScoreList[dealerPosition]:
					playerAccounts[i] += 0 # Strictly speaking, this is unnecessary, I'm just putting it there for my benefit
				elif playerScoreList[i] < playerScoreList[dealerPosition]:
					playerAccounts[i] -= playerBets[i]
				else:
					playerAccounts[i] -= playerBets[i]

		for i in range(len(playerAccounts)):
			print(playerNames[i], ", you bet $", format(playerBets[i], ".2f"), " so you now have $" , format(playerAccounts[i], ".2f"), " in your account.")


# Exit the loop or play again!
		while playAgain != "y" and playAgain != "n":
			makeDivision()
			playAgain = input("Would you like to play again? Y/N: ").lower()
			makeDivision()
			if all (i == 0 for i in playerAccounts):
				print("Actually, no one has any money, so it doesn't matter what you want!")
				playAgain = "n"
			if playAgain == "y":
				deletionList = []
				for i in range(len(playerAccounts)):
					if playerAccounts[i] <= 0:
						deletionList.append(i)
				for i in range(len(deletionList) - 1, -1, -1):
					print("Remember, the house always wins. Goodbye ", playerNames[deletionList[i]])
					del playerAccounts[deletionList[i]]
					del playerBets[deletionList[i]]
					del playerNames[deletionList[i]]
					del playerHands[deletionList[i]]
					del playerScoreList[deletionList[i]]
					if i == 0:
						makeDivision()
				del playerHands[dealerPosition]
				del playerScoreList[dealerPosition]
				print("Very well remaining players, let's begin.")
				makeDivision()
				numOfPlayers = len(playerHands)
				playAgain = True
				break

			elif playAgain == "n":
				playerSort(playerAccounts, playerNames)
				for i in range(len(playerNames)):
					print(playerNames[i], " you're walking away with $", format(playerAccounts[i], ".2f"))
				print("Everyone else (if any), you should have already left with nothing. If you haven't, LEAVE.")

				playAgain = False
				break

	makeDivision()
	print("Thanks for playing! Hopefully you've learned not to gamble, you heathen (though for SOME reason I sincerely doubt it...).")
	makeDivision()


def getPlayerScores(inputList):
	playerScoreList = []
	for i in range(len(inputList)):
		playerScoreList.append([])

	for i in range(len(inputList)):
		for j in range(len(inputList[i])):
			if inputList[i][j].getCardValue() in range(2, 11):
				playerScoreList[i].append(inputList[i][j].getCardValue())
			elif inputList[i][j].getCardValue() in range(11, 14):
				playerScoreList[i].append(10)
			elif inputList[i][j].getCardValue() == 1:
				playerScoreList[i].append(1)
				if sum(playerScoreList[i]) in range(1, 11):
					playerScoreList[i].append(10)

	return [sum(i) for i in playerScoreList]


def playerSort(inputList, nameList):
	for i in range(len(inputList) - 1):
		currMaxIndex = i
		for j in range(i + 1, len(inputList)):
			if inputList[currMaxIndex] < inputList[j]:
				currMaxIndex = j
		if currMaxIndex != i:
			inputList[i], inputList[currMaxIndex] = inputList[currMaxIndex], inputList[i]
			nameList[i], nameList[currMaxIndex] = nameList[currMaxIndex], nameList[i]


def makeDivision():
	print(" ")
	print("----------------------------------------------------")
	print(" ")


main()
