# tetris-mc

<img width="832" alt="Screenshot 2024-12-09 at 17 12 49" src="https://github.com/user-attachments/assets/d904354f-c629-453d-85cd-3f7886a24ef1">

Simple Tetris clone made as part of the Mastercamp IT program in 2023 at [Efrei Paris](https://eng.efrei.fr/).

---

# How to run

1. Clone the repository locally using `git clone`.
2. Move to the folder containing the project in your terminal.
3. Install the required libraries with `pip install -r requirements.txt`.
4. Start the game with `python main.py`.

# How to play

The game features several game modes:

- Classic: Each new tetromino and line removed gives you points. Try to get the highest score among your friends but be careful because as your score gets higher, so does the speed of the tetrominos!
- Time Trials: Try to get the highest score in only 60 seconds!
- Challenges: Try to complete challenges while playing, like removing four lines or scoring 300 points in a single move.

Press `Up Arrow` to rotate the tetromino. 
Press `Left Arrow` to move it to the left, or `Right Arrow` to move it to the right. Press `Down Arrow` to move it directly to the bottom. 

Press `Escape` to bring up the pause menu. From there, you can save your game (you'll be able to load it from the main menu) or quit. Be careful, you can only have a single save at a time!

Good luck and have fun!

# How it works

This project was coded in **Python** and uses **PyGame** as a rendering library and **NumPy** to handle the tetronimos and move/rotate them.
