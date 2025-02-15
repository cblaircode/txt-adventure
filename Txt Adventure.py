import random
print (r'''                                ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____        ''')



import random

while True:  # Loop to restart the game when needed
    print("\nYou wake up on the ground in a field of overgrown grass and flowers. To the north you spot an old abandoned castle.\n"
          "To the west you see a flowing river. To the east a dark and thick forest. And to the south you see open plains with wildlife.\n"
          "Adventurer, choose your path. But be cautious, one path leads to glory and treasure. The others to certain death.")

    choice = input("Which path do you choose? (North, South, East, West or let fate decide...): ").lower()

    fate = ["north", "south", "east", "west"]
    bridge_1 = ["heads", "tails"]

    if "fate" in choice:
        choice = random.choice(fate)
        print(f"Fate has decided... You go {choice.capitalize()}")

    if "north" in choice:
        choice_2 = input("You make it to the castle. You notice two ways to enter: an outside staircase "
                         "or through the front entrance. Which do you choose? ").lower()
        if "stair" in choice_2:  # Matches "stair", "stairs", "staircase"
            print("You head up the staircase and are immediately attacked by a skeleton. Game Over!")
        elif "front" in choice_2:  # Matches "front", "front entrance"
            castle_entrance = input("You make it inside the entrance of the castle.\n "
                                    "There are three paths to choose from:\n"
                                    "Go upstairs, door to the left, or door to the right: ").lower()
            if "left" in castle_entrance:
                print("The door was booby-trapped, you take an arrow to the chest and die. Game Over!")
            elif "right" in castle_entrance:
                print("The door was booby-trapped. You fall into a hole and die. Game Over!")
            elif "up" in castle_entrance:
                choice_3 = input("You are at the top of the stairs.\n"
                                 "There is a tall door in front of you.\n"
                                 "Do you enter? (yes/no): ").lower()
                if "no" in choice_3:
                    print("We do not deal with the scared. I strike you down with lightning. Game Over!")
                elif "yes" in choice_3:
                    chest_1 = input("You see a chest sitting on the floor. Do you open it? (yes/no): ").lower()
                    if "yes" in chest_1:
                        print("You've chosen poorly. The chest was actually a mimic that bites your face off. Game Over!")
                    elif "no" in chest_1:
                        print("Smart move, but there is no treasure to be found here. Game Over!")
                else:
                    print("It's a simple \"yes\" or \"no\".")
            else:
                print("Choose a path: \"left\", \"right\", or \"upstairs\".")
        else:
            print("You must choose \"staircase\" or \"front entrance\".")

    elif "south" in choice:
        choice_4 = input("As you stroll along the open plains, you notice a bunch of creatures running away from what looks to be a witch's hut. "
                         "Do you approach the hut or follow the creatures? ").lower()
        if "hut" in choice_4:
            print("Did you not read? I said it's a witch's hut. She turned you into a stew. Game Over!")
        elif "follow" in choice_4:
            choice_5 = input("You catch up to the creatures. There are two groups in front of you trying to get you to approach them. "
                             "One group is a pack of wolves, the other is bunnies. Which do you go with? ").lower()
            if "wolf" in choice_5:
                print("You fool! It's a pack of wolves. They eat you. Game Over!")
            elif "bunny" in choice_5:
                print("The bunnies were a safe and cute choice, but they do not have the treasure you seek. Try again!")
            else:
                print("You have to pick \"wolves\" or \"bunnies\".")
        else:
            print("What's it going to be? \"hut\" or \"follow\".")

    elif "east" in choice:
        print("The forest is too dark to venture off into at the moment. Come back when you have the right tools.")

    elif "west" in choice:
        choice_6 = input("As you're getting closer to the river, you notice the water is flowing at a rate too high to swim in.\n"
                         "Your only options are to walk upstream or downstream. ").lower()
        if "up" in choice_6:
            bridge = input("You find yourself at the foot of an old rickety rope bridge. "
                           "Your chances of making it across are fifty-fifty. Do you dare try? (yes/no): ").lower()
            if "yes" in bridge:
                choice_7 = random.choice(bridge_1)
                if choice_7 == "heads":
                    print("The bridge collapses and you drown in the river. Game Over!")
                elif choice_7 == "tails":
                    choice_8 = input("You successfully crossed the bridge, but you are far from danger.\n"
                                     "You hear screaming off in the distance. Do you go towards it or run the opposite direction? ").lower()
                    if "toward" in choice_8:
                        print("The screaming came from someone getting mauled by a bear.\n"
                              "You were more attractive, so the bear came for you. You were mauled. Game Over!")
                    elif "run" in choice_8:
                        choice_9 = input("Smart choice, that screaming was from someone being mauled by a bear. \n"
                                         "While running away, you found an old run-down shed. It looks harmless.\n"
                                         "Do you want to take a look or keep moving? ").lower()
                        if "look" in choice_9:
                            print("Wow, you actually managed to find the treasure. Congratulations!")
                        elif "move" in choice_9:
                            print("You kept moving and got lost in the wilderness. Game Over!")
                        else:
                            print("You must choose \"take a look\" or \"keep moving\".")
                else:
                    print("The bridge is too risky. Choose another path.")
        elif "down" in choice_6:
            print("You walk downstream but find nothing of interest. Try again.")
        else:
            print("You must choose \"upstream\" or \"downstream\".")

    else:
        print("That is not a valid choice. Please try again.")

    # Ask if the player wants to restart
    restart = input("\nWould you like to try again? (yes/no): ").lower()
    if "no" in restart:
        print("Thanks for playing!")
        break




#else:
   # print("Please choose \"north\" or \"south\" or \"west\" or \"east\"")