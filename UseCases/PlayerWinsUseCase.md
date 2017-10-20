| Use Case #              | Player wins the game                                        |
| ------------------------|:----------------------------------------------------------:|
| **Goal in Context**         | User wins the game and exits                     |
| **Scope & Level**           | System, Core                                               |
| **Preconditions**           | Game ends, user has earned more points than opponent                                               |
| **Success End Condition**   | User wins the game |
| **Failed End Condition**    | User loses the game       |
| **Primary Actors,<br>Secondary Actors**         | Player,<br>Game, Opponent                                                    |
| **Trigger**                 | Both players pass their turn and there are no valid moves                           |
**DESCRIPTION**
| **Step** | **Action**                                               |
| 1        | Player 1 passes move as there are no valid moves left                         |
| 2        | Player 2 passes moves as there are no valid moves left                       |
| 3        | Game ends                                |
| 4        | Scores are calculated|
| 5        | Outcome reached, Player 1 wins game                                    |
| 6        | Players are removed from the game and the game exits       |
| 7        | Player 1’s win count is increased by 1 |
**EXTENSIONS**
| **Step** | **Branching Action**                                     |
| 2a       | 5 minutes has passed without player making a move        |
| 5a       | Player 2 wins game  |
**VARIATIONS**
| **Step** | **Branching Action**                                     |
| 2        | The other player could be the computer or another person |
