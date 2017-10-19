## Scenarios

- **User John logs on**
  - **Current System State:**
    Server is waiting for user John to input his details.
  - **Informal Scenario:**
    User John enters his username. The server prompts John to choose his game settings such as the board size (9x9, 13x13 or 19x19) and his piece (black or white).
  - **Next Scenario:**
    User John initiates a game.
   
- **User John initiates a game**
  - **Current System State:**
    User John has logged on and must choose his game settings.
  - **Informal Scenario:**
    John chooses the 19x19 board size and the black piece. He then waits for the server to connect him with an appropriate player. 
  - **Next Scenario:**
    Server matches two users together.

- **Server matches two users together**
  - **Current System State:**
    There are two players not in the game. User Julie and user John are looking for a game of size 19x19, John wants to be black and Julie wants to be white.
  - **Informal Scenario:**
    The server sees there are 2 players looking for a game and choices match. It starts a game and places them in the active game.
  - **Next Scenario:**
    The Server needs to generate a board of 19x19 size and start the game

- **Server starts the game**
  - **Current System State:**
    There are two players in the game. User Julie and user John selected a game of size 19x19.
  - **Informal Scenario:**
    The server generates a board of size 19x19 and prompts the black user, John to go first.
  - **Next Scenario:**
    User John makes a move

- **User John makes a move**
  - **Current System State:**
    The has begun and it's John's turn
  - **Informal Scenario:**
    John places a black piece on the board. If black pieces surround any white pieces then those white pieces are removed from the board and John keeps them.
  - **Next Scenario:**
    User Julie makes a move or User wins the game
    
- **User Julie makes a move**
  - **Current System State:**
    John places a black piece on the board and now its Julie's turn
  - **Informal Scenario:**
    Julie places a white piece on the board. If white pieces surround any black pieces then those black pieces are removed from the board and Julie keeps them.
  - **Next Scenario:**
    User John makes a move

- **User plays knock out move**
  - **Current System State:**
    There are two players in the game. User Julie has just made a move taking John's piece. It is user John's go.
  - **Informal Scenario:**
    User John makes a move that results in the board being is such a position that it was before Julie's move. 
  - **Next Scenario:**
    The move is reversed and John must make a legal move.

- **User plays suicide move**
  - **Current System State:**
    There are two players in the game. User Julie has a square surrounded. It is user John's go.
  - **Informal Scenario:**
    User John moves his piece into the surrounded square letting his piece be captured immediatly. 
  - **Next Scenario:**
    The move is reversed and John must make a legal move.

- **5 minutes have passed and John has not maked a move**
  - **Current System State:**
    It is John's go.
  - **Informal Scenario:**
    5 minutes have passed and there has been no input from John
  - **Next Scenario:**
    User Julie wins the game

- **User wins the game:**
  - **Current System State:**
    There are two players in the game. User John didn't take a turn and his timer timed out.
  - **Informal Scenario:**
    User John didn't make a move therefore ending the game and Julie wins.
  - **Next Scenario:**
    Both users have been removed from the game. Julie’s win counter has increased by 1.

- **User loses the game:**
  - **Current System State:**
    There are two players in the game. User John didn't take a turn and his timer timed out.
  - **Informal Scenario:**
    User John didn't make a move therefore ending the game and losing.
  - **Next Scenario:**
    Both users have been removed from the game. User John’s loss counter has increased by 1.




