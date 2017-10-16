# Player Leaves Game

| **Use Case**                  | Player Leaves Game                    |
|:-----------------------------:|:-------------------------------------:|
| **Goal in Context**           | Player quits from the game            |
| **Scope & Level**             | System                                |
| **Preconditions**             | The user has to be in a game          |
| **Success End Condition**     | The user has quit and subsequently lost the game. The other player has won the game |
| **Failed End Condition**      | Both users continue to play the game  |
| **Secondary Actors**          | Game User One, Server                 |
| **Secondary Actors**          | Game User Two                         |
| **Trigger**                   | Player leaves game                    |
| **Description**                                                       | 
| **Step** | **Action**                                                 |
| 1        | Player One invokes leave game                              |
| 2        | Server tells Player One they have left the game            |
| 3        | Server tells Player Two, Player One has left the game      |
| 4        | Player Two's win counter is increased by the server        |
| **Extensions**                                                        |
| **Step** | **Branching Action**                                       |
|          |                                                            |
| **VARIATIONS**                                                        |
| **Step** | **Branching Action**                                       |
| 1       | The person could be leaving beacuse the game has timed them out   |
