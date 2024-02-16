# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:28:55 2024

@author: chris
"""

def main():
    game = getGame()
    currentGame = "start"
    keepGoing = True
    while keepGoing:
        currentGame = playNode(game, currentGame)
        if currentGame == "quit":
            keepGoing = False
def getGame():
    game = {
        "start": ["You are on a burning plane that is descending at an alarming rate.", "Accept your fate", "accept", "Head to the cockpit to see what the heck the pilots are doing", "pilot"], 
 "accept": ["Even though it took some time, you accepted your fate on going down with this scorching bird of steel. The moments before the crash felt almost...liberating, but you still died which isn't fun.", "Start over", "start", "Quit", "quit"], 
 "pilot": ["Rushing to the front of the plane amidst the sea of panicking passengers, you head to the cockpit area only to be blocked by a metal door. You peer through and the pilots seem to also...be panicking.", "Give up on the pilots and try looking for a parachute to save yourself", "parachute", "Knock extremely aggressively on the door to get the pilots' attention", "knock"], 
 "parachute": ["Realizing that buying these cheep plane tickets was a mistake, you decided to only rely on yourself and thus you went looking for a parachute. You spend your last moments bumbling about as you had no idea where to look. The plane crashes and cements itself as the iron tomb in which your soul will forever remain. womp womp", "Start over", "start", "Quit", "quit"], 
 "knock": ["Even in the most dire of situations, maintaining proper manners is always important. So you decide to knock, quite furiously, to get the attention of the pilots. They let you in as the more the merrier right?", "Slap the pilots to bring down their hysteria", "slap", "Join them in freaking out and abandon all hope for survival", "freak"], 
 "slap": ["Winding up your hand, you deliver a devastating slap to both pilots thus snapping them out of this daze. They direct you to the supply closet and ask you to give life jackets to the rest of the passengers to prepare for an emergency landing", "Listen and have a good conscience and take time to help the other passengers", "help", "Let your selfishness overcome you and only get a lifejacket for yourself out of self-preservation", "selfish"], 
 "freak": ["Seeing the pilots scream and run about with their arms flailing about seems quite fun! Whether out of your sanity breaking or a genuine want to join in on this dance, you freak out with the other pilots. The plane still crashes though...but at least your last moments were filled with lots of energy and excitement!", "Start over", "start", "Quit", "quit"], 
 "help": ["You rush and get as many lifejackets as you can to the passengers on board, but everyone has a jacket except for you...outside the window you see how it'll only be mere seconds before the plane makes an emergency landing in the water.", "Make a last ditch effort to the supply closet to see if there is still a remaining life jacket", "last", "Have complete faith in your nonexistent swimming abilities", "hope"], 
 "hope": ["Acknowledging that you yourself were never hero material, you decide to act solely in your own interest and procure a life jacket exclusively for yourself. The plane crashes onto the water and while you lived you feel an immense guilt weighing upon you...also the other survivors dragging you down to steal your life jacket may also contribute to that sinking feeling. You actually sink and your body is lost to the depths of the uncaring ocean.", "Start over", "start", "Quit", "quit"], 
 "last": ["You make a rush for the supply closet and manage to get one last life jacket for yourself! The plane crashes onto the water and everyone is alive and breathing...EPIC WIN. You and all the other passengers awkwardly wait for help to come until a helicopter comes rescuing you all the unpleasant fate of being food for the fishes! Nice job. Now you can either move on with your life or relive this traumatic event. What do you do?", "Start over", "start", "Quit", "quit"]
 }
    return game

def playNode(game, currentGame):
    (description, menuA, nodeA, menuB, nodeB) = game[currentGame]
    keepGoing = True
    while keepGoing:
        print (f"""
           {description}
    1) {menuA}
    2) {menuB}
    """)
        response = input("What is your choice? 1 or 2?: ")
        if response == "1":
            nextNode = nodeA
            keepGoing = False
        elif response == "2":
            nextNode = nodeB
            keepGoing = False
        else:
            print("Look...buddy...chum...I know that making choices is difficult especially when these choices determine whether you live or die BUT at least try to play along! THERE ARE ONLY TWO CHOICES AND THERE'S NO ESCAPING IT! You can quit after you've reached an ending sooooo yeah...have fun. Now then where were we? OH yeah!")
            nextNode = currentGame
        return nextNode
main()