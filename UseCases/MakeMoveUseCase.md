| Use Case 1                  || Player makes a move                                        |
| ------------------------|:----:|:----------------------------------------------:|
| **Goal in Context**         || Player places their piece on the board                     |
| **Scope & Level**           || System, Core                                               |
| **Preconditions**           || Players turn                                               |
| **Success End Condition**   || Player makes a valid move, places their piece on the board |
| **Failed End Condition**    || Player doesn't make a valid move or skips their turn       |
| **Primary Actors** <br>**Secondary Actors** || User  <br>Playing piece. Board.            |
| **Trigger**                 || Other player finished their turn                           |
|**DESCRIPTION**| **Step** | **Action**                                               |
|               | 1        | Other player finished their turn                         |
|               | 2        | Player places a piece on the board                       |
|               | 3        | System validates the move                                |
|               | 4        | System removes any of the other player's pieces<br>that are surrounded by this player's pieces|
|               | 5        |Players turn has ended                                    |
|**EXTENSIONS** | **Step** | **Branching Action**                                     |
|               | 2a       | 5 minutes has passed without player making a move        |
|               | 2b       | Player passes their turn                                 |
|               | 3a       |Player doesn’t make valid move                            |
|**VARIATIONS** | **Step** | **Branching Action**                                     |
|               |  1       | The other player could be the computer or another person |
