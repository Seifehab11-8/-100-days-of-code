# first printing a block of lines as one statment using '''  ''' 3 single quote print statment or 3 double quotes
tresure_chest = """                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           /'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'//U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-/U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-' """
gameover ="""
             .AMMMMMMMMMMA.
           .AV. :::.:.:.::MA.
          A' :..        : .:`A
         A'..              . `A.
        A' :.    :::::::::  : :`A
        M  .    :::.:.:.:::  . .M
        M  :   ::.:.....::.:   .M
        V : :.::.:........:.:  :V
       A  A:    ..:...:...:.   A A
      .V  MA:.....:M.::.::. .:AM.M
     A'  .VMMMMMMMMM:.:AMMMMMMMV: A
    :M .  .`VMMMMMMV.:A `VMMMMV .:M:
     V.:.  ..`VMMMV.:AM..`VMV' .: V
      V.  .:. .....:AMMA. . .:. .V
       VMM...: ...:.MMMM.: .: MMV
           `VM: . ..M.:M..:::M'
             `M::. .:.... .::M
              M:.  :. .... ..M
              V:  M:. M. :M .V
              `V.:M.. M. :M.V'"""


print("****************************************************************")
print("welcome to treasure island, your mission is to find the treasure")
print("****************************************************************")

checkpoint1 = input("You're running from the pirates, Do you want to go 'left' or 'right'?:\nhint!: right is a water fall\nChoose: ")
checkpoint1 = checkpoint1.lower()
if checkpoint1 == "left":
    checkpoint2 = input("you suddenly face a river 'swim' or 'wait':\n")
    checkpoint2 = checkpoint2.lower()
    if(checkpoint2 == "swim"):
        print("you drowned in the river\nGAMEOVER!!")
        print(gameover)
    else:
        checkpoint3 = input("you found three doors 'yellow' : 'red' : 'blue' \nchoose which door you want to go through :")
        if(checkpoint3 == "yellow"):
            print("you found the treasure, CONGRATULATION")
            print(tresure_chest)
        else:
            print("You were eaten by a beast, GAMEOVER!!")
            print(gameover)
else:
    print("You have fallen in the water fall game over!!")
    print(gameover)
