# Player makes an illegal move

| **Use Case 3**                  || Player makes an illegal move                    |
|:-----------------------------:|:---:|:--------------------------------:|
| **Goal in Context**           || Player is notified they played an illegal move and asked to make a new move            |
| **Scope & Level**             || System                                |
| **Preconditions**             || User must be in a game and have played an invalid move          |
| **Success End Condition**     || User makes a different valid move and play continues |
| **Failed End Condition**      || User quits or passes their turn.  |
| **Primary Actors** || Player 1  |
| **Secondary Actors** || Player 2, board, pieces, server |
| **Trigger**                   || Users move returns invalid                    |
| **Description**           | **Step** | **Action**                                            |
|                           | 1        | Player one makes an invalid move                         |
|                           | 2        | Server notifies player one of the invalid move       |
|                           | 3        | Player one makes a new valid move |
|                           | 4        | Player two is now notified it is their turn   |
| **Extensions**            | **Step** | **Branching Action**                                  |
|                           | 3a       | Player one makes a new invalid move |
|                           | 3b       | Player one passes their turn |
|                           | 3c       | Player one leaves the game |
|                           | 3d       | Player one makes no move and the countdown timer reaches zero |