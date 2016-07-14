# import some things
import copy
import os
import random
from deuces import Card
from deuces import Evaluator
from deuces import Deck

# team names
team1 = "WHITE"
team2 = "YELLOW"
team3 = "BLUE"
team4 = "RED"

# team starting stacks
team1chips = 144
team2chips = 144
team3chips = 144
team4chips = 144

# introduce the teams...and their phat stacks
_=os.system("clear")
print "Hi there! Want to simulate a poker match?"
ans2 = raw_input("\nHit <enter> when you're ready to start playing :) ")

# playing the game...
keep_playing = "Yes"
while keep_playing == "Yes":
    _=os.system("clear")
    print "Let's play a poker hand!"
    print "\nOK here are the teams and their starting chips:"
    print "\n%s TEAM has %d chips" % (team1, team1chips)
    print "%s TEAM has %d chips" % (team2, team2chips)
    print "%s TEAM has %d chips" % (team3, team3chips)
    print "%s TEAM has %d chips" % (team4, team4chips)
    print "\nWow nice chips!"
    # new deck
    deck = Deck()
    deck.shuffle()
    evaluator = Evaluator()
    print "\nFirst we deal 2 cards to each team..."
    ans3 = raw_input("\nHit <enter> to see the hands: ")
    # random board and hands
    hand1 = deck.draw(2)
    hand2 = deck.draw(2)
    hand3 = deck.draw(2)
    hand4 = deck.draw(2)
    leftovers = deck.draw(44)
    # print the hands
    _=os.system("clear")
    print "%s TEAM has hand " % team1
    Card.print_pretty_cards(hand1)
    print "\n%s TEAM has hand " % team2
    Card.print_pretty_cards(hand2)
    print "\n%s TEAM has hand " % team3
    Card.print_pretty_cards(hand3)
    print "\n%s TEAM has hand " % team4
    Card.print_pretty_cards(hand4)
    print "\nWow nice hands!"
    ans4 = raw_input("\nHit <enter> to continue: ")
    _=os.system("clear")
    # simulate boards
    print "Now let's simulate boards..."
    # win/tie counts
    wins1 = 0
    wins2 = 0
    wins3 = 0
    wins4 = 0
    ties1 = 0
    ties2 = 0
    ties3 = 0
    ties4 = 0
    total_boards = 0
    ans5 = input("\nHow many boards do you want to simulate? ")
    num_boards = ans5
    while num_boards != 0 and type(num_boards) == int:
        for i in range(0,num_boards):
            total_boards += 1
            new_leftovers = copy.deepcopy(leftovers)
            board = [new_leftovers.pop(random.randint(0,len(new_leftovers)-1)) for i in range(5)]
            s1 = evaluator.evaluate(board, hand1)
            s2 = evaluator.evaluate(board, hand2)
            s3 = evaluator.evaluate(board, hand3)
            s4 = evaluator.evaluate(board, hand4)
            s = [s1,s2,s3,s4]
            # compute number of winners
            winners = []
            if s1 == min(s):
                winners += [s1]
            if s2 == min(s):
                winners += [s2]
            if s3 == min(s):
                winners += [s3]
            if s4 == min(s):
                winners += [s4]
            # cases with ties....
            if len(winners) == 1:
                if s1 == min(s):
                    wins1 += 1
                elif s2 == min(s):
                    wins2 += 1
                elif s3 == min(s):
                    wins3 += 1
                else:
                    wins4 += 1
            elif len(winners) == 4:
                ties1 += 1
                ties2 += 1
                ties3 += 1
                ties4 += 1
            elif len(winners) == 3:
                if s1 != min(s):
                    ties2 += 1
                    ties3 += 1
                    ties4 += 1
                elif s2 != min(s):
                    ties1 += 1
                    ties3 += 1
                    ties4 += 1
                elif s3 != min(s):
                    ties1 += 1
                    ties2 += 1
                    ties4 += 1
                else:
                    ties1 += 1
                    ties2 += 1
                    ties3 += 1
            else:
                if s1 == min(s):
                    if s2 == min(s):
                        ties1 += 1
                        ties2 += 1
                    elif s3 == min(s):
                        ties1 += 1
                        ties3 += 1
                    else:
                        ties1 += 1
                        ties4 += 1
                elif s2 == min(s):
                    if s1 == min(s):
                        ties2 += 1
                        ties1 += 1
                    elif s3 == min(s):
                        ties2 += 1
                        ties3 += 1
                    else:
                        ties2 += 1
                        ties4 += 1
                elif s3 == min(s):
                    if s1 == min(s):
                        ties3 += 1
                        ties1 += 1
                    elif s2 == min(s):
                        ties3 += 1
                        ties2 += 1
                    else:
                        ties3 += 1
                        ties4 += 1
                else:
                    if s1 == min(s):
                        ties4 += 1
                        ties1 += 1
                    elif s2 == min(s):
                        ties4 += 1
                        ties2 += 1
                    else:
                        ties4 += 1
                        ties3 += 1
        _=os.system("clear")
        print "OK so far we've simulated %s boards..." % total_boards
        print "\n%s TEAM won %d times -> approx %f" % (team1, wins1, float(wins1)/float(total_boards))
        print "%s TEAM tied %d times -> approx %f" % (team1, ties1, float(ties1)/float(total_boards))
        print "\n%s TEAM won %d times -> approx %f" % (team2, wins2, float(wins2)/float(total_boards))
        print "%s TEAM tied %d times -> approx %f" % (team2, ties2, float(ties2)/float(total_boards))
        print "\n%s TEAM won %d times -> approx %f" % (team3, wins3, float(wins3)/float(total_boards))
        print "%s TEAM tied %d times -> approx %f" % (team3, ties3, float(ties3)/float(total_boards))
        print "\n%s TEAM won %d times -> approx %f" % (team4, wins4, float(wins4)/float(total_boards))
        print "%s TEAM tied %d times -> approx %f" % (team4, ties4, float(ties4)/float(total_boards))
        print "\nDo you want to simulate more boards?"
        ans6 = input("Enter how many or just 0 if you're done: ")
        num_boards = ans6
    _=os.system("clear")
    print "OK now it's time to place your bets..."
    print "\nRecall from our simulations the following information:"
    print "\nWe simulated a total of %d boards and..." % total_boards
    print "%s TEAM won %d times -> approx %f" % (team1, wins1, float(wins1)/float(total_boards))
    print "%s TEAM won %d times -> approx %f" % (team2, wins2, float(wins2)/float(total_boards))
    print "%s TEAM won %d times -> approx %f" % (team3, wins3, float(wins3)/float(total_boards))
    print "%s TEAM won %d times -> approx %f" % (team4, wins4, float(wins4)/float(total_boards))
    print "There were also some ties...anyways..."
    print "\nRULES FOR BETTING:"
    print "Each team must bet 0 or 12 chips..."
    print "If at least 1 team bets 12 chips, then Jody and Tom each put in 6 chips (they're so nice)!"
    print "All teams that bet 12 chips then compete for all the chips!"
    ans7 = raw_input("\nHit <enter> when you're ready to bet: ")
    _=os.system("clear")
    bet1 = input("How much does the %s TEAM bet? " % team1)
    bet2 = input("How much does the %s TEAM bet? " % team2)
    bet3 = input("How much does the %s TEAM bet? " % team3)
    bet4 = input("How much does the %s TEAM bet? " % team4)
    potsize = 12+bet1+bet2+bet3+bet4
    print "\nWow nice bets!"
    print "\nAfter betting we have %d chips up for grabs in the pot" % potsize
    print "\nHere are updated chipstacks for each team after betting:"
    print "%s TEAM has %d - %d = %d chips" % (team1,team1chips,bet1,team1chips-bet1)
    team1chips -= bet1
    print "%s TEAM has %d - %d = %d chips" % (team2,team2chips,bet2,team2chips-bet2)
    team2chips -= bet2
    print "%s TEAM has %d - %d = %d chips" % (team3,team3chips,bet3,team3chips-bet3)
    team3chips -= bet3
    print "%s TEAM has %d - %d = %d chips" % (team4,team4chips,bet4,team4chips-bet4)
    team4chips -= bet4
    ans7_1 = raw_input("\nHit <enter> to continue: ")
    _=os.system("clear")
    print "Now we simulate a single game for %s chips!" % potsize
    ans8 = raw_input("\nHit <enter> when you're ready: ")
    _=os.system("clear")
    new_leftovers = copy.deepcopy(leftovers)
    board = [new_leftovers.pop(random.randint(0,len(new_leftovers)-1)) for i in range(5)]
    print "The random board is:"
    Card.print_pretty_cards(board)
    # hand ranks
    s1 = evaluator.evaluate(board, hand1)
    s2 = evaluator.evaluate(board, hand2)
    s3 = evaluator.evaluate(board, hand3)
    s4 = evaluator.evaluate(board, hand4)
    # print the hands
    print "\n%s TEAM bet %d, has hand rank %d, and has hand:" % (team1,bet1,s1)
    Card.print_pretty_cards(hand1)
    print "\n%s TEAM bet %d, has hand rank %d, and has hand:" % (team2,bet2,s2)
    Card.print_pretty_cards(hand2)
    print "\n%s TEAM bet %d, has hand rank %d, and has hand:" % (team3,bet3,s3)
    Card.print_pretty_cards(hand3)
    print "\n%s TEAM bet %d, has hand rank %d, and has hand:" % (team4,bet4,s4)
    Card.print_pretty_cards(hand4)
    print "\nThe total potsize is (%d+%d+%d+%d)+12 = %d" % (bet1,bet2,bet3,bet4,potsize)
    print "\nLet's record what happened:"
    chipchange1 = input("How many chips does %s TEAM get from the pot? " % team1)
    chipchange2 = input("How many chips does %s TEAM get from the pot? " % team2)
    chipchange3 = input("How many chips does %s TEAM get from the pot? " % team3)
    chipchange4 = input("How many chips does %s TEAM get from the pot? " % team4)
    ans9 = raw_input("\nHit <enter> to update chips: ")
    team1chips += chipchange1
    team2chips += chipchange2
    team3chips += chipchange3
    team4chips += chipchange4
    # summarize end of hand chips
    print "\nHere are the updated chip totals:"
    print "%s TEAM has %d - %d + %d = %d chips" % (team1, team1chips-chipchange1+bet1, bet1, chipchange1, team1chips)
    print "%s TEAM has %d - %d + %d = %d chips" % (team2, team2chips-chipchange2+bet2, bet2, chipchange2, team2chips)
    print "%s TEAM has %d - %d + %d = %d chips" % (team3, team3chips-chipchange3+bet3, bet3, chipchange3, team3chips)
    print "%s TEAM has %d - %d + %d = %d chips" % (team4, team4chips-chipchange4+bet4, bet4, chipchange4, team4chips)
    # stop playing
    final_answer = raw_input("\nDo you want to play again? ")
    if final_answer == "N" or final_answer == "No" or final_answer == "no":
        keep_playing = "No"
        finalfinalans = raw_input("\nAre you SURE you're done with this game? ")
# summarize end of game
_=os.system("clear")
print "\nOK here are the chip totals at the end of the game:"
print "%s TEAM has %d chips" % (team1, team1chips)
print "%s TEAM has %d chips" % (team2, team2chips)
print "%s TEAM has %d chips" % (team3, team3chips)
print "%s TEAM has %d chips" % (team4, team4chips)
