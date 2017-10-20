# Structured walkthrough
## Server
- Server finds and connects two opponents to a game.
- Server indicates to the user with black disks that it's their turn.
- Server sets a timer at the start of each users turn.
- Each time a user makes a move the server validates it.
- Game ends when two users pass in a row.
- Server calculates who won and users are notified. 
- Once game has ended users are returned to the main menu.
- Server updates the winner's win counter. 

## Client
- User logs onto server. 
- User chooses game settings.
- User joins a game.
- Users have one move per turn.
- User chooses a place on the board to place their coloured disk.
- If this move is deemed valid it moves onto the opponents turn.
- Game ends when two users pass in a row.
- User is notified of who won the game.
- User is returned to main menu.