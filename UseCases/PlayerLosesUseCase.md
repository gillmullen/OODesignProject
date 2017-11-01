| Use Case 1                  || Player loses game                                    |
| ------------------------|:----:|:----------------------------------------------:|
| **Goal in Context**         || Player loses the game and exits                      |
| **Scope & Level**           || System, Core                                         |
| **Preconditions**           || Game ends, player has earned less points than opponent |
| **Success End Condition**   || Player loses the game                                |
| **Failed End Condition**    || Player wins the game                                 |
| **Primary Actors** <br>**Secondary Actors** || User  <br>Game. Board.               |
| **Trigger**                 || Both players pass their turn and there are no valid moves|
|**DESCRIPTION**| **Step** | **Action**                                               |
|               | 1        | Player 1 passes move as there are no valid moves left    |
|               | 2        | Player 2 passes moves as there are no valid moves left   |
|               | 3        | Game ends                                                |
|               | 4        | Scores are calculated                                    |
|               | 5        | Outcome reached, Player 1 loses game                     |
|               | 6        | Players are removed from the game and the game exits     |
|               | 7        | Player 2's win count is increased by 1                   |
|**EXTENSIONS** | **Step** | **Branching Action**                                     |
|               | 2a       | 5 minutes has passed without player making a move        |
|               | 5a       | Player 1 wins game                                       |
|**VARIATIONS** | **Step** | **Branching Action**                                     |
|               |  2       | The other player could be the computer or another person |
