# Gomoku-Row in five

import pygame
import time



# RGB color code
PERU= (205,133,63)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED = (255,0,0)

# initialize
pygame.init()
clock=pygame.time.Clock()
pygame.font.init()

# Creat an 1024*768 sized screen

screen = pygame.display.set_mode([1024,768])

# Set the title of the window
pygame.display.set_caption("Gomoku-Row in five")

# All Lists
# TotalPiecesTestList：
# 1. For each move, test if the black/white pieces are already existed in the board
# 2. The “pieces” which already in the List are use as boundary to restrict and \
# analyse pieces connecting near the boundary
TotalPiecesTestList = [[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[6,-1],\
                       [7,-1],[8,-1],[9,-1],[10,-1],[11,-1],[12,-1],[13,-1],\
                       [14,-1],[15,-1],\
                       
                       [15,0],[15,1],[15,2],[15,3],[15,4],[15,5],[15,6],[15,7],\
                       [15,8],[15,9],[15,10],[15,11],[15,12],[15,13],[15,14],[15,15],\
                       
                       [14,15],[13,15],[12,15],[11,15],[10,15],[9,15],[8,15],[7,15],\
                       [6,15],[5,15],[4,15],[3,15],[2,15],[1,15],[0,15],[-1,15],\
                       
                       [-1,14],[-1,13],[-1,12],[-1,11],[-1,10],[-1,9],[-1,8],[-1,7],\
                       [-1,6],[-1,5],[-1,4],[-1,3],[-1,2],[-1,1],[-1,0]]


BlackPiecesDisplayList = [] # Actual coordinates 
BlackPiecesWinList = [] # Minimised assumed coordinate to check the win condition

WhitePiecesDisplayList = [] # Actual coordinate 
WhitePiecesWinList = [] # Minimised assumed coordinate to check the win condition



Player1scoreList = [0] # Present the Score for player 1
Player2scoreList = [0] # Present the Score for player 2

PlayerNameList = [str("AI")] # Players' names and AI.






##########################################################
# This class includes the function of black pieces and white pieces’ win condition.
class TotalPieces():
    

    # Black Pieces Win condition
    def BlackPiecesPosition(): 

        # Go through and check all the black pieces which on the board.      
        for i in range(len(BlackPiecesWinList)):
            global WinBlack # Set global veriable since it might be changed.
            global TieGame

            # Win conditions
            # 1. Horizontal five black pieces
                    
            if (([(BlackPiecesWinList[i][0])+1, BlackPiecesWinList[i][1]]) in BlackPiecesWinList) and \
               (([(BlackPiecesWinList[i][0])+2, BlackPiecesWinList[i][1]]) in BlackPiecesWinList) and \
               (([(BlackPiecesWinList[i][0])+3, BlackPiecesWinList[i][1]]) in BlackPiecesWinList) and \
               (([(BlackPiecesWinList[i][0])+4, BlackPiecesWinList[i][1]]) in BlackPiecesWinList):
                WinBlack = 1 # For this point, if all these four black pieces are also one the board,
                             # which means there are five same color continuous pieces. 
                        
            # 2. Vertical five black pieces 
            elif (([BlackPiecesWinList[i][0],(BlackPiecesWinList[i][1])+1]) in BlackPiecesWinList) and \
                 (([BlackPiecesWinList[i][0],(BlackPiecesWinList[i][1])+2]) in BlackPiecesWinList) and \
                 (([BlackPiecesWinList[i][0],(BlackPiecesWinList[i][1])+3]) in BlackPiecesWinList) and \
                 (([BlackPiecesWinList[i][0],(BlackPiecesWinList[i][1])+4]) in BlackPiecesWinList):
                WinBlack = 1
                   
            # 3. -45 degree five black pieces
            elif (([(BlackPiecesWinList[i][0])+1, (BlackPiecesWinList[i][1])+1]) in BlackPiecesWinList) and \
                 (([(BlackPiecesWinList[i][0])+2, (BlackPiecesWinList[i][1])+2]) in BlackPiecesWinList) and \
                 (([(BlackPiecesWinList[i][0])+3, (BlackPiecesWinList[i][1])+3]) in BlackPiecesWinList) and \
                 (([(BlackPiecesWinList[i][0])+4, (BlackPiecesWinList[i][1])+4]) in BlackPiecesWinList):
                WinBlack = 1
                        
            # 4. 45 degree five black pieces
            elif (([(BlackPiecesWinList[i][0])+1, (BlackPiecesWinList[i][1])-1]) in BlackPiecesWinList) and \
                 (([(BlackPiecesWinList[i][0])+2, (BlackPiecesWinList[i][1])-2]) in BlackPiecesWinList) and \
                 (([(BlackPiecesWinList[i][0])+3, (BlackPiecesWinList[i][1])-3]) in BlackPiecesWinList) and \
                 (([(BlackPiecesWinList[i][0])+4, (BlackPiecesWinList[i][1])-4]) in BlackPiecesWinList):
                WinBlack = 1
            # Since it will search every black piece, so there is no need\
            # to search 8 directions. 4 directions are enough.


        if WinBlack == 1: # In convention, black always goes first in every round.
            if Round % 2 != 0: # Round 1,3,5,7,9... player 1 uses black pieces and go first. 
                Player1scoreList[0]=Player1scoreList[0]+1
                
            else: # Round 2,4,6,8,10... player 2 uses black pieces and go first. 
                Player2scoreList[0]=Player2scoreList[0]+1
                
        if len(TotalPiecesTestList) == 289: # 15*15 = 225 + 64(outside of boundary) point = 289
            TieGame = 1                     

                        
    # White Pieces Win condition                                                                       
    def WhitePiecesPosition():

        
        # Go through all the white pieces which on the board. 
        for i in range(len(WhitePiecesWinList)):
            global WinWhite # Set global veriable since it might be changed
            global TieGame

            # Win conditions 
            # 1. Horizontal five white pieces
            if (([(WhitePiecesWinList[i][0])+1, WhitePiecesWinList[i][1]]) in WhitePiecesWinList) and \
               (([(WhitePiecesWinList[i][0])+2, WhitePiecesWinList[i][1]]) in WhitePiecesWinList) and \
               (([(WhitePiecesWinList[i][0])+3, WhitePiecesWinList[i][1]]) in WhitePiecesWinList) and \
               (([(WhitePiecesWinList[i][0])+4, WhitePiecesWinList[i][1]]) in WhitePiecesWinList):
                WinWhite = 1

            # 2. Vertical five white pieces
            elif (([WhitePiecesWinList[i][0],(WhitePiecesWinList[i][1])+1]) in WhitePiecesWinList) and \
                 (([WhitePiecesWinList[i][0],(WhitePiecesWinList[i][1])+2]) in WhitePiecesWinList) and \
                 (([WhitePiecesWinList[i][0],(WhitePiecesWinList[i][1])+3]) in WhitePiecesWinList) and \
                 (([WhitePiecesWinList[i][0],(WhitePiecesWinList[i][1])+4]) in WhitePiecesWinList):
                WinWhite = 1

            # 5. -45 degree five white pieces
            elif (([(WhitePiecesWinList[i][0])+1, (WhitePiecesWinList[i][1])+1]) in WhitePiecesWinList) and \
                 (([(WhitePiecesWinList[i][0])+2, (WhitePiecesWinList[i][1])+2]) in WhitePiecesWinList) and \
                 (([(WhitePiecesWinList[i][0])+3, (WhitePiecesWinList[i][1])+3]) in WhitePiecesWinList) and \
                 (([(WhitePiecesWinList[i][0])+4, (WhitePiecesWinList[i][1])+4]) in WhitePiecesWinList):
                WinWhite = 1

            # 7. 45 degree five white pieces
            elif (([(WhitePiecesWinList[i][0])+1, (WhitePiecesWinList[i][1])-1]) in WhitePiecesWinList) and \
                 (([(WhitePiecesWinList[i][0])+2, (WhitePiecesWinList[i][1])-2]) in WhitePiecesWinList) and \
                 (([(WhitePiecesWinList[i][0])+3, (WhitePiecesWinList[i][1])-3]) in WhitePiecesWinList) and \
                 (([(WhitePiecesWinList[i][0])+4, (WhitePiecesWinList[i][1])-4]) in WhitePiecesWinList):
                WinWhite = 1

        if WinWhite == 1: # In convention,white always goes second. 
            if Round % 2 != 0: # Round 1,3,5,7,9... player 2 uses white pieces and go second.
                Player2scoreList[0]=Player2scoreList[0]+1
                
            else: # Round 2,4,6,8,10... player 1 uses white pieces and go second.
                Player1scoreList[0]=Player1scoreList[0]+1
        if len(TotalPiecesTestList) == 289:
            TieGame = 1



            
##########################################################                        
# Function keys
class Operator():

    # When one round is finished, click ReStart to continue. 
    def ReStart():
        global WinWhite
        global TieGame
        global WinBlack
        
        
        if (WinBlack == 1) or (WinWhite == 1) or (TieGame == 1): # Only can be clicked when black or white wins.
            # Clear everything on the board
            global TotalPiecesTestList

            # Remain the boundary pieces
            TotalPiecesTestList = [[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[6,-1],\
                       [7,-1],[8,-1],[9,-1],[10,-1],[11,-1],[12,-1],[13,-1],\
                       [14,-1],[15,-1],\
                       
                       [15,0],[15,1],[15,2],[15,3],[15,4],[15,5],[15,6],[15,7],\
                       [15,8],[15,9],[15,10],[15,11],[15,12],[15,13],[15,14],[15,15],\
                       
                       [14,15],[13,15],[12,15],[11,15],[10,15],[9,15],[8,15],[7,15],\
                       [6,15],[5,15],[4,15],[3,15],[2,15],[1,15],[0,15],[-1,15],\
                       
                       [-1,14],[-1,13],[-1,12],[-1,11],[-1,10],[-1,9],[-1,8],[-1,7],\
                       [-1,6],[-1,5],[-1,4],[-1,3],[-1,2],[-1,1],[-1,0]]
                       

            BlackPiecesDisplayList.clear()
            BlackPiecesWinList.clear()
            WhitePiecesDisplayList.clear()
            WhitePiecesWinList.clear()
            WinBlack = 0
            WinWhite = 0
            TieGame = 0
            global Round
            Round = Round + 1

            
    # Retract a false move
    def Undo():

        turn = 1 # without this, 2 pieces will be removeved in the same time
        # 1. Undo Blackpieces
        if len(BlackPiecesDisplayList) > len(WhitePiecesDisplayList):
            if BlackPiecesDisplayList == []: # Empty board, nothing to Undo
                pass
            else:
                # Undo the last piece
                BlackPiecesDisplayList.pop(-1) 
                BlackPiecesWinList.pop(-1)
                TotalPiecesTestList.pop(-1)
                turn = 0 # This is used to constrain the white pieces.
                         # Since black pieces always goes first so if the black piece\
                         # is retracted, the number of black pieces will be equal to the\
                         # number of white pieces,which means in the next if statement the\
                         # white piece will be cleared automatically in one click.
                
               
        # 2. Undo Whitepieces
        if len(BlackPiecesDisplayList) == len(WhitePiecesDisplayList):
            if WhitePiecesDisplayList == []: # Empty board, nothing to Undo.
                pass
            elif turn == 1:
                WhitePiecesDisplayList.pop(-1)
                WhitePiecesWinList.pop(-1)
                TotalPiecesTestList.pop(-1)
                
    # Back to initial Interface
    def Quit():
        # Reset all the variables and lists back to initial value

        global Interface
        Interface = 1 

        global PVP
        PVP = 0

        global PVE
        PVE = 0
        
        global TotalPiecesTestList
        TotalPiecesTestList = [[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[6,-1],\
                       [7,-1],[8,-1],[9,-1],[10,-1],[11,-1],[12,-1],[13,-1],\
                       [14,-1],[15,-1],\
                       
                       [15,0],[15,1],[15,2],[15,3],[15,4],[15,5],[15,6],[15,7],\
                       [15,8],[15,9],[15,10],[15,11],[15,12],[15,13],[15,14],[15,15],\
                       
                       [14,15],[13,15],[12,15],[11,15],[10,15],[9,15],[8,15],[7,15],\
                       [6,15],[5,15],[4,15],[3,15],[2,15],[1,15],[0,15],[-1,15],\
                       
                       [-1,14],[-1,13],[-1,12],[-1,11],[-1,10],[-1,9],[-1,8],[-1,7],\
                       [-1,6],[-1,5],[-1,4],[-1,3],[-1,2],[-1,1],[-1,0]]


        BlackPiecesDisplayList.clear()
        BlackPiecesWinList.clear()
        WhitePiecesDisplayList.clear()
        WhitePiecesWinList.clear()

        global WinBlack
        WinBlack = 0

        global WinWhite
        WinWhite = 0

        global TieGame
        TieGame = 0
        
        global Player1scoreList
        Player1scoreList = [0]

        global Player2scoreList
        Player2scoreList = [0]
        
        global Round
        Round = 1

        global Name
        Name = 0

        global PlayerNameList
        PlayerNameList = [str("AI")]
        
    # Get help from AI
    def Help():
        
        Turn = 1 # Same reason in the Undo, to constrain and make only one piece\
                 # will be added in one click.
        
        global Round # The reason here needs to change Round is the order and value of \
                     # each point is decided by the number of round. In AI's function \
                     # for example in Round 1, AI is white piece, but in here, we need AI \
                     # to be not only white but also black since both black and white need be \
                     # helped in this function. So by increasing Round to (Round + 1), AI will \
                     # think it is in Round 2 and change to black piece mode, so in this case \
                     # it can help both white and black. And most important is the (Round + 1) is decreased \
                     # back to Round before refresh the screen so it wound not affect the playerinformation.
                     
        if Round % 2 != 0:
            if len(BlackPiecesDisplayList) == len(WhitePiecesDisplayList) and Turn == 1:
                Round = Round + 1 # Change to even number Round.
                AI.Evaluate() 
                AI.Set() # So AI will analyse black piece.
                Round = Round - 1 # Change back to odd number Round.
                Turn = 0
        
            if len(BlackPiecesDisplayList) > len(WhitePiecesDisplayList) and Turn == 1:
                AI.Evaluate()
                AI.Set()
                
        elif Round % 2 == 0 :
            if len(BlackPiecesDisplayList) == len(WhitePiecesDisplayList) and Turn == 1:
                AI.Evaluate()
                AI.Set()
                Turn = 0
        
            if len(BlackPiecesDisplayList) > len(WhitePiecesDisplayList) and Turn == 1:
                Round = Round + 1 # Change to odd number Round.
                AI.Evaluate()
                AI.Set() # So AI will analyse white piece.
                Round = Round - 1 # Change back to even number Round.



        
##########################################################
# This class includes all the draw functions               
class Draw():

    # Draw the starting page Interface
    
    def StartInterface(screen):
        
        global RemindPVP # These variables might be changed
        global RemindPVE
        global RemindQuitGame
        
        # Set font
        GameNameText = pygame.font.SysFont("Helvetica",100)
        GameRules = pygame.font.SysFont("Helvetica",40)
        GameModeText = pygame.font.SysFont("Helvetica",60)
        RemindText = pygame.font.SysFont("Helvetica",45)
        
        GameName = GameNameText.render("Gomoku - row in five",1,(0,0,0))
        screen.blit(GameName,(175,65))

        # Rules
        Rules1 = GameRules.render("Rules: 1. Black plays first "\
                                  "and white play second, and only one ",1,(0,0,0))
        Rules2 = GameRules.render("different color piece one will be "\
                                  "placed on the board.",1,(0,0,0))

        Rules3 = GameRules.render("2. If 5 continuously same color pieces "\
                                  "are in a straight",1,(0,0,0))
        Rules4 = GameRules.render("line in any directions, that player wins.",1,(0,0,0))
        
        screen.blit(Rules1,(90,170))
        screen.blit(Rules2,(215,215))
        screen.blit(Rules3,(183,260))
        screen.blit(Rules4,(215,305))

        # PVP
        GameModePVP = GameModeText.render("PVP",1,(0,0,0))
                    
        screen.blit(GameModePVP,(222,440))
        pygame.draw.line(screen,BLACK,(215,435),(307,435),2)
        pygame.draw.line(screen,BLACK,(307,435),(307,478),2)
        pygame.draw.line(screen,BLACK,(307,478),(215,478),2)
        pygame.draw.line(screen,BLACK,(215,478),(215,435),2)
        

        if RemindPVP == 1: # introduce the PVP mode.
            
            RemindPVP = RemindText.render("Click PVP to play with your friend.",1,(0,0,0))
 
            screen.blit(RemindPVP,(200,500))

            RemindPVP = 0
            
        
        # PVE
        GameModePVE = GameModeText.render("PVE",1,(0,0,0))
        
        screen.blit(GameModePVE,(470,440))
        pygame.draw.line(screen,BLACK,(463,435),(555,435),2)
        pygame.draw.line(screen,BLACK,(555,435),(555,478),2)
        pygame.draw.line(screen,BLACK,(555,478),(463,478),2)
        pygame.draw.line(screen,BLACK,(463,478),(463,435),2)
        
        if RemindPVE == 1: # introduce the PVE mode.
            
            RemindPVE = RemindText.render("Click PVE to play with computer.",1,(0,0,0))
 
            screen.blit(RemindPVE,(200,500))

            RemindPVE = 0

        # Quit
        Quit = GameModeText.render("Quit",1,(0,0,0))
        screen.blit(Quit,(718,440))

        pygame.draw.line(screen,BLACK,(711,435),(812,435),2)
        pygame.draw.line(screen,BLACK,(812,435),(812,478),2)
        pygame.draw.line(screen,BLACK,(812,478),(711,478),2)
        pygame.draw.line(screen,BLACK,(711,478),(711,435),2)
        if RemindQuitGame == 1: # introduce the Quit.
            
            RemindQuitGame = RemindText.render("Click Quit to end the game.",1,(255,0,0))
 
            screen.blit(RemindQuitGame,(200,500))

            RemindQuitGame = 0
        

    # Draw the chess baord
    def Board(screen):
        # Draw the lines on the board
        for i in range(15):
            if i == 0: # Wide lines
                # Horizontal first line
                pygame.draw.line(screen,BLACK,(40,50),(670,50),3)
                # Vertical first line
                pygame.draw.line(screen,BLACK,(40,50),(40,680),3)

            elif i == 14: # Wide lines
                # Horizontal last line
                pygame.draw.line(screen,BLACK,(40,680),(670,680),2)
                # Vertical last line
                pygame.draw.line(screen,BLACK,(670,50),(670,680),2)

            else: 
                # Other horizontal lines
                pygame.draw.line(screen,BLACK,(40,50+45*i),(670,50+45*i),2)
                # Other vertical lines
                pygame.draw.line(screen,BLACK,(40+45*i,50),(40+45*i,680),2)
                
        # Draw the stars on the board (based on conventional board layout)
        pygame.draw.circle(screen,BLACK,(175,185),6)
        pygame.draw.circle(screen,BLACK,(175,545),6)
        pygame.draw.circle(screen,BLACK,(535,185),6)
        pygame.draw.circle(screen,BLACK,(535,545),6)
        pygame.draw.circle(screen,BLACK,(355,365),6)
        
    # Draw black pieces
    def ClickBlack():

        if len(BlackPiecesDisplayList) == len(WhitePiecesDisplayList):
            # which means this is black's turn
            
            XPositionBlack = int(round((pygame.mouse.get_pos()[0]-40)/45))
            YPositionBlack = int(round((pygame.mouse.get_pos()[1]-50)/45))
            # When user click the board, choose the nearest coordinate to the click positon.
            BlackPiecesPosition = [XPositionBlack,YPositionBlack]

            # Make sure this coordinate is empty.
            if BlackPiecesPosition not in TotalPiecesTestList:
                TotalPiecesTestList.append([XPositionBlack,YPositionBlack])
                BlackPiecesDisplayList.append([((XPositionBlack)*45)+40,((YPositionBlack)*45)+50])
                # transfer assumed coordinate back to actual coordinate.
                
                BlackPiecesWinList.append(([XPositionBlack,YPositionBlack]))

    # Draw white pieces               
    def ClickWhite():

        if len(WhitePiecesDisplayList) < len(BlackPiecesDisplayList):
            # which means this is white's turn
            
            XPositionWhite = int(round((pygame.mouse.get_pos()[0]-40)/45))
            YPositionWhite = int(round((pygame.mouse.get_pos()[1]-50)/45))
            WhitePiecesPosition = [XPositionWhite,YPositionWhite]
            
            if WhitePiecesPosition not in TotalPiecesTestList:
                TotalPiecesTestList.append([XPositionWhite,YPositionWhite])
                WhitePiecesDisplayList.append([((XPositionWhite)*45)+40,((YPositionWhite)*45)+50])
                WhitePiecesWinList.append(([XPositionWhite,YPositionWhite]))


    # Draw black pieces               
    def BlackPieces(screen):
        for i in range(len(BlackPiecesDisplayList)):
            # Draw all the black pieces in the List.
            x = BlackPiecesDisplayList[i][0]
            y = BlackPiecesDisplayList[i][1]
            pygame.draw.circle(screen,BLACK,(x,y),18,18) # Draw the circle
            

    # Draw white pieces
    def WhitePieces(screen):
        for i in range(len(WhitePiecesDisplayList)):
            # Draw all the white pieces in the List.
            x = WhitePiecesDisplayList[i][0]
            y = WhitePiecesDisplayList[i][1]
            pygame.draw.circle(screen,WHITE,(x,y),18,18)

    # Draw the Hint to display the other player's last move
    def Hint(screen):
        # 1. For black piece
        if len(BlackPiecesDisplayList) > len(WhitePiecesDisplayList):
            # The last move is black, so find the last element in the Black List.
            

            # Black starts first
            # 1. Left up
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]-22,BlackPiecesDisplayList[-1][1]-14),\
                             (BlackPiecesDisplayList[-1][0]-22,BlackPiecesDisplayList[-1][1]-20),2)
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]-20,BlackPiecesDisplayList[-1][1]-20),\
                             (BlackPiecesDisplayList[-1][0]-16,BlackPiecesDisplayList[-1][1]-20),2)

            # 2. Right up
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]+20,BlackPiecesDisplayList[-1][1]-14),\
                             (BlackPiecesDisplayList[-1][0]+20,BlackPiecesDisplayList[-1][1]-20),2)
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]+20,BlackPiecesDisplayList[-1][1]-20),\
                             (BlackPiecesDisplayList[-1][0]+14,BlackPiecesDisplayList[-1][1]-20),2)

            # 3. Left down
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]-22,BlackPiecesDisplayList[-1][1]+14),\
                             (BlackPiecesDisplayList[-1][0]-22,BlackPiecesDisplayList[-1][1]+20),2)
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]-22,BlackPiecesDisplayList[-1][1]+20),\
                             (BlackPiecesDisplayList[-1][0]-16,BlackPiecesDisplayList[-1][1]+20),2)

            # 4. Right Down
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]+20,BlackPiecesDisplayList[-1][1]+14),\
                             (BlackPiecesDisplayList[-1][0]+20,BlackPiecesDisplayList[-1][1]+20),2)
            pygame.draw.line(screen, RED, (BlackPiecesDisplayList[-1][0]+20,BlackPiecesDisplayList[-1][1]+20),\
                             (BlackPiecesDisplayList[-1][0]+14,BlackPiecesDisplayList[-1][1]+20),2)

        # 2. For white piece
        elif len(WhitePiecesDisplayList) == len(BlackPiecesDisplayList):
            # The last move was is white.
            if WhitePiecesDisplayList == []: # There is nothing on the board
                pass                
            else:
                # 1. Left up
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]-22,WhitePiecesDisplayList[-1][1]-14),\
                             (WhitePiecesDisplayList[-1][0]-22,WhitePiecesDisplayList[-1][1]-20),2)
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]-20,WhitePiecesDisplayList[-1][1]-20),\
                             (WhitePiecesDisplayList[-1][0]-16,WhitePiecesDisplayList[-1][1]-20),2)

                # 2. Right up
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]+20,WhitePiecesDisplayList[-1][1]-14),\
                             (WhitePiecesDisplayList[-1][0]+20,WhitePiecesDisplayList[-1][1]-20),2)
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]+20,WhitePiecesDisplayList[-1][1]-20),\
                             (WhitePiecesDisplayList[-1][0]+14,WhitePiecesDisplayList[-1][1]-20),2)

                # 3. Left down
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]-22,WhitePiecesDisplayList[-1][1]+14),\
                             (WhitePiecesDisplayList[-1][0]-22,WhitePiecesDisplayList[-1][1]+20),2)
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]-22,WhitePiecesDisplayList[-1][1]+20),\
                             (WhitePiecesDisplayList[-1][0]-16,WhitePiecesDisplayList[-1][1]+20),2)

                # 4. Right Down
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]+20,WhitePiecesDisplayList[-1][1]+14),\
                             (WhitePiecesDisplayList[-1][0]+20,WhitePiecesDisplayList[-1][1]+20),2)
                pygame.draw.line(screen, RED, (WhitePiecesDisplayList[-1][0]+20,WhitePiecesDisplayList[-1][1]+20),\
                             (WhitePiecesDisplayList[-1][0]+14,WhitePiecesDisplayList[-1][1]+20),2)
    # Draw the cursor
    def Cursor(screen):

        # Get the mouse's coordinate and display the nearest point on the boad.
        XPositionCursor = int(round((pygame.mouse.get_pos()[0]-40)/45))
        YPositionCursor = int(round((pygame.mouse.get_pos()[1]-50)/45))
        MousePosition = [(XPositionCursor*45)+40,(YPositionCursor*45)+50]
        # Tansfer assumed coordinate to actual coordinate.
        
        if (pygame.mouse.get_pos()[0] <= 680) and (pygame.mouse.get_pos()[0] >= 30)\
               and (pygame.mouse.get_pos()[1]<= 690) and (pygame.mouse.get_pos()[1] >=40 )\
               and WinBlack == 0 and WinWhite == 0: # Mouse in the board and game is not finished.

            # 1. For Black piece
            if len(BlackPiecesDisplayList) == len(WhitePiecesDisplayList):
                # Black turn

                # 1. Left up
                pygame.draw.line(screen, BLACK, (MousePosition[0]-22,MousePosition[1]-14),\
                                 (MousePosition[0]-22,MousePosition[1]-20),2)
                pygame.draw.line(screen, BLACK, (MousePosition[0]-20,MousePosition[1]-20),\
                                 (MousePosition[0]-16,MousePosition[1]-20),2)

                # 2. Right up
                pygame.draw.line(screen, BLACK, (MousePosition[0]+20,MousePosition[1]-14),\
                                 (MousePosition[0]+20,MousePosition[1]-20),2)
                pygame.draw.line(screen, BLACK, (MousePosition[0]+20,MousePosition[1]-20),\
                                 (MousePosition[0]+14,MousePosition[1]-20),2)

                # 3. Left down
                pygame.draw.line(screen, BLACK, (MousePosition[0]-22,MousePosition[1]+14),\
                                 (MousePosition[0]-22,MousePosition[1]+20),2)
                pygame.draw.line(screen, BLACK, (MousePosition[0]-22,MousePosition[1]+20),\
                                 (MousePosition[0]-16,MousePosition[1]+20),2)

                # 4. Right Down
                pygame.draw.line(screen, BLACK, (MousePosition[0]+20,MousePosition[1]+14),\
                                 (MousePosition[0]+20,MousePosition[1]+20),2)
                pygame.draw.line(screen, BLACK, (MousePosition[0]+20,MousePosition[1]+20),\
                                 (MousePosition[0]+14,MousePosition[1]+20),2)

            # 2. For White piece
            elif len(BlackPiecesDisplayList) > len(WhitePiecesDisplayList):
                # White turn

                # 1. Left up
                pygame.draw.line(screen, WHITE, (MousePosition[0]-22,MousePosition[1]-14),\
                                 (MousePosition[0]-22,MousePosition[1]-20),2)
                pygame.draw.line(screen, WHITE, (MousePosition[0]-20,MousePosition[1]-20),\
                                 (MousePosition[0]-16,MousePosition[1]-20),2)

                # 2. Right up
                pygame.draw.line(screen, WHITE, (MousePosition[0]+20,MousePosition[1]-14),\
                                 (MousePosition[0]+20,MousePosition[1]-20),2)
                pygame.draw.line(screen, WHITE, (MousePosition[0]+20,MousePosition[1]-20),\
                                 (MousePosition[0]+14,MousePosition[1]-20),2)

                # 3. Left down
                pygame.draw.line(screen, WHITE, (MousePosition[0]-22,MousePosition[1]+14),\
                                 (MousePosition[0]-22,MousePosition[1]+20),2)
                pygame.draw.line(screen, WHITE, (MousePosition[0]-22,MousePosition[1]+20),\
                                 (MousePosition[0]-16,MousePosition[1]+20),2)

                # 4. Right Down
                pygame.draw.line(screen, WHITE, (MousePosition[0]+20,MousePosition[1]+14),\
                                 (MousePosition[0]+20,MousePosition[1]+20),2)
                pygame.draw.line(screen, WHITE, (MousePosition[0]+20,MousePosition[1]+20),\
                                 (MousePosition[0]+14,MousePosition[1]+20),2)

                      


    # Draw the PlayerInformation              
    def PlayerInformation():
        # Set the font.
        ScoreBoardText = pygame.font.SysFont("Helvetica",30)
        RoundBoardText = pygame.font.SysFont("Helvetica",30)
        NameHintText = pygame.font.SysFont("Helvetica",40)

        
        # Change the player name's color to indicate which player goes first.
        if Round % 2 != 0:
            cp1 = 0 
            cp2 = 255
        else:
            cp1 = 255
            cp2 = 0

        global Name

        if PVP == 1:
            if Name == 0: # Names have not entered.
                
                Player1Name = input(str("Please enter player1's name"))
                Player2Name = input(str("Please enter player2's name"))
                PlayerNameList.insert(0,Player1Name)
                PlayerNameList.insert(1,Player2Name)
                
                Name = 1 # Names have entered.                  
            
            Player1 = ScoreBoardText.render(PlayerNameList[0] + ": " + str(Player1scoreList[0]),1,(cp1,cp1,cp1))
            Player2 = ScoreBoardText.render(PlayerNameList[1] + ": " + str(Player2scoreList[0]),1,(cp2,cp2,cp2))
            RoundBoard = RoundBoardText.render("Round: " + str(Round),1,(255,0,0))
            screen.blit(Player1, (130,20))
            screen.blit(Player2, (490,20))
            screen.blit(RoundBoard,(310,20))
            
        elif PVE == 1:
            if Name == 0: # Name have not entered.
                Player1Name = input(str("Please enter player1's name"))
                PlayerNameList.insert(0,Player1Name)

                Name = 1 # Name have entered.
                
            Player1 = ScoreBoardText.render(PlayerNameList[0] + ": " + str(Player1scoreList[0]),1,(cp1,cp1,cp1))
            Player2 = ScoreBoardText.render(PlayerNameList[1] + ": " + str(Player2scoreList[0]),1,(cp2,cp2,cp2))
            RoundBoard = RoundBoardText.render("Round: " + str(Round),1,(255,0,0))
            screen.blit(Player1, (130,20))
            screen.blit(Player2, (490,20))
            screen.blit(RoundBoard,(310,20))
            
            
        

    # Draw the Operators
    def Operators(screen):

        # Set the font
        OperatorsText = pygame.font.SysFont("Helvetica",60)
        RemindText = pygame.font.SysFont("Helvetica",33)
        
        global RemindReStart
        global RemindUndo
        global RemindQuit
        global RemindHelp

        # 1. ReStart      
        ReStart = OperatorsText.render("Restart",1,(0,0,0))
        screen.blit(ReStart,(765,120))
        
        pygame.draw.line(screen,BLACK,(760,115),(915,115),2)
        pygame.draw.line(screen,BLACK,(915,115),(915,160),2)
        pygame.draw.line(screen,BLACK,(915,160),(760,160),2)
        pygame.draw.line(screen,BLACK,(760,160),(760,115),2)
        

        if RemindReStart == 1: # Mouse is on the Restart
            
            RemindReStart1 = RemindText.render('Restart can be clicked' \
                                                 ,1,(255,0,0))
            RemindReStart2 = RemindText.render("when this round is finished.",1,(255,0,0))
            screen.blit(RemindReStart1,(720,170))
            screen.blit(RemindReStart2,(720,200))

            RemindReStart = 0 # Make the hint disappear

        # 2. Undo
        Undo = OperatorsText.render("Undo",1,(0,0,0))
        screen.blit(Undo,(786,255))

        pygame.draw.line(screen,BLACK,(760,250),(915,250),2)
        pygame.draw.line(screen,BLACK,(915,250),(915,295),2)
        pygame.draw.line(screen,BLACK,(915,295),(760,295),2)
        pygame.draw.line(screen,BLACK,(760,295),(760,250),2)

        if RemindUndo == 1: # Mouse is on the Undo
            RemindUndo1 = RemindText.render('Click Undo to retract',1,(255,0,0))
            RemindUndo2 = RemindText.render("your last piece.",1,(255,0,0))
            screen.blit(RemindUndo1,(720,305))
            screen.blit(RemindUndo2,(720,335))

            RemindUndo = 0 # Make the hint disappear
        

        # 4. Quit
        Quit = OperatorsText.render("Quit",1,(0,0,0))
        screen.blit(Quit,(792,400))

        pygame.draw.line(screen,BLACK,(760,395),(915,395),2)
        pygame.draw.line(screen,BLACK,(915,395),(915,440),2)
        pygame.draw.line(screen,BLACK,(915,440),(760,440),2)
        pygame.draw.line(screen,BLACK,(760,440),(760,395),2)

        if RemindQuit == 1: # Mouse is on the Quit
            RemindQuit1 = RemindText.render('Click Quit to go back',1,(255,0,0))
            RemindQuit2 = RemindText.render("to the mian Interface.",1,(255,0,0))
            screen.blit(RemindQuit1,(720,450))
            screen.blit(RemindQuit2,(720,480))

            RemindQuit = 0 # Make the hint disappear

        # 3. Help from AI

        Help = OperatorsText.render("Help",1,(0,0,0))
        screen.blit(Help,(792,545))

        pygame.draw.line(screen,BLACK,(760,540),(915,540),2)
        pygame.draw.line(screen,BLACK,(915,540),(915,585),2)
        pygame.draw.line(screen,BLACK,(915,585),(760,585),2)
        pygame.draw.line(screen,BLACK,(760,585),(760,540),2)
        
        if RemindHelp == 1: # Mouse is on the Help
            RemindHelp1 = RemindText.render('Click Help to get help',1,(255,0,0))
            RemindHelp2 = RemindText.render("from AI.",1,(255,0,0))
            screen.blit(RemindHelp1,(720,595))
            screen.blit(RemindHelp2,(720,625))

            RemindHelp = 0 # Make the hint disappear



    def Result(screen):
        
        # Set the font 
        ResultText = pygame.font.SysFont("Helvetica",60)
        
        if WinBlack == 1: # Black wins 
            Result = ResultText.render("Black Win !",1,(0,0,0))
            screen.blit(Result,(245,186))
        
        elif WinWhite == 1: # White wins
            Result = ResultText.render("White Win !",1,(255,255,255))
            screen.blit(Result,(245,186))
            
        elif TieGame == 1: # Tie game
            Result = ResultText.render("Tie Game !",1,(255,0,0))
            screen.blit(Result,(245,186))




# These two dictionary are used to give the value of each point on the board.
# To analyse the offence value of this point.
Offence = {"Connect 5" : 100000000,\

            "Connect 4" : 1000000,\
               
            "HalfConnect 4" : 10000,\

            "Connect 3" : 15000,\
               
            "HalfConnect 3" : 5000,\

            "Connect 2" :100}

# To analyse the Defence value of this point.
Defence = {"Connect 5" : 90000000,\

           "Connect 4" : 900000,\

           "HalfConnect 4" : 9000,\

           "Connect 3" : 13000,\

           "HalfConnect 3" : 4000,\

           "Connect 2" : 90}
# 1. The reason of the value of "connect (x)" is much more higher than "connect (x-1)" \
#    is if this point is satisfied with 8 times (maximum, and it's nearly impossible) \
#    of "connect (x-1)" and also satisfied with 1 time of "connect x" AI should \
#    place the piece on the "connect x" point.
# 2. The reason of the value of the same pattern of offence is higher than Defence
#    is if the pieces is placed and could lead to win, defend is unnecessary.

# Store all the values and coordinates of the empty points on the board.
ScoreDictionary = {}  # For example, {10000:[7,7]}

# The value of each point.
Score = 0




##########################################################
# This class includes evaluate all the points and find the most appropriate \ 
# point to set the piece.
class AI():
    
    def Evaluate():
        if Round % 2 !=0 : # AI plays white, user plays balck.
                BlackDictionary = Defence # Sine AI is white, so AI needs to defend black。
                WhiteDictionary = Offence # White attacks.
                # By using these two variables helps reduce a lot of repeated codes
                # So in different Rounds it could change to analyse offence value of diffence value.
                

        elif Round % 2 == 0: # AI plays black, user plays white.
                BlackDictionary = Offence # Black attacks
                WhiteDictionary = Defence # AI defends white.
                    
                        
        for x in range (15): # Go through and evaluate every point on the board.

            for y in range(15):
                
                global Score

                if ([x,y]) not in TotalPiecesTestList: # This point is empty
                
                    # 〇 means white piece
                    # ▢ means the white piece which is going to be placed
                    # - means empty position
                    # degree means 8 directions
                    

                    # 1. Connect 5 for AI (white)
                    # 1.1 ▢〇〇〇〇 
                    # 0°
                    if (([x+1, y]) in WhitePiecesWinList) and \
                       (([x+2, y]) in WhitePiecesWinList) and \
                       (([x+3, y]) in WhitePiecesWinList) and \
                       (([x+4, y]) in WhitePiecesWinList):                   
                        Score = Score + WhiteDictionary["Connect 5"]                      
                    
                    # 45°
                    if (([x+1, y-1]) in WhitePiecesWinList) and \
                       (([x+2, y-2]) in WhitePiecesWinList) and \
                       (([x+3, y-3]) in WhitePiecesWinList) and \
                       (([x+4, y-4]) in WhitePiecesWinList):                       
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 90°
                    if (([x, y-1]) in WhitePiecesWinList) and \
                       (([x, y-2]) in WhitePiecesWinList) and \
                       (([x, y-3]) in WhitePiecesWinList) and \
                       (([x, y-4]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 135°
                    if (([x-1, y-1]) in WhitePiecesWinList) and \
                       (([x-2, y-2]) in WhitePiecesWinList) and \
                       (([x-3, y-3]) in WhitePiecesWinList) and \
                       (([x-4, y-4]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 180°
                    if (([x-1, y]) in WhitePiecesWinList) and \
                       (([x-2, y]) in WhitePiecesWinList) and \
                       (([x-3, y]) in WhitePiecesWinList) and \
                       (([x-4, y]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 225°
                    if (([x-1, y+1]) in WhitePiecesWinList) and \
                       (([x-2, y+2]) in WhitePiecesWinList) and \
                       (([x-3, y+3]) in WhitePiecesWinList) and \
                       (([x-4, y+4]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                            
                            
                    # 270°
                    if (([x, y+1]) in WhitePiecesWinList) and \
                       (([x, y+2]) in WhitePiecesWinList) and \
                       (([x, y+3]) in WhitePiecesWinList) and \
                       (([x, y+4]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                        
                    # 315°
                    if (([x+1, y+1]) in WhitePiecesWinList) and \
                       (([x+2, y+2]) in WhitePiecesWinList) and \
                       (([x+3, y+3]) in WhitePiecesWinList) and \
                       (([x+4, y+4]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            

                    #1.2 〇▢〇〇〇
                    # 0°
                    if (([x-1, y]) in WhitePiecesWinList) and \
                       (([x+1, y]) in WhitePiecesWinList) and \
                       (([x+2, y]) in WhitePiecesWinList) and \
                       (([x+3, y]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 45°
                    if (([x-1, y+1]) in WhitePiecesWinList) and \
                       (([x+1, y-1]) in WhitePiecesWinList) and \
                       (([x+2, y-2]) in WhitePiecesWinList) and \
                       (([x+3, y-3]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                    # 90°
                    if (([x, y+1]) in WhitePiecesWinList) and \
                       (([x, y-1]) in WhitePiecesWinList) and \
                       (([x, y-2]) in WhitePiecesWinList) and \
                       (([x, y-3]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                                                                                                                                
                    # 135°
                    if (([x+1, y+1]) in WhitePiecesWinList) and \
                       (([x-1, y-1]) in WhitePiecesWinList) and \
                       (([x-2, y-2]) in WhitePiecesWinList) and \
                       (([x-3, y-3]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                        
                    # 180°
                    if (([x+1, y]) in WhitePiecesWinList) and \
                       (([x-1, y]) in WhitePiecesWinList) and \
                       (([x-2, y]) in WhitePiecesWinList) and \
                       (([x-3, y]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 225°
                    if (([x+1, y-1]) in WhitePiecesWinList) and \
                       (([x-1, y+1]) in WhitePiecesWinList) and \
                       (([x-2, y+2]) in WhitePiecesWinList) and \
                       (([x-3, y+3]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 270°
                    if (([x, y-1]) in WhitePiecesWinList) and \
                       (([x, y+1]) in WhitePiecesWinList) and \
                       (([x, y+2]) in WhitePiecesWinList) and \
                       (([x, y+3]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 315°
                    if (([x-1, y-1]) in WhitePiecesWinList) and \
                       (([x+1, y+1]) in WhitePiecesWinList) and \
                       (([x+2, y+2]) in WhitePiecesWinList) and \
                       (([x+3, y+3]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            

                    # 1.3 〇〇▢〇〇
                    # 0°
                    if (([x-1, y]) in WhitePiecesWinList) and \
                       (([x-2, y]) in WhitePiecesWinList) and \
                       (([x+1, y]) in WhitePiecesWinList) and \
                       (([x+2, y]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 45°
                    if (([x-1, y+1]) in WhitePiecesWinList) and \
                       (([x-2, y+2]) in WhitePiecesWinList) and \
                       (([x+1, y-1]) in WhitePiecesWinList) and \
                       (([x+2, y-2]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 90°
                    if (([x, y+1]) in WhitePiecesWinList) and \
                       (([x, y+2]) in WhitePiecesWinList) and \
                       (([x, y-1]) in WhitePiecesWinList) and \
                       (([x, y-2]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    
                    # 135°
                    if (([x+1, y+1]) in WhitePiecesWinList) and \
                       (([x+2, y+2]) in WhitePiecesWinList) and \
                       (([x-1, y-1]) in WhitePiecesWinList) and \
                       (([x-2, y-2]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 180°
                    if (([x+1, y]) in WhitePiecesWinList) and \
                       (([x+2, y]) in WhitePiecesWinList) and \
                       (([x-1, y]) in WhitePiecesWinList) and \
                       (([x-2, y]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 225°
                    if (([x+1, y-1]) in WhitePiecesWinList) and \
                       (([x+2, y-2]) in WhitePiecesWinList) and \
                       (([x-1, y+1]) in WhitePiecesWinList) and \
                       (([x-2, y+2]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 270°
                    if (([x, y-1]) in WhitePiecesWinList) and \
                       (([x, y-2]) in WhitePiecesWinList) and \
                       (([x, y+1]) in WhitePiecesWinList) and \
                       (([x, y+2]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            
                    # 315°
                    if (([x-1, y-1]) in WhitePiecesWinList) and \
                       (([x-2, y-2]) in WhitePiecesWinList) and \
                       (([x+1, y+1]) in WhitePiecesWinList) and \
                       (([x+2, y+2]) in WhitePiecesWinList):
                        Score = Score + WhiteDictionary["Connect 5"]
                        
                            

                    
                    # 2. Connect 4
                    # 2.1 -▢〇〇〇-
                    # 0°
                    if (([x+1,y]) in WhitePiecesWinList) and \
                       (([x+2,y]) in WhitePiecesWinList) and \
                       (([x+3,y]) in WhitePiecesWinList):
                        
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                        
                        if ([x+4,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                        # By doing this, for example, if this point's left side point and right\
                        # next 4 potin are empty, the Score of this point will be added 4 times,\
                        # which means it will be picked (if it is highest).
                        # This is also the reason of using "if" rather than "elif"
                        # The aim is by going through all the situation to find the most appropriate point.
                                       

                         
                    # 45°
                    if (([x+1,y-1]) in WhitePiecesWinList) and \
                       (([x+2,y-2]) in WhitePiecesWinList) and \
                       (([x+3,y-3]) in WhitePiecesWinList):

                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                        
                        if ([x+4,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                
                    
                    # 90°
                    if (([x,y-1]) in WhitePiecesWinList) and \
                       (([x,y-2]) in WhitePiecesWinList) and \
                       (([x,y-3]) in WhitePiecesWinList):
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                        if ([x,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                
                            
                                                                         
                    # 135°
                    if (([x-1,y-1]) in WhitePiecesWinList) and \
                       (([x-2,y-2]) in WhitePiecesWinList) and \
                       (([x-3,y-3]) in WhitePiecesWinList):
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                        if ([x-4,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                

                    # 180°
                    if (([x-1,y]) in WhitePiecesWinList) and \
                       (([x-2,y]) in WhitePiecesWinList) and \
                       (([x-3,y]) in WhitePiecesWinList):
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                        if ([x-4,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                
                            
                    # 225°
                    if (([x-1,y+1]) in WhitePiecesWinList) and \
                       (([x-2,y+2]) in WhitePiecesWinList) and \
                       (([x-3,y+3]) in WhitePiecesWinList):
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                        if ([x-4,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                
                            
                    # 270°
                    if (([x,y+1]) in WhitePiecesWinList) and \
                       (([x,y+2]) in WhitePiecesWinList) and \
                       (([x,y+3]) in WhitePiecesWinList):
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                        if ([x,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                
                    # 315°
                    if (([x+1,y+1]) in WhitePiecesWinList) and \
                       (([x+2,y+2]) in WhitePiecesWinList) and \
                       (([x+3,y+3]) in WhitePiecesWinList):
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                        if ([x+4,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + 10 + WhiteDictionary["Connect 4"]
                                
                            
                    
                    # 2.2 -〇▢〇〇-
                    # 0°
                    if (([x-1,y]) in WhitePiecesWinList) and \
                       (([x+1,y]) in WhitePiecesWinList) and \
                       (([x+2,y]) in WhitePiecesWinList):
                        if ([x-2,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x+3,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                         
                    # 45°
                    if (([x-1,y+1]) in WhitePiecesWinList) and \
                       (([x+1,y-1]) in WhitePiecesWinList) and \
                       (([x+2,y-2]) in WhitePiecesWinList):
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                                
                    # 90°
                    if (([x,y-1]) in WhitePiecesWinList) and \
                       (([x,y-1]) in WhitePiecesWinList) and \
                       (([x,y-2]) in WhitePiecesWinList):
                        if ([x,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                                
                    # 135°
                    if (([x+1,y+1]) in WhitePiecesWinList) and \
                       (([x-1,y-1]) in WhitePiecesWinList) and \
                       (([x-2,y-2]) in WhitePiecesWinList):
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                                
                    # 180°
                    if (([x+1,y]) in WhitePiecesWinList) and \
                       (([x-1,y]) in WhitePiecesWinList) and \
                       (([x-2,y]) in WhitePiecesWinList):
                        if ([x+2,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x-3,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                                
                    # 225°
                    if (([x+1,y-1]) in WhitePiecesWinList) and \
                       (([x-1,y+1]) in WhitePiecesWinList) and \
                       (([x-2,y+2]) in WhitePiecesWinList):
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                                
                    # 270°
                    if (([x,y-1]) in WhitePiecesWinList) and \
                       (([x,y+1]) in WhitePiecesWinList) and \
                       (([x,y+2]) in WhitePiecesWinList):
                        if ([x,y-2])  not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x,y-2])  not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                                
                    # 315°
                    if (([x-1,y-1]) in WhitePiecesWinList) and \
                       (([x+1,y+1]) in WhitePiecesWinList) and \
                       (([x+2,y+2]) in WhitePiecesWinList):
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["Connect 4"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 4"]

                    ## 2.3 -▢-〇〇〇
                    # 0°
                    if ([x+2,y]) in WhitePiecesWinList and \
                       ([x+3,y]) in WhitePiecesWinList and \
                       ([x+4,y]) in WhitePiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                
                    # 45°
                    if ([x+2,y-2]) in WhitePiecesWinList and \
                       ([x+3,y-3]) in WhitePiecesWinList and \
                       ([x+4,y-4]) in WhitePiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                
                    # 90°
                    if ([x,y-2]) in WhitePiecesWinList and \
                       ([x,y-3]) in WhitePiecesWinList and \
                       ([x,y-4]) in WhitePiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                            

                    # 135°
                    if ([x-2,y-2]) in WhitePiecesWinList and \
                       ([x-3,y-3]) in WhitePiecesWinList and \
                       ([x-4,y-4]) in WhitePiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 180°
                    if ([x-2,y]) in WhitePiecesWinList and \
                       ([x-3,y]) in WhitePiecesWinList and \
                       ([x-4,y]) in WhitePiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 225°
                    if ([x-2,y+2]) in WhitePiecesWinList and \
                       ([x-3,y+3]) in WhitePiecesWinList and \
                       ([x-4,y+4]) in WhitePiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
             
                    # 270°
                    if ([x,y+2]) in WhitePiecesWinList and \
                       ([x,y+3]) in WhitePiecesWinList and \
                       ([x,y+4]) in WhitePiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                         
                    # 315°
                    if ([x+2,y+2]) in WhitePiecesWinList and \
                       ([x+3,y+3]) in WhitePiecesWinList and \
                       ([x+4,y+4]) in WhitePiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
  

                            
                    ## 2.4 -▢〇-〇〇 
                    # 0°
                    if ([x+1,y]) in WhitePiecesWinList and \
                       ([x+3,y]) in WhitePiecesWinList and \
                       ([x+4,y]) in WhitePiecesWinList:
                        if ([x+2,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 45°
                    if ([x+1,y-1]) in WhitePiecesWinList and \
                       ([x+3,y-3]) in WhitePiecesWinList and \
                       ([x+4,y-4]) in WhitePiecesWinList:
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-1]) in WhitePiecesWinList and \
                       ([x,y-3]) in WhitePiecesWinList and \
                       ([x,y-4]) in WhitePiecesWinList:
                        if ([x,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-1,y-1]) in WhitePiecesWinList and \
                       ([x-3,y-3]) in WhitePiecesWinList and \
                       ([x-4,y-4]) in WhitePiecesWinList:
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-1,y]) in WhitePiecesWinList and \
                       ([x-3,y]) in WhitePiecesWinList and \
                       ([x-4,y]) in WhitePiecesWinList:
                        if ([x-2,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-1,y+1]) in WhitePiecesWinList and \
                       ([x-3,y+3]) in WhitePiecesWinList and \
                       ([x-4,y+4]) in WhitePiecesWinList:
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+1]) in WhitePiecesWinList and \
                       ([x,y+3]) in WhitePiecesWinList and \
                       ([x,y+4]) in WhitePiecesWinList:
                        if ([x,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+1,y+1]) in WhitePiecesWinList and \
                       ([x+3,y+3]) in WhitePiecesWinList and \
                       ([x+4,y+4]) in WhitePiecesWinList:
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                
                    ## 2.5-▢〇〇-〇  
                    # 0°
                    if ([x+1,y]) in WhitePiecesWinList and \
                       ([x+2,y]) in WhitePiecesWinList and \
                       ([x+4,y]) in WhitePiecesWinList:
                        if ([x+3,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 45°
                    if ([x+1,y-1]) in WhitePiecesWinList and \
                       ([x+2,y-2]) in WhitePiecesWinList and \
                       ([x+4,y-4]) in WhitePiecesWinList:
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-1]) in WhitePiecesWinList and \
                       ([x,y-2]) in WhitePiecesWinList and \
                       ([x,y-4]) in WhitePiecesWinList:
                        if ([x,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-1,y-1]) in WhitePiecesWinList and \
                       ([x-2,y-2]) in WhitePiecesWinList and \
                       ([x-4,y-4]) in WhitePiecesWinList:
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-1,y]) in WhitePiecesWinList and \
                       ([x-2,y]) in WhitePiecesWinList and \
                       ([x-4,y]) in WhitePiecesWinList:
                        if ([x-3,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-1,y+1]) in WhitePiecesWinList and \
                       ([x-2,y+2]) in WhitePiecesWinList and \
                       ([x-4,y+4]) in WhitePiecesWinList:
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+1]) in WhitePiecesWinList and \
                       ([x,y+2]) in WhitePiecesWinList and \
                       ([x,y+4]) in WhitePiecesWinList:
                        if ([x,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+1,y+1]) in WhitePiecesWinList and \
                       ([x+2,y+2]) in WhitePiecesWinList and \
                       ([x+4,y+4]) in WhitePiecesWinList:
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                
                    ## 2.6 -▢〇-〇-〇-
                    # 0°
                    if ([x+1,y]) in WhitePiecesWinList and \
                       ([x+3,y]) in WhitePiecesWinList and \
                       ([x+5,y]) in WhitePiecesWinList:
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x-1,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]                               
                    # 45°
                    if ([x+1,y-1]) in WhitePiecesWinList and \
                       ([x+3,y-3]) in WhitePiecesWinList and \
                       ([x+5,y-5]) in WhitePiecesWinList:
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x-1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-1]) in WhitePiecesWinList and \
                       ([x,y-3]) in WhitePiecesWinList and \
                       ([x,y-5]) in WhitePiecesWinList:
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x,y+1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-1,y-1]) in WhitePiecesWinList and \
                       ([x-3,y-3]) in WhitePiecesWinList and \
                       ([x-5,y-5]) in WhitePiecesWinList:
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x+1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-1,y]) in WhitePiecesWinList and \
                       ([x-3,y]) in WhitePiecesWinList and \
                       ([x-5,y]) in WhitePiecesWinList:
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x+1,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-1,y+1]) in WhitePiecesWinList and \
                       ([x-3,y+3]) in WhitePiecesWinList and \
                       ([x-5,y+5]) in WhitePiecesWinList:
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x+1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+1]) in WhitePiecesWinList and \
                       ([x,y+3]) in WhitePiecesWinList and \
                       ([x,y+5]) in WhitePiecesWinList:
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x,y-1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+1,y+1]) in WhitePiecesWinList and \
                       ([x+3,y+3]) in WhitePiecesWinList and \
                       ([x+5,y+5]) in WhitePiecesWinList:
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                if ([x-1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["HalfConnect 4"]
                    
                    
                    
                    ## 2.7 -〇〇▢-〇
                    # 0°
                    if ([x+2,y]) in WhitePiecesWinList and \
                       ([x-1,y]) in WhitePiecesWinList and \
                       ([x-2,y]) in WhitePiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 45°
                    if ([x+2,y-2]) in WhitePiecesWinList and \
                       ([x-1,y+1]) in WhitePiecesWinList and \
                       ([x-2,y+2]) in WhitePiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-2]) in WhitePiecesWinList and \
                       ([x,y+1]) in WhitePiecesWinList and \
                       ([x,y+2]) in WhitePiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-2,y-2]) in WhitePiecesWinList and \
                       ([x+1,y+1]) in WhitePiecesWinList and \
                       ([x+2,y+2]) in WhitePiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-2,y]) in WhitePiecesWinList and \
                       ([x+1,y]) in WhitePiecesWinList and \
                       ([x+2,y]) in WhitePiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-2,y+2]) in WhitePiecesWinList and \
                       ([x+1,y-1]) in WhitePiecesWinList and \
                       ([x+2,y-2]) in WhitePiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+2]) in WhitePiecesWinList and \
                       ([x,y-1]) in WhitePiecesWinList and \
                       ([x,y-2]) in WhitePiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+2,y+2]) in WhitePiecesWinList and \
                       ([x-1,y-1]) in WhitePiecesWinList and \
                       ([x-2,y-2]) in WhitePiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    
                    ## 2.8 -〇〇-▢〇-
                    # 0°
                    if ([x+1,y]) in WhitePiecesWinList and \
                       ([x-2,y]) in WhitePiecesWinList and \
                       ([x-3,y]) in WhitePiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                               
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                                         
                    # 45°
                    if ([x+1,y-1]) in WhitePiecesWinList and \
                       ([x-2,y+2]) in WhitePiecesWinList and \
                       ([x-3,y+3]) in WhitePiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                               
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                
                    # 90°
                    if ([x,y-1]) in WhitePiecesWinList and \
                       ([x,y+2]) in WhitePiecesWinList and \
                       ([x,y+3]) in WhitePiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                               
                    # 135°
                    if ([x-1,y-1]) in WhitePiecesWinList and \
                       ([x+2,y+2]) in WhitePiecesWinList and \
                       ([x+3,y+3]) in WhitePiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                               
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]

                    # 180°
                    if ([x-1,y]) in WhitePiecesWinList and \
                       ([x+2,y]) in WhitePiecesWinList and \
                       ([x+3,y]) in WhitePiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                               
                    # 225°
                    if ([x-1,y+1]) in WhitePiecesWinList and \
                       ([x+2,y-2]) in WhitePiecesWinList and \
                       ([x+3,y-3]) in WhitePiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                               
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+1]) in WhitePiecesWinList and \
                       ([x,y-2]) in WhitePiecesWinList and \
                       ([x,y-3]) in WhitePiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                              
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]

                    # 315°
                    if ([x+1,y+1]) in WhitePiecesWinList and \
                       ([x-2,y-2]) in WhitePiecesWinList and \
                       ([x-3,y-3]) in WhitePiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 4"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]

                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 4"]
                                

                                

                    # 3. Connect 3
                    # 3.1 -▢〇〇-
                    # 0°
                    if (([x+1,y]) in WhitePiecesWinList) and \
                       (([x+2,y]) in WhitePiecesWinList):
                        if ([x-1,y]) not in TotalPiecesTestList:
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x+3,y]) not in TotalPiecesTestList:
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                         
                    # 45°
                    if (([x+1,y-1]) in WhitePiecesWinList) and \
                       (([x+2,y-2]) in WhitePiecesWinList):
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 90°
                    if (([x,y-1]) in WhitePiecesWinList) and \
                       (([x,y-2]) in WhitePiecesWinList):
                        if ([x,y+1]) not in TotalPiecesTestList:
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x,y-3]) not in TotalPiecesTestList:
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                                        
                    # 135°
                    if (([x-1,y-1]) in WhitePiecesWinList) and \
                       (([x-2,y-2]) in WhitePiecesWinList):
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 180°
                    if (([x-1,y]) in WhitePiecesWinList) and \
                       (([x-2,y]) in WhitePiecesWinList):
                        if ([x+1,y]) not in TotalPiecesTestList:
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x-3,y]) not in TotalPiecesTestList:
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 225°
                    if (([x-1,y+1]) in WhitePiecesWinList) and \
                       (([x-2,y+2]) in WhitePiecesWinList):
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 270°
                    if (([x,y+1]) in WhitePiecesWinList) and \
                       (([x,y+2]) in WhitePiecesWinList):
                        if ([x,y-1]) not in TotalPiecesTestList:
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x,y+3]) not in TotalPiecesTestList:
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 315°
                    if (([x+1,y+1]) in WhitePiecesWinList) and \
                       (([x+2,y+2]) in WhitePiecesWinList):
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    

                    
                    # 3.2 -〇▢〇-
                    # 0°
                    if (([x+1,y]) in WhitePiecesWinList) and \
                       (([x-1,y]) in WhitePiecesWinList):
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
            
                    # 45°
                    if (([x+1,y-1]) in WhitePiecesWinList) and \
                       (([x-1,y+1]) in WhitePiecesWinList):
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    
                    # 90°
                    if (([x,y-1]) in WhitePiecesWinList) and \
                       (([x,y+1]) in WhitePiecesWinList):
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 135°
                    if (([x-1,y-1]) in WhitePiecesWinList) and \
                       (([x+1,y+1]) in WhitePiecesWinList):
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    
                    # 180°
                    if (([x-1,y]) in WhitePiecesWinList) and \
                       (([x+1,y]) in WhitePiecesWinList):
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 225°
                    if (([x-1,y+1]) in WhitePiecesWinList) and \
                       (([x+1,y-1]) in WhitePiecesWinList):
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    
                    # 270°
                    if (([x,y+1]) in WhitePiecesWinList) and \
                       (([x,y-1]) in WhitePiecesWinList):
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                    # 315°
                    if (([x+1,y+1]) in WhitePiecesWinList) and \
                       (([x-1,y-1]) in WhitePiecesWinList):
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["Connect 3"]
                                
                    ## 3.3 -▢〇-〇-
                    # 0°
                    if ([x+1,y]) in WhitePiecesWinList and \
                       ([x+3,y]) in WhitePiecesWinList and \
                       ([x+2,y]) not in TotalPiecesTestList:
                        if ([x+4,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 45°
                    if ([x+1,y-1]) in WhitePiecesWinList and \
                       ([x+3,y-3]) in WhitePiecesWinList and \
                       ([x+2,y-2]) not in TotalPiecesTestList:
                        if ([x+4,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 90°
                    if ([x,y-1]) in WhitePiecesWinList and \
                       ([x,y-3]) in WhitePiecesWinList and \
                       ([x,y-2]) not in TotalPiecesTestList:
                        if ([x,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 135°
                    if ([x-1,y-1]) in WhitePiecesWinList and \
                       ([x-3,y-3]) in WhitePiecesWinList and \
                       ([x-2,y-2]) not in TotalPiecesTestList:
                        if ([x-4,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 180°
                    if ([x-1,y]) in WhitePiecesWinList and \
                       ([x-3,y]) in WhitePiecesWinList and \
                       ([x-2,y]) not in TotalPiecesTestList:
                        if ([x-4,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 225°
                    if ([x-1,y+1]) in WhitePiecesWinList and \
                       ([x-3,y+3]) in WhitePiecesWinList and \
                       ([x-2,y+2]) not in TotalPiecesTestList:
                        if ([x-4,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 270°
                    if ([x,y+1]) in WhitePiecesWinList and \
                       ([x,y+3]) in WhitePiecesWinList and \
                       ([x,y+2]) not in TotalPiecesTestList:
                        if ([x,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 315°
                    if ([x+1,y+1]) in WhitePiecesWinList and \
                       ([x+3,y+3]) in WhitePiecesWinList and \
                       ([x+2,y+2]) not in TotalPiecesTestList:
                        if ([x+4,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    
            
                    ## 3.4 -〇▢-〇-
                    # 0°
                    if ([x+2,y]) in WhitePiecesWinList and \
                       ([x-1,y]) in WhitePiecesWinList and \
                       ([x+1,y]) not in TotalPiecesTestList:
                        if ([x+3,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-2,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]                           
                    # 45°
                    if ([x+2,y-2]) in WhitePiecesWinList and \
                       ([x-1,y+1]) in WhitePiecesWinList and \
                       ([x+1,y-1]) not in TotalPiecesTestList:
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 90°
                    if ([x,y-2]) in WhitePiecesWinList and \
                       ([x,y+1]) in WhitePiecesWinList and \
                       ([x,y-1]) not in TotalPiecesTestList:
                        if ([x,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 135°
                    if ([x-2,y-2]) in WhitePiecesWinList and \
                       ([x+1,y+1]) in WhitePiecesWinList and \
                       ([x-1,y-1]) not in TotalPiecesTestList:
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 180°
                    if ([x-2,y]) in WhitePiecesWinList and \
                       ([x+1,y]) in WhitePiecesWinList and \
                       ([x-1,y]) not in TotalPiecesTestList:
                        if ([x-3,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+2,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 225°
                    if ([x-2,y+2]) in WhitePiecesWinList and \
                       ([x+1,y-1]) in WhitePiecesWinList and \
                       ([x-1,y+1]) not in TotalPiecesTestList:
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]

                    # 270°
                    if ([x,y+2]) in WhitePiecesWinList and \
                       ([x,y-1]) in WhitePiecesWinList and \
                       ([x,y+1]) not in TotalPiecesTestList:
                        if ([x,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 315°
                    if ([x+2,y+2]) in WhitePiecesWinList and \
                       ([x-1,y-1]) in WhitePiecesWinList and \
                       ([x+1,y+1]) not in TotalPiecesTestList:
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                                
                    ## 3.5 -▢-〇〇-
                    # 0°
                    if ([x+2,y]) in WhitePiecesWinList and \
                       ([x+3,y]) in WhitePiecesWinList and \
                       ([x+1,y]) in WhitePiecesWinList:
                        if ([x+4,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 45°
                    if ([x+2,y-2]) in WhitePiecesWinList and \
                       ([x+3,y-3]) in WhitePiecesWinList and \
                       ([x+1,y-1]) in WhitePiecesWinList:
                        if ([x+4,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 90°
                    if ([x,y-2]) in WhitePiecesWinList and \
                       ([x,y-3]) in WhitePiecesWinList and \
                       ([x,y-1]) in WhitePiecesWinList:
                        if ([x,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 135°
                    if ([x-2,y-2]) in WhitePiecesWinList and \
                       ([x-3,y-3]) in WhitePiecesWinList and \
                       ([x-1,y-1]) in WhitePiecesWinList:
                        if ([x-4,y-4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 180°
                    if ([x-2,y]) in WhitePiecesWinList and \
                       ([x-3,y]) in WhitePiecesWinList and \
                       ([x-1,y]) in WhitePiecesWinList:
                        if ([x-4,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 225°
                    if ([x-2,y+2]) in WhitePiecesWinList and \
                       ([x-3,y+3]) in WhitePiecesWinList and \
                       ([x-1,y+1]) in WhitePiecesWinList:
                        if ([x-4,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 270°
                    if ([x,y+2]) in WhitePiecesWinList and \
                       ([x,y+3]) in WhitePiecesWinList and \
                       ([x,y+1]) in WhitePiecesWinList:
                        if ([x,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                    # 315°
                    if ([x+2,y+2]) in WhitePiecesWinList and \
                       ([x+3,y+3]) in WhitePiecesWinList and \
                       ([x+1,y+1]) in WhitePiecesWinList:
                        if ([x+4,y+4]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + WhiteDictionary["HalfConnect 3"]
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + WhiteDictionary["HalfConnect 3"]
          
                               
                    # 4. Connect 2
                    # 4.1 ▢〇
                    # 0°
                    if ([x+1,y]) in WhitePiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            if ([x-2,y]) not in TotalPiecesTestList:
                                if ([x-3,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+2,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                if ([x-2,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+3,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x-1,y]) not in TotalPiecesTestList:
                                if ([x-2,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+3,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                if ([x-1,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+4,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]                                               
                    # 45°
                    if ([x+1,y-1]) in WhitePiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                if ([x-3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                if ([x-2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                if ([x-2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                if ([x-1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+4,y-4]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                    # 90°
                    if ([x,y-1]) in WhitePiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            if ([x,y+2]) not in TotalPiecesTestList:
                                if ([x,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                if ([x,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y+1]) not in TotalPiecesTestList:
                                if ([x,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                if ([x,y+1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y-4]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                    # 135°
                    if ([x-1,y-1]) in WhitePiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                if ([x+3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                if ([x+2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                if ([x+2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                if ([x+1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-4,y-4]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                    # 180°
                    if ([x-1,y]) in WhitePiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            if ([x+2,y]) not in TotalPiecesTestList:
                                if ([x+3,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-2,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                if ([x+2,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-3,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x+1,y]) not in TotalPiecesTestList:
                                if ([x+2,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-3,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                if ([x+1,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-4,y]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                    # 225°
                    if ([x-1,y+1]) in WhitePiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                if ([x+3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                if ([x+2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                if ([x+2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                if ([x+1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x-4,y+4]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                    # 270°
                    if ([x,y+1]) in WhitePiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            if ([x,y-2]) not in TotalPiecesTestList:
                                if ([x,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                if ([x,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y-1]) not in TotalPiecesTestList:
                                if ([x,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                if ([x,y-1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x,y+4]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                    # 315°
                    if ([x+1,y+1]) in WhitePiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                if ([x-3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                if ([x-2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                if ([x-2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                if ([x-1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]
                                if ([x+4,y+4]) not in TotalPiecesTestList:
                                    Score = Score + WhiteDictionary["Connect 2"]


                                                    
                    #####################################################################################################################
                    # 〇 means black piece
                    # ▢ means the black piece which is going to be placed
                    # - means empty position
                    # degree means 8 directions

                    
                    # 1. Connect 5 for User (black)
                    # 1.1 ▢〇〇〇〇 
                    # 0°
                    if (([x+1, y]) in BlackPiecesWinList) and \
                       (([x+2, y]) in BlackPiecesWinList) and \
                       (([x+3, y]) in BlackPiecesWinList) and \
                       (([x+4, y]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                    
                    # 45°
                    if (([x+1, y-1]) in BlackPiecesWinList) and \
                       (([x+2, y-2]) in BlackPiecesWinList) and \
                       (([x+3, y-3]) in BlackPiecesWinList) and \
                       (([x+4, y-4]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 90°
                    if (([x, y-1]) in BlackPiecesWinList) and \
                       (([x, y-2]) in BlackPiecesWinList) and \
                       (([x, y-3]) in BlackPiecesWinList) and \
                       (([x, y-4]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 135°
                    if (([x-1, y-1]) in BlackPiecesWinList) and \
                       (([x-2, y-2]) in BlackPiecesWinList) and \
                       (([x-3, y-3]) in BlackPiecesWinList) and \
                       (([x-4, y-4]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 180°
                    if (([x-1, y]) in BlackPiecesWinList) and \
                       (([x-2, y]) in BlackPiecesWinList) and \
                       (([x-3, y]) in BlackPiecesWinList) and \
                       (([x-4, y]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 225°
                    if (([x-1, y+1]) in BlackPiecesWinList) and \
                       (([x-2, y+2]) in BlackPiecesWinList) and \
                       (([x-3, y+3]) in BlackPiecesWinList) and \
                       (([x-4, y+4]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 270°
                    if (([x, y+1]) in BlackPiecesWinList) and \
                       (([x, y+2]) in BlackPiecesWinList) and \
                       (([x, y+3]) in BlackPiecesWinList) and \
                       (([x, y+4]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 315°
                    if (([x+1, y+1]) in BlackPiecesWinList) and \
                       (([x+2, y+2]) in BlackPiecesWinList) and \
                       (([x+3, y+3]) in BlackPiecesWinList) and \
                       (([x+4, y+4]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            

                    #1.2 〇▢〇〇〇
                    # 0°
                    if (([x-1, y]) in BlackPiecesWinList) and \
                       (([x+1, y]) in BlackPiecesWinList) and \
                       (([x+2, y]) in BlackPiecesWinList) and \
                       (([x+3, y]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 45°
                    if (([x-1, y+1]) in BlackPiecesWinList) and \
                       (([x+1, y-1]) in BlackPiecesWinList) and \
                       (([x+2, y-2]) in BlackPiecesWinList) and \
                       (([x+3, y-3]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                    # 90°
                    if (([x, y+1]) in BlackPiecesWinList) and \
                       (([x, y-1]) in BlackPiecesWinList) and \
                       (([x, y-2]) in BlackPiecesWinList) and \
                       (([x, y-3]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                                                                                                                                
                    # 135°
                    if (([x+1, y+1]) in BlackPiecesWinList) and \
                       (([x-1, y-1]) in BlackPiecesWinList) and \
                       (([x-2, y-2]) in BlackPiecesWinList) and \
                       (([x-3, y-3]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 180°
                    if (([x+1, y]) in BlackPiecesWinList) and \
                       (([x-1, y]) in BlackPiecesWinList) and \
                       (([x-2, y]) in BlackPiecesWinList) and \
                       (([x-3, y]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 225°
                    if (([x+1, y-1]) in BlackPiecesWinList) and \
                       (([x-1, y+1]) in BlackPiecesWinList) and \
                       (([x-2, y+2]) in BlackPiecesWinList) and \
                       (([x-3, y+3]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 270°
                    if (([x, y-1]) in BlackPiecesWinList) and \
                       (([x, y+1]) in BlackPiecesWinList) and \
                       (([x, y+2]) in BlackPiecesWinList) and \
                       (([x, y+3]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 315°
                    if (([x-1, y-1]) in BlackPiecesWinList) and \
                       (([x+1, y+1]) in BlackPiecesWinList) and \
                       (([x+2, y+2]) in BlackPiecesWinList) and \
                       (([x+3, y+3]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            

                    # 1.3 〇〇▢〇〇
                    # 0°
                    if (([x-1, y]) in BlackPiecesWinList) and \
                       (([x-2, y]) in BlackPiecesWinList) and \
                       (([x+1, y]) in BlackPiecesWinList) and \
                       (([x+2, y]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 45°
                    if (([x-1, y+1]) in BlackPiecesWinList) and \
                       (([x-2, y+2]) in BlackPiecesWinList) and \
                       (([x+1, y-1]) in BlackPiecesWinList) and \
                       (([x+2, y-2]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 90°
                    if (([x, y+1]) in BlackPiecesWinList) and \
                       (([x, y+2]) in BlackPiecesWinList) and \
                       (([x, y-1]) in BlackPiecesWinList) and \
                       (([x, y-2]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    
                    # 135°
                    if (([x+1, y+1]) in BlackPiecesWinList) and \
                       (([x+2, y+2]) in BlackPiecesWinList) and \
                       (([x-1, y-1]) in BlackPiecesWinList) and \
                       (([x-2, y-2]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 180°
                    if (([x+1, y]) in BlackPiecesWinList) and \
                       (([x+2, y]) in BlackPiecesWinList) and \
                       (([x-1, y]) in BlackPiecesWinList) and \
                       (([x-2, y]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 225°
                    if (([x+1, y-1]) in BlackPiecesWinList) and \
                       (([x+2, y-2]) in BlackPiecesWinList) and \
                       (([x-1, y+1]) in BlackPiecesWinList) and \
                       (([x-2, y+2]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 270°
                    if (([x, y-1]) in BlackPiecesWinList) and \
                       (([x, y-2]) in BlackPiecesWinList) and \
                       (([x, y+1]) in BlackPiecesWinList) and \
                       (([x, y+2]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            
                    # 315°
                    if (([x-1, y-1]) in BlackPiecesWinList) and \
                       (([x-2, y-2]) in BlackPiecesWinList) and \
                       (([x+1, y+1]) in BlackPiecesWinList) and \
                       (([x+2, y+2]) in BlackPiecesWinList):
                        Score = Score + BlackDictionary["Connect 5"]
                        
                            

                    
                    # 2. Connect 4
                    # 2.1 -▢〇〇〇-
                    # 0°
                    if (([x+1,y]) in BlackPiecesWinList) and \
                       (([x+2,y]) in BlackPiecesWinList) and \
                       (([x+3,y]) in BlackPiecesWinList):
                        
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                        
                        if ([x+4,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                

                         
                    # 45°
                    if (([x+1,y-1]) in BlackPiecesWinList) and \
                       (([x+2,y-2]) in BlackPiecesWinList) and \
                       (([x+3,y-3]) in BlackPiecesWinList):

                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                        
                        if ([x+4,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                        
                    # 90°
                    if (([x,y-1]) in BlackPiecesWinList) and \
                       (([x,y-2]) in BlackPiecesWinList) and \
                       (([x,y-3]) in BlackPiecesWinList):
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                            
                                                                         
                    # 135°
                    if (([x-1,y-1]) in BlackPiecesWinList) and \
                       (([x-2,y-2]) in BlackPiecesWinList) and \
                       (([x-3,y-3]) in BlackPiecesWinList):
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x-4,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                

                    # 180°
                    if (([x-1,y]) in BlackPiecesWinList) and \
                       (([x-2,y]) in BlackPiecesWinList) and \
                       (([x-3,y]) in BlackPiecesWinList):
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x-4,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                            
                    # 225°
                    if (([x-1,y+1]) in BlackPiecesWinList) and \
                       (([x-2,y+2]) in BlackPiecesWinList) and \
                       (([x-3,y+3]) in BlackPiecesWinList):
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x-4,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                            
                    # 270°
                    if (([x,y+1]) in BlackPiecesWinList) and \
                       (([x,y+2]) in BlackPiecesWinList) and \
                       (([x,y+3]) in BlackPiecesWinList):
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    # 315°
                    if (([x+1,y+1]) in BlackPiecesWinList) and \
                       (([x+2,y+2]) in BlackPiecesWinList) and \
                       (([x+3,y+3]) in BlackPiecesWinList):
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x+4,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                            
                    
                    # 2.2 -〇▢〇〇-
                    # 0°
                    if (([x-1,y]) in BlackPiecesWinList) and \
                       (([x+1,y]) in BlackPiecesWinList) and \
                       (([x+2,y]) in BlackPiecesWinList):
                        if ([x-2,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x+3,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                        
                         
                         
                    # 45°
                    if (([x-1,y+1]) in BlackPiecesWinList) and \
                       (([x+1,y-1]) in BlackPiecesWinList) and \
                       (([x+2,y-2]) in BlackPiecesWinList):
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    # 90°
                    if (([x,y-1]) in BlackPiecesWinList) and \
                       (([x,y-1]) in BlackPiecesWinList) and \
                       (([x,y-2]) in BlackPiecesWinList):
                        if ([x,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    # 135°
                    if (([x+1,y+1]) in BlackPiecesWinList) and \
                       (([x-1,y-1]) in BlackPiecesWinList) and \
                       (([x-2,y-2]) in BlackPiecesWinList):
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    # 180°
                    if (([x+1,y]) in BlackPiecesWinList) and \
                       (([x-1,y]) in BlackPiecesWinList) and \
                       (([x-2,y]) in BlackPiecesWinList):
                        if ([x+2,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x-3,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    # 225°
                    if (([x+1,y-1]) in BlackPiecesWinList) and \
                       (([x-1,y+1]) in BlackPiecesWinList) and \
                       (([x-2,y+2]) in BlackPiecesWinList):
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    # 270°
                    if (([x,y-1]) in BlackPiecesWinList) and \
                       (([x,y+1]) in BlackPiecesWinList) and \
                       (([x,y+2]) in BlackPiecesWinList):
                        if ([x,y-2])  not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x,y-2])  not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    # 315°
                    if (([x-1,y-1]) in BlackPiecesWinList) and \
                       (([x+1,y+1]) in BlackPiecesWinList) and \
                       (([x+2,y+2]) in BlackPiecesWinList):
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["Connect 4"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 4"]
                                
                    ## 2.3 -▢-〇〇〇
                    # 0°
                    if ([x+2,y]) in BlackPiecesWinList and \
                       ([x+3,y]) in BlackPiecesWinList and \
                       ([x+4,y]) in BlackPiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                
                    # 45°
                    if ([x+2,y-2]) in BlackPiecesWinList and \
                       ([x+3,y-3]) in BlackPiecesWinList and \
                       ([x+4,y-4]) in BlackPiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                
                    # 90°
                    if ([x,y-2]) in BlackPiecesWinList and \
                       ([x,y-3]) in BlackPiecesWinList and \
                       ([x,y-4]) in BlackPiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-2,y-2]) in BlackPiecesWinList and \
                       ([x-3,y-3]) in BlackPiecesWinList and \
                       ([x-4,y-4]) in BlackPiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-2,y]) in BlackPiecesWinList and \
                       ([x-3,y]) in BlackPiecesWinList and \
                       ([x-4,y]) in BlackPiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-2,y+2]) in BlackPiecesWinList and \
                       ([x-3,y+3]) in BlackPiecesWinList and \
                       ([x-4,y+4]) in BlackPiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+2]) in BlackPiecesWinList and \
                       ([x,y+3]) in BlackPiecesWinList and \
                       ([x,y+4]) in BlackPiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+2,y+2]) in BlackPiecesWinList and \
                       ([x+3,y+3]) in BlackPiecesWinList and \
                       ([x+4,y+4]) in BlackPiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            
                    ## 2.4 -▢〇-〇〇 
                    # 0°
                    if ([x+1,y]) in BlackPiecesWinList and \
                       ([x+3,y]) in BlackPiecesWinList and \
                       ([x+4,y]) in BlackPiecesWinList:
                        if ([x+2,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 45°
                    if ([x+1,y-1]) in BlackPiecesWinList and \
                       ([x+3,y-3]) in BlackPiecesWinList and \
                       ([x+4,y-4]) in BlackPiecesWinList:
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-1]) in BlackPiecesWinList and \
                       ([x,y-3]) in BlackPiecesWinList and \
                       ([x,y-4]) in BlackPiecesWinList:
                        if ([x,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-1,y-1]) in BlackPiecesWinList and \
                       ([x-3,y-3]) in BlackPiecesWinList and \
                       ([x-4,y-4]) in BlackPiecesWinList:
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-1,y]) in BlackPiecesWinList and \
                       ([x-3,y]) in BlackPiecesWinList and \
                       ([x-4,y]) in BlackPiecesWinList:
                        if ([x-2,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-1,y+1]) in BlackPiecesWinList and \
                       ([x-3,y+3]) in BlackPiecesWinList and \
                       ([x-4,y+4]) in BlackPiecesWinList:
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+1]) in BlackPiecesWinList and \
                       ([x,y+3]) in BlackPiecesWinList and \
                       ([x,y+4]) in BlackPiecesWinList:
                        if ([x,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+1,y+1]) in BlackPiecesWinList and \
                       ([x+3,y+3]) in BlackPiecesWinList and \
                       ([x+4,y+4]) in BlackPiecesWinList:
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                
                    ## 2.5-▢〇〇-〇  
                    # 0°
                    if ([x+1,y]) in BlackPiecesWinList and \
                       ([x+2,y]) in BlackPiecesWinList and \
                       ([x+4,y]) in BlackPiecesWinList:
                        if ([x+3,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 45°
                    if ([x+1,y-1]) in BlackPiecesWinList and \
                       ([x+2,y-2]) in BlackPiecesWinList and \
                       ([x+4,y-4]) in BlackPiecesWinList:
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-1]) in BlackPiecesWinList and \
                       ([x,y-2]) in BlackPiecesWinList and \
                       ([x,y-4]) in BlackPiecesWinList:
                        if ([x,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-1,y-1]) in BlackPiecesWinList and \
                       ([x-2,y-2]) in BlackPiecesWinList and \
                       ([x-4,y-4]) in BlackPiecesWinList:
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-1,y]) in BlackPiecesWinList and \
                       ([x-2,y]) in BlackPiecesWinList and \
                       ([x-4,y]) in BlackPiecesWinList:
                        if ([x-3,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-1,y+1]) in BlackPiecesWinList and \
                       ([x-2,y+2]) in BlackPiecesWinList and \
                       ([x-4,y+4]) in BlackPiecesWinList:
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+1]) in BlackPiecesWinList and \
                       ([x,y+2]) in BlackPiecesWinList and \
                       ([x,y+4]) in BlackPiecesWinList:
                        if ([x,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+1,y+1]) in BlackPiecesWinList and \
                       ([x+2,y+2]) in BlackPiecesWinList and \
                       ([x+4,y+4]) in BlackPiecesWinList:
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                
                    ## 2.6 -▢〇-〇-〇-
                    # 0°
                    if ([x+1,y]) in BlackPiecesWinList and \
                       ([x+3,y]) in BlackPiecesWinList and \
                       ([x+5,y]) in BlackPiecesWinList:
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x-1,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]                               
                    # 45°
                    if ([x+1,y-1]) in BlackPiecesWinList and \
                       ([x+3,y-3]) in BlackPiecesWinList and \
                       ([x+5,y-5]) in BlackPiecesWinList:
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x-1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-1]) in BlackPiecesWinList and \
                       ([x,y-3]) in BlackPiecesWinList and \
                       ([x,y-5]) in BlackPiecesWinList:
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x,y+1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-1,y-1]) in BlackPiecesWinList and \
                       ([x-3,y-3]) in BlackPiecesWinList and \
                       ([x-5,y-5]) in BlackPiecesWinList:
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x+1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-1,y]) in BlackPiecesWinList and \
                       ([x-3,y]) in BlackPiecesWinList and \
                       ([x-5,y]) in BlackPiecesWinList:
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x+1,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-1,y+1]) in BlackPiecesWinList and \
                       ([x-3,y+3]) in BlackPiecesWinList and \
                       ([x-5,y+5]) in BlackPiecesWinList:
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x+1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+1]) in BlackPiecesWinList and \
                       ([x,y+3]) in BlackPiecesWinList and \
                       ([x,y+5]) in BlackPiecesWinList:
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x,y-1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+1,y+1]) in BlackPiecesWinList and \
                       ([x+3,y+3]) in BlackPiecesWinList and \
                       ([x+5,y+5]) in BlackPiecesWinList:
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                if ([x-1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["HalfConnect 4"]
                    
                    
                    
                    ## 2.7 -〇〇▢-〇
                    # 0°
                    if ([x+2,y]) in BlackPiecesWinList and \
                       ([x-1,y]) in BlackPiecesWinList and \
                       ([x-2,y]) in BlackPiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 45°
                    if ([x+2,y-2]) in BlackPiecesWinList and \
                       ([x-1,y+1]) in BlackPiecesWinList and \
                       ([x-2,y+2]) in BlackPiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 90°
                    if ([x,y-2]) in BlackPiecesWinList and \
                       ([x,y+1]) in BlackPiecesWinList and \
                       ([x,y+2]) in BlackPiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 135°
                    if ([x-2,y-2]) in BlackPiecesWinList and \
                       ([x+1,y+1]) in BlackPiecesWinList and \
                       ([x+2,y+2]) in BlackPiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 180°
                    if ([x-2,y]) in BlackPiecesWinList and \
                       ([x+1,y]) in BlackPiecesWinList and \
                       ([x+2,y]) in BlackPiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 225°
                    if ([x-2,y+2]) in BlackPiecesWinList and \
                       ([x+1,y-1]) in BlackPiecesWinList and \
                       ([x+2,y-2]) in BlackPiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 270°
                    if ([x,y+2]) in BlackPiecesWinList and \
                       ([x,y-1]) in BlackPiecesWinList and \
                       ([x,y-2]) in BlackPiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    # 315°
                    if ([x+2,y+2]) in BlackPiecesWinList and \
                       ([x-1,y-1]) in BlackPiecesWinList and \
                       ([x-2,y-2]) in BlackPiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                    
                    ## 2.8 -〇〇-▢〇-
                    # 0°
                    if ([x+1,y]) in BlackPiecesWinList and \
                       ([x-2,y]) in BlackPiecesWinList and \
                       ([x-3,y]) in BlackPiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                              
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]
                                                         
                    # 45°
                    if ([x+1,y-1]) in BlackPiecesWinList and \
                       ([x-2,y+2]) in BlackPiecesWinList and \
                       ([x-3,y+3]) in BlackPiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 90°
                    if ([x,y-1]) in BlackPiecesWinList and \
                       ([x,y+2]) in BlackPiecesWinList and \
                       ([x,y+3]) in BlackPiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 135°
                    if ([x-1,y-1]) in BlackPiecesWinList and \
                       ([x+2,y+2]) in BlackPiecesWinList and \
                       ([x+3,y+3]) in BlackPiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 180°
                    if ([x-1,y]) in BlackPiecesWinList and \
                       ([x+2,y]) in BlackPiecesWinList and \
                       ([x+3,y]) in BlackPiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 225°
                    if ([x-1,y+1]) in BlackPiecesWinList and \
                       ([x+2,y-2]) in BlackPiecesWinList and \
                       ([x+3,y-3]) in BlackPiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 270°
                    if ([x,y+1]) in BlackPiecesWinList and \
                       ([x,y-2]) in BlackPiecesWinList and \
                       ([x,y-3]) in BlackPiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                    # 315°
                    if ([x+1,y+1]) in BlackPiecesWinList and \
                       ([x-2,y-2]) in BlackPiecesWinList and \
                       ([x-3,y-3]) in BlackPiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 4"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 4"]

                                

                    # 3. Connect 3
                    # 3.1 -▢〇〇-
                    # 0°
                    if (([x+1,y]) in BlackPiecesWinList) and \
                       (([x+2,y]) in BlackPiecesWinList):
                        if ([x-1,y]) not in TotalPiecesTestList:
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x+3,y]) not in TotalPiecesTestList:
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                         
                    # 45°
                    if (([x+1,y-1]) in BlackPiecesWinList) and \
                       (([x+2,y-2]) in BlackPiecesWinList):
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 90°
                    if (([x,y-1]) in BlackPiecesWinList) and \
                       (([x,y-2]) in BlackPiecesWinList):
                        if ([x,y+1]) not in TotalPiecesTestList:
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x,y-3]) not in TotalPiecesTestList:
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                                            
                    # 135°
                    if (([x-1,y-1]) in BlackPiecesWinList) and \
                       (([x-2,y-2]) in BlackPiecesWinList):
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 180°
                    if (([x-1,y]) in BlackPiecesWinList) and \
                       (([x-2,y]) in BlackPiecesWinList):
                        if ([x+1,y]) not in TotalPiecesTestList:
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x-3,y]) not in TotalPiecesTestList:
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 225°
                    if (([x-1,y+1]) in BlackPiecesWinList) and \
                       (([x-2,y+2]) in BlackPiecesWinList):
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 270°
                    if (([x,y+1]) in BlackPiecesWinList) and \
                       (([x,y+2]) in BlackPiecesWinList):
                        if ([x,y-1]) not in TotalPiecesTestList:
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x,y+3]) not in TotalPiecesTestList:
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 315°
                    if (([x+1,y+1]) in BlackPiecesWinList) and \
                       (([x+2,y+2]) in BlackPiecesWinList):
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    

                    
                    # 3.2 -〇▢〇-
                    # 0°
                    if (([x+1,y]) in BlackPiecesWinList) and \
                       (([x-1,y]) in BlackPiecesWinList):
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
            
                    # 45°
                    if (([x+1,y-1]) in BlackPiecesWinList) and \
                       (([x-1,y+1]) in BlackPiecesWinList):
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    
                    # 90°
                    if (([x,y-1]) in BlackPiecesWinList) and \
                       (([x,y+1]) in BlackPiecesWinList):
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 135°
                    if (([x-1,y-1]) in BlackPiecesWinList) and \
                       (([x+1,y+1]) in BlackPiecesWinList):
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    
                    # 180°
                    if (([x-1,y]) in BlackPiecesWinList) and \
                       (([x+1,y]) in BlackPiecesWinList):
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 225°
                    if (([x-1,y+1]) in BlackPiecesWinList) and \
                       (([x+1,y-1]) in BlackPiecesWinList):
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    
                    # 270°
                    if (([x,y+1]) in BlackPiecesWinList) and \
                       (([x,y-1]) in BlackPiecesWinList):
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                    # 315°
                    if (([x+1,y+1]) in BlackPiecesWinList) and \
                       (([x-1,y-1]) in BlackPiecesWinList):
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["Connect 3"]
                                
                    ## 3.3 -▢〇-〇-
                    # 0°
                    if ([x+1,y]) in BlackPiecesWinList and \
                       ([x+3,y]) in BlackPiecesWinList and \
                       ([x+2,y]) not in TotalPiecesTestList:
                        if ([x+4,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 45°
                    if ([x+1,y-1]) in BlackPiecesWinList and \
                       ([x+3,y-3]) in BlackPiecesWinList and \
                       ([x+2,y-2]) not in TotalPiecesTestList:
                        if ([x+4,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 90°
                    if ([x,y-1]) in BlackPiecesWinList and \
                       ([x,y-3]) in BlackPiecesWinList and \
                       ([x,y-2]) not in TotalPiecesTestList:
                        if ([x,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 135°
                    if ([x-1,y-1]) in BlackPiecesWinList and \
                       ([x-3,y-3]) in BlackPiecesWinList and \
                       ([x-2,y-2]) not in TotalPiecesTestList:
                        if ([x-4,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 180°
                    if ([x-1,y]) in BlackPiecesWinList and \
                       ([x-3,y]) in BlackPiecesWinList and \
                       ([x-2,y]) not in TotalPiecesTestList:
                        if ([x-4,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 225°
                    if ([x-1,y+1]) in BlackPiecesWinList and \
                       ([x-3,y+3]) in BlackPiecesWinList and \
                       ([x-2,y+2]) not in TotalPiecesTestList:
                        if ([x-4,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 270°
                    if ([x,y+1]) in BlackPiecesWinList and \
                       ([x,y+3]) in BlackPiecesWinList and \
                       ([x,y+2]) not in TotalPiecesTestList:
                        if ([x,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 315°
                    if ([x+1,y+1]) in BlackPiecesWinList and \
                       ([x+3,y+3]) in BlackPiecesWinList and \
                       ([x+2,y+2]) not in TotalPiecesTestList:
                        if ([x+4,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    
            
                    ## 3.4 -〇▢-〇-
                    # 0°
                    if ([x+2,y]) in BlackPiecesWinList and \
                       ([x-1,y]) in BlackPiecesWinList and \
                       ([x+1,y]) not in TotalPiecesTestList:
                        if ([x+3,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-2,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]                           
                    # 45°
                    if ([x+2,y-2]) in BlackPiecesWinList and \
                       ([x-1,y+1]) in BlackPiecesWinList and \
                       ([x+1,y-1]) not in TotalPiecesTestList:
                        if ([x+3,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 90°
                    if ([x,y-2]) in BlackPiecesWinList and \
                       ([x,y+1]) in BlackPiecesWinList and \
                       ([x,y-1]) not in TotalPiecesTestList:
                        if ([x,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 135°
                    if ([x-2,y-2]) in BlackPiecesWinList and \
                       ([x+1,y+1]) in BlackPiecesWinList and \
                       ([x-1,y-1]) not in TotalPiecesTestList:
                        if ([x-3,y-3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 180°
                    if ([x-2,y]) in BlackPiecesWinList and \
                       ([x+1,y]) in BlackPiecesWinList and \
                       ([x-1,y]) not in TotalPiecesTestList:
                        if ([x-3,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+2,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 225°
                    if ([x-2,y+2]) in BlackPiecesWinList and \
                       ([x+1,y-1]) in BlackPiecesWinList and \
                       ([x-1,y+1]) not in TotalPiecesTestList:
                        if ([x-3,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]

                    # 270°
                    if ([x,y+2]) in BlackPiecesWinList and \
                       ([x,y-1]) in BlackPiecesWinList and \
                       ([x,y+1]) not in TotalPiecesTestList:
                        if ([x,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 315°
                    if ([x+2,y+2]) in BlackPiecesWinList and \
                       ([x-1,y-1]) in BlackPiecesWinList and \
                       ([x+1,y+1]) not in TotalPiecesTestList:
                        if ([x+3,y+3]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                                
                    ## 3.5 -▢-〇〇-
                    # 0°
                    if ([x+2,y]) in BlackPiecesWinList and \
                       ([x+3,y]) in BlackPiecesWinList and \
                       ([x+1,y]) not in TotalPiecesTestList:
                        if ([x+4,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 45°
                    if ([x+2,y-2]) in BlackPiecesWinList and \
                       ([x+3,y-3]) in BlackPiecesWinList and \
                       ([x+1,y-1]) not in TotalPiecesTestList:
                        if ([x+4,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 90°
                    if ([x,y-2]) in BlackPiecesWinList and \
                       ([x,y-3]) in BlackPiecesWinList and \
                       ([x,y-1]) not in TotalPiecesTestList:
                        if ([x,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 135°
                    if ([x-2,y-2]) in BlackPiecesWinList and \
                       ([x-3,y-3]) in BlackPiecesWinList and \
                       ([x-1,y-1]) not in TotalPiecesTestList:
                        if ([x-4,y-4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-4,y-4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 180°
                    if ([x-2,y]) in BlackPiecesWinList and \
                       ([x-3,y]) in BlackPiecesWinList and \
                       ([x-1,y]) not in TotalPiecesTestList:
                        if ([x-4,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+1,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+1,y]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-4,y]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 225°
                    if ([x-2,y+2]) in BlackPiecesWinList and \
                       ([x-3,y+3]) in BlackPiecesWinList and \
                       ([x-1,y+1]) not in TotalPiecesTestList:
                        if ([x-4,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 270°
                    if ([x,y+2]) in BlackPiecesWinList and \
                       ([x,y+3]) in BlackPiecesWinList and \
                       ([x,y+1]) not in TotalPiecesTestList:
                        if ([x,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                    # 315°
                    if ([x+2,y+2]) in BlackPiecesWinList and \
                       ([x+3,y+3]) in BlackPiecesWinList and \
                       ([x+1,y+1]) not in TotalPiecesTestList:
                        if ([x+4,y+4]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            Score = Score + BlackDictionary["HalfConnect 3"]
                            if ([x+4,y+4]) not in TotalPiecesTestList:
                                Score = Score + BlackDictionary["HalfConnect 3"]

                                
                    # 4. Connect 2
                    # 4.1 ▢〇
                    # 0°
                    if ([x+1,y]) in BlackPiecesWinList:
                        if ([x-1,y]) not in TotalPiecesTestList:
                            if ([x-2,y]) not in TotalPiecesTestList:
                                if ([x-3,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+2,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x+2,y]) not in TotalPiecesTestList:
                                if ([x-2,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+3,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x+2,y]) not in TotalPiecesTestList:
                            if ([x-1,y]) not in TotalPiecesTestList:
                                if ([x-2,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+3,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x+3,y]) not in TotalPiecesTestList:
                                if ([x-1,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+4,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
      
  
                    # 45°
                    if ([x+1,y-1]) in BlackPiecesWinList:
                        if ([x-1,y+1]) not in TotalPiecesTestList:
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                if ([x-3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                if ([x-2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x+2,y-2]) not in TotalPiecesTestList:
                            if ([x-1,y+1]) not in TotalPiecesTestList:
                                if ([x-2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x+3,y-3]) not in TotalPiecesTestList:
                                if ([x-1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+4,y-4]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
      
 
                    # 90°
                    if ([x,y-1]) in BlackPiecesWinList:
                        if ([x,y+1]) not in TotalPiecesTestList:
                            if ([x,y+2]) not in TotalPiecesTestList:
                                if ([x,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x,y-2]) not in TotalPiecesTestList:
                                if ([x,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x,y-2]) not in TotalPiecesTestList:
                            if ([x,y+1]) not in TotalPiecesTestList:
                                if ([x,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x,y-3]) not in TotalPiecesTestList:
                                if ([x,y+1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y-4]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
     
    
                    # 135°
                    if ([x-1,y-1]) in BlackPiecesWinList:
                        if ([x+1,y+1]) not in TotalPiecesTestList:
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                if ([x+3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                if ([x+2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x-2,y-2]) not in TotalPiecesTestList:
                            if ([x+1,y+1]) not in TotalPiecesTestList:
                                if ([x+2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x-3,y-3]) not in TotalPiecesTestList:
                                if ([x+1,y+1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-4,y-4]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
      
    
                    # 180°
                    if ([x-1,y]) in BlackPiecesWinList:
                        if ([x+1,y]) not in TotalPiecesTestList:
                            if ([x+2,y]) not in TotalPiecesTestList:
                                if ([x+3,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-2,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x-2,y]) not in TotalPiecesTestList:
                                if ([x+2,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-3,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x-2,y]) not in TotalPiecesTestList:
                            if ([x+1,y]) not in TotalPiecesTestList:
                                if ([x+2,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-3,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x-3,y]) not in TotalPiecesTestList:
                                if ([x+1,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-4,y]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
          
                    # 225°
                    if ([x-1,y+1]) in BlackPiecesWinList:
                        if ([x+1,y-1]) not in TotalPiecesTestList:
                            if ([x+2,y-2]) not in TotalPiecesTestList:
                                if ([x+3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x-2,y+2]) not in TotalPiecesTestList:
                                if ([x+2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x-2,y+2]) not in TotalPiecesTestList:
                            if ([x+1,y-1]) not in TotalPiecesTestList:
                                if ([x+2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x-3,y+3]) not in TotalPiecesTestList:
                                if ([x+1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x-4,y+4]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
    
      
                    # 270°
                    if ([x,y+1]) in BlackPiecesWinList:
                        if ([x,y-1]) not in TotalPiecesTestList:
                            if ([x,y-2]) not in TotalPiecesTestList:
                                if ([x,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x,y+2]) not in TotalPiecesTestList:
                                if ([x,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x,y+2]) not in TotalPiecesTestList:
                            if ([x,y-1]) not in TotalPiecesTestList:
                                if ([x,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x,y+3]) not in TotalPiecesTestList:
                                if ([x,y-1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x,y+4]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
     
   
                    # 315°
                    if ([x+1,y+1]) in BlackPiecesWinList:
                        if ([x-1,y-1]) not in TotalPiecesTestList:
                            if ([x-2,y-2]) not in TotalPiecesTestList:
                                if ([x-3,y-3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+2,y+2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x+2,y+2]) not in TotalPiecesTestList:
                                if ([x-2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                        if ([x+2,y+2]) not in TotalPiecesTestList:
                            if ([x-1,y-1]) not in TotalPiecesTestList:
                                if ([x-2,y-2]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+3,y+3]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                            if ([x+3,y+3]) not in TotalPiecesTestList:
                                if ([x-1,y-1]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]
                                if ([x+4,y+4]) not in TotalPiecesTestList:
                                    Score = Score + BlackDictionary["Connect 2"]

                    # Add the Score and coordinate of this point into the ScoreDictionary.
                    ScoreDictionary.update({Score:[x,y]})
                    # Change the Score back to zero before test the value of next point.
                    Score = 0

## 1. The reason of all of these statement are "if" instead of "elif" and some \
## coordinates are used more than once in one direction is allowing AI to go through \
## every situation of this point and add all the score if this point satisfied with
## these situations. In other words, if this coordinate could not only make black piece\
## become "connect 4" but also could stop white piece becoming "connect 4", this point's\
## value will be fairly high, and if it is the highest value, AI will place the black piece\
## on this point.
## 2. This also allows codes become more concise, since if this point could let\
## black piece become double "Connect 3", the "connect 3" score will be added\
## twice and it will be higher than the point which on can make black piece become\
## one "connect 3". So in this case, we do not need to write codes for double \
## "Connect 3".
   
                                                                   


    def Set():
        
        global ScoreDictionary
        if ScoreDictionary != {}: # If there is still an empty point on the board
            if Round % 2 != 0: # Round 1,3,5... AI is white

                # Double check this point is not on the board
                if len(BlackPiecesDisplayList) > len(WhitePiecesDisplayList) and (ScoreDictionary[max(ScoreDictionary)] not in TotalPiecesTestList):
                    
                    WhitePiecesWinList.append(ScoreDictionary[max(ScoreDictionary)])
                    # Choose the most appropriate point (highest key(score) of the dict.)
                    TotalPiecesTestList.append(ScoreDictionary[max(ScoreDictionary)])
                    X = (ScoreDictionary[max(ScoreDictionary)])[0]
                    Y = (ScoreDictionary[max(ScoreDictionary)])[1]

                    # Tansfer assumed coordinate to actual coordinate.
                    WhitePiecesDisplayList.append([(X*45)+40,(Y*45)+50])
                    
                    # Make the ScoreDictionary empty for next evaluate.
                    ScoreDictionary = {}               

            if Round % 2 == 0:
                
                if len(BlackPiecesDisplayList) == 0: # Empty board

                    # Center point
                    BlackPiecesWinList.append([7,7])
                    BlackPiecesDisplayList.append([355,365])
                    TotalPiecesTestList.append([7,7])
                    
                elif len(BlackPiecesDisplayList) == len(WhitePiecesDisplayList) and (ScoreDictionary[max(ScoreDictionary)] not in TotalPiecesTestList):
                    BlackPiecesWinList.append(ScoreDictionary[max(ScoreDictionary)])
                    TotalPiecesTestList.append(ScoreDictionary[max(ScoreDictionary)])
                    X = (ScoreDictionary[max(ScoreDictionary)])[0]
                    Y = (ScoreDictionary[max(ScoreDictionary)])[1]
                    BlackPiecesDisplayList.append([(X*45)+40,(Y*45)+50])
     

                    ScoreDictionary = {}
        # Since this is "elif", so if ScoreDictionary is not empty, it would not\
        # enter this statement. And if ScoreDictionary is not not empty, which means \
        # it is empty, and which means the board is full, and game is not over, it \
        # wiil be tie game.
        elif ScoreDictionary == {}: 
            TieGame = 1

           
            
##########################################################
# Variables

Start = 1 # True
WinBlack = 0 
WinWhite = 0
TieGame = 0
# Counter, used to check which player starts first
Round = 1

cp1 = 0 # player's name corlor
cp2 = 255
Interface = 1
PVP = 0
PVE = 0

Name = 0

RemindPVP = 0
RemindPVE = 0
RemindQuitGame = 0

RemindReStart = 0
RemindUndo = 0
RemindQuit = 0
RemindHelp = 0



##########################################################
# Main loop


while Start:

    # Set the background corlor
    screen.fill(PERU)

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = 0 # False
            
        # Show the interface    
        if Interface == 1:
            
            # Draw the interface page
            Draw.StartInterface(screen)

            
            # PVP button
            if (pygame.mouse.get_pos()[0] <= 307) and \
               (pygame.mouse.get_pos()[0] >= 215) and \
               (pygame.mouse.get_pos()[1] <= 478) and \
               (pygame.mouse.get_pos()[1] >= 435):
                RemindPVP = 1
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Name == 0: # Names have not entered
                        NameHintText = pygame.font.SysFont("Helvetica",50)
                        NameHint = NameHintText.render("Please enter your names in the Shell!", \
                                           1,(255,0,0))
                        screen.blit(NameHint,(200,550))
                        time.sleep(0.1) 
                        
                        PVP = 1 # PVP mode is chosen
                        Interface = 0
                
            # PVE button
            elif (pygame.mouse.get_pos()[0] <= 555) and \
                 (pygame.mouse.get_pos()[0] >= 463) and \
                 (pygame.mouse.get_pos()[1] <= 478) and \
                 (pygame.mouse.get_pos()[1] >= 435):
                RemindPVE = 1
                
                if event.type == pygame.MOUSEBUTTONDOWN:                   
                    if Name == 0: # Name has not entered
                        NameHintText = pygame.font.SysFont("Helvetica",50)
                        NameHint = NameHintText.render("Please enter your name in the Shell!", \
                                           1,(255,0,0))
                        screen.blit(NameHint,(200,550))
                        time.sleep(0.1)

                        PVE = 1 # PVE mode is chosen
                        Interface = 0

            # Quit button
            elif (pygame.mouse.get_pos()[0] <= 812) and \
                 (pygame.mouse.get_pos()[0] >= 711) and \
                 (pygame.mouse.get_pos()[1] <= 478) and \
                 (pygame.mouse.get_pos()[1] >= 435):
                RemindQuitGame = 1
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 0 # Quit the game
                       

            # Flip screen
            pygame.display.flip()

            # Same FPS
            clock.tick(60)

             
        # PVP mode 
        elif PVP == 1:
            
            # Darw the board
            Draw.Board(screen)
                           

            # Doaw the ScoreBoard
            Draw.PlayerInformation()
            

            # Draw the operators
            Draw.Operators(screen)


            # 1. In game
            if WinBlack == 0 and WinWhite == 0 and TieGame == 0:
                
                # 1.1 Black and white pieces.

                if (pygame.mouse.get_pos()[0] <= 680) and \
                   (pygame.mouse.get_pos()[0] >= 30) and \
                   (pygame.mouse.get_pos()[1]<= 690) and \
                   (pygame.mouse.get_pos()[1] >= 40):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Draw.ClickBlack()
                        TotalPieces.BlackPiecesPosition() # Test the win condition

                        Draw.ClickWhite()
                        TotalPieces.WhitePiecesPosition()

                # 1.2 Undo
                elif (pygame.mouse.get_pos()[0] <= 915) and \
                     (pygame.mouse.get_pos()[0] >= 760) and \
                     (pygame.mouse.get_pos()[1] <= 295) and \
                     (pygame.mouse.get_pos()[1] >= 250):
                    RemindUndo = 1
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Operator.Undo()
                    
                # 1.3 Help
                elif (pygame.mouse.get_pos()[0] <= 915) and \
                     (pygame.mouse.get_pos()[0] >= 760) and \
                     (pygame.mouse.get_pos()[1] <= 585) and \
                     (pygame.mouse.get_pos()[1] >= 540):
                    RemindHelp = 1
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Operator.Help()
                        TotalPieces.BlackPiecesPosition()
                        TotalPieces.WhitePiecesPosition()
                        
                # 1.4 ReStart
                elif (pygame.mouse.get_pos()[0] <= 915) and \
                     (pygame.mouse.get_pos()[0] >= 760) and \
                     (pygame.mouse.get_pos()[1] <= 160) and \
                     (pygame.mouse.get_pos()[1] >= 115):
                    RemindReStart = 1
                        


                        
            # 2. End game
            if WinBlack == 1 or WinWhite == 1 or TieGame == 1:

                # 2.1 ReStart
                if (pygame.mouse.get_pos()[0] <= 915) and \
                   (pygame.mouse.get_pos()[0] >= 760) and \
                   (pygame.mouse.get_pos()[1] <= 160) and \
                   (pygame.mouse.get_pos()[1] >= 115):
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        Operator.ReStart()
                        
            # 3. Quit
            if (pygame.mouse.get_pos()[0] <= 915) and \
                 (pygame.mouse.get_pos()[0] >= 760) and \
                 (pygame.mouse.get_pos()[1] <= 440) and \
                 (pygame.mouse.get_pos()[1] >= 395):
                RemindQuit = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Operator.Quit()



            # Present the cursor
            Draw.Cursor(screen)

            # Draw the pieces
            Draw.BlackPieces(screen)
            Draw.WhitePieces(screen)

            # Draw the Hint
            Draw.Hint(screen)

            # Present results
            Draw.Result(screen)

            
            # Flip screen
            pygame.display.flip()

            # Same FPS
            clock.tick(60)

        # PVE mode

        elif PVE == 1:

            # Draw the Board
            Draw.Board(screen)


            # Draw the ScoreBoard
            Draw.PlayerInformation()

            # Draw the operators
            Draw.Operators(screen)

            # 1. In game
            if WinBlack == 0 and WinWhite == 0 and TieGame == 0:

                # 1.1 Player first
                if Round % 2 != 0:

                    # 1.1.1 AI white pieces
                    if len(BlackPiecesDisplayList) > len(WhitePiecesDisplayList):
                        AI.Evaluate()
                        AI.Set()
                        TotalPieces.WhitePiecesPosition() # Test the win condition

                    # 1.1.2 Player black pieces
                    if (pygame.mouse.get_pos()[0] <= 680) and \
                       (pygame.mouse.get_pos()[0] >= 30) and \
                       (pygame.mouse.get_pos()[1]<= 690) and \
                       (pygame.mouse.get_pos()[1] >= 40):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            Draw.ClickBlack()
                            TotalPieces.BlackPiecesPosition()
                        
                    # 1.1.3 Undo
                    elif (pygame.mouse.get_pos()[0] <= 915) and \
                         (pygame.mouse.get_pos()[0] >= 760) and \
                         (pygame.mouse.get_pos()[1] <= 295) and \
                         (pygame.mouse.get_pos()[1] >= 250):
                        RemindUndo = 1
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            Operator.Undo()
                            Operator.Undo()
                            
                    # 1.1.4 Help
                    elif (pygame.mouse.get_pos()[0] <= 915) and \
                         (pygame.mouse.get_pos()[0] >= 760) and \
                         (pygame.mouse.get_pos()[1] <= 585) and \
                         (pygame.mouse.get_pos()[1] >= 540):
                        RemindHelp = 1
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            Operator.Help()
                            TotalPieces.BlackPiecesPosition()
                            TotalPieces.WhitePiecesPosition()
                            
                    # 1.1.5 Restart
                    elif (pygame.mouse.get_pos()[0] <= 915) and \
                         (pygame.mouse.get_pos()[0] >= 760) and \
                         (pygame.mouse.get_pos()[1] <= 160) and \
                         (pygame.mouse.get_pos()[1] >= 115):
                        RemindReStart = 1

                           
                # 1.2 AI first
                if Round % 2 ==0:

                    # 1.2.1 AI black pieces
                    if len(BlackPiecesDisplayList) == len(WhitePiecesDisplayList):
                        AI.Evaluate()
                        AI.Set()
                        TotalPieces.BlackPiecesPosition() # Test the win condition
                        
                    # 1.2.2 Player white pieces 
                    if (pygame.mouse.get_pos()[0] <= 680) and \
                       (pygame.mouse.get_pos()[0] >= 30) and \
                       (pygame.mouse.get_pos()[1]<= 690) and \
                       (pygame.mouse.get_pos()[1] >= 40):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            Draw.ClickWhite()
                            TotalPieces.WhitePiecesPosition()

                    # 1.2.3 Undo
                    elif (pygame.mouse.get_pos()[0] <= 915) and \
                         (pygame.mouse.get_pos()[0] >= 760) and \
                         (pygame.mouse.get_pos()[1] <= 295) and \
                         (pygame.mouse.get_pos()[1] >= 250):
                        RemindUndo = 1
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            Operator.Undo()
                            Operator.Undo()
                            
                    # 1.2.4 Help
                    elif (pygame.mouse.get_pos()[0] <= 915) and \
                         (pygame.mouse.get_pos()[0] >= 760) and \
                         (pygame.mouse.get_pos()[1] <= 585) and \
                         (pygame.mouse.get_pos()[1] >= 540):
                        RemindHelp = 1
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            Operator.Help()
                            TotalPieces.BlackPiecesPosition()
                            TotalPieces.WhitePiecesPosition()

                            
                    # 1.2.5 Restart
                    elif (pygame.mouse.get_pos()[0] <= 915) and \
                         (pygame.mouse.get_pos()[0] >= 760) and \
                         (pygame.mouse.get_pos()[1] <= 160) and \
                         (pygame.mouse.get_pos()[1] >= 115):
                        RemindReStart = 1

            # 2. End game
            elif WinBlack == 1 or WinWhite == 1 or TieGame == 1:
                
                # 2.1 Restart
                if (pygame.mouse.get_pos()[0] <= 915) and \
                   (pygame.mouse.get_pos()[0] >= 760) and \
                   (pygame.mouse.get_pos()[1] <= 160) and \
                   (pygame.mouse.get_pos()[1] >= 115):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                       Operator.ReStart()
                

            # 3. Quit

            if (pygame.mouse.get_pos()[0] <= 915) and \
               (pygame.mouse.get_pos()[0] >= 760) and \
               (pygame.mouse.get_pos()[1] <= 440) and \
               (pygame.mouse.get_pos()[1] >= 395):
                RemindQuit = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Operator.Quit()


            # Present the cursor
            Draw.Cursor(screen)

            # Draw the pieces
            Draw.BlackPieces(screen)
            Draw.WhitePieces(screen)

            # Draw the Hint
            Draw.Hint(screen)

            # Present results
            Draw.Result(screen)

            # Flip screen
            pygame.display.flip()

            # Same FPS
            clock.tick(60)       

pygame.quit()
   
