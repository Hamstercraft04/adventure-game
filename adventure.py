import time

#startup
print('Stelle dir eine Startmusik vor.')
time.sleep(1)

#deefinitons
def newScreen():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def awatingInput(query, options, option1, option2, option3, option4):
    if options == 2:
        newScreen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2)
    if options == 3:
        newScreen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2, '               <>', option3)
    if options == 4:
        newScreen()
        print('            ', query, '\n\n', '               <>', option1, '\n', '               <>', option2, '               <>', option3, '               <>', option4)

    choice = input('\n\n\n\n\n\n\n\n\n             >> ')

#textboxes
def textbox(sleep, nametag, line1, line2, line3):

    #nametag adjustments
    rawCountNametag = len(nametag)
    CountNametag = int(36) - rawCountNametag
    spaceNametag = CountNametag*str('-') + str('+')

    #line1 adjustments
    rawCountLine1 = len(line1)
    CountLine1 = int(37) - rawCountLine1
    spaceLine1 = CountLine1*str(' ')

    #line2 adjustments
    rawCountLine2 = len(line2)
    CountLine2 = int(37) - rawCountLine2
    spaceLine2 = CountLine2*str(' ')

    #line3 adjustments
    rawCountLine3 = len(line3)
    CountLine3 = int(37) - rawCountLine3
    spaceLine3 = CountLine3*str(' ')

    print('     +--',nametag, spaceNametag)
    print('     |                                        |')
    print('     |', line1, spaceLine1, '|')
    print('     |', line2, spaceLine2, '|')
    print('     |', line3, spaceLine3, '|')
    print('     |                                        |')
    print('     +----------------------------------------+')

    time.sleep(sleep)
    newScreen()

#titlescreen, Art by Korrath
newScreen()
print("                                         -,,,__                                                 \n                                          \\    ``~~--,,__                /   /                   \n                                          /              ``~~--,,_     //--//                   \n                               _,,,,-----,\\              ,,,,---- >   (c  c)\\                   \n                           ,;''            `\\\\,,,,----''''   ,,-'''---/   /_ ;___        -,_     \n                          ( ''---,;====;,----/             (-,,_____/  /'/ `;   '''''----\\ `:.  \n                          (                 '               `      (oo)/   ;~~~~~~~~~~~~~/--~   \n                           `;_           ;    \\            ;   \\   `  ' ,,'                     \n                              ```-----...|     )___________|    )-----'''                       \n                                          /  /,              `\\   \\\\                            \n                                        ,'---\\ \\              ,---`,;,                          \n                                              ```                                               \n\n\n\n\n\n                                        -<[  Schere  -  Stein  -  Drache  ]>- \n\n\n\n\n\n")
input('                                             Press \"ENTER\" to continue \n\n')
newScreen()

#introduction
time.sleep(4)
textbox(4, 'Unbekannter', 'Hallo!', '','')
textbox(3, 'Unbekannter', 'Ich bin Professor E.!', '', '')
textbox(2.5, 'Professor E.', 'Ich werde dein Begleiter sein.', '', '')
textbox(1.5, 'Professor E.', 'Ich werde dein Begleiter sein.', 'Aber leider bin ich sehr vergesslich.', '')
textbox(2, 'Professor E.', 'Ich werde dein Begleiter sein.', 'Aber leider bin ich sehr vergesslich.', 'Wie heißt du nochmal?')
textbox()

#playername
awatingInput('Willst du deinen Vater retten?', 2, 'Ja', 'Nein', '', '')

input()