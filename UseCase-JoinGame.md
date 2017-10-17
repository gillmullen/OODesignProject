# Player joins a game

| **Use Case 1**                | Player joins a game                         |
|:-----------------------------:|:-:|:-----------------------------------------:|
| **Goal in Context**           || Player starts a game with an opponent player |
| **Scope & Level**             || System, Core                                 |
| **Preconditions**             || Player logged on                             |
| **Success End Condition**     || Player is in a game against another player   |
| **Failed End Condition**      || Player is unable to join a game              |
| **Primary, Secondary Actors** || User, Server, Opponent                       |
| **Trigger**                   || Player logs on with username and password    |
| **DESCRIPTION**               | **Step** | **Action**     |
|| 1 | Player selects board size and their piece colour     |
|| 2 | Server finds appropiate opponent for player          |
|| 3 | Server connects player to opponent                   |
|| 4 | Server generates board                               |
|| 5 | Server prompts black piece player to make first move |
|| 6 | Game starts with black piece player making a move    |
| **EXTENSIONS**                | **Step** | **Branching Action**                           |
| 2a | Server is unable to find appropiate opponent. Alerts Player to change settings       |
| 6a | Black piece player doesn't make a move within 5 minutes                              |
|**VARIATIONS**                 | **Step** | **Branching Action**                           | 
| 1 | Player could select a "random" option which chooses their board/piece colour for them |
| 2 | The opponent player could be computer or person                                       |


