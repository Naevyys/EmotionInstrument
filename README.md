# User guide

This is a short user guide explaining how to run the code successfully. It was written such that absolutely (hopefully) everyone knowing what a terminal is can understand it.

## Prerequisites

- This code was made to run on QTrobot only, it does not work on any other robot or computer.
- To run correctly, we need both computers of QT working (QTPC and QT132/QT110 depending on which QT you run the code) and have the bi-directional connection between them enabled.

From here on, we will assume that you are using the most recent version of QT, which has the computers QTPC and QT132 [07/12/2019]. However, the tutorial should work for the previous version of QT (with computers QTPC and QT110) too.

## Clone repository and setup

1. Open a terminal on QTPC (T1)
2. Clone this repository anywhere convenient on QTPC. The exact location of the code does not matter.
3. If not already there, change directory to the folder containing the cloned repository named EmotionInstrument (but not inside the repository)
4. Copy the entire repository into any remote directory on QT132 using the command

        $ scp -r EmotionInstrument qtrobot@192.168.100.1:/remote/directory/

5. Open a second terminal (T2) on QTPC and ssh to QT132 using the command

        $ ssh qtrobot@192.168.100.1

6. In T2, change directory to the home directory of QT132
7. Move the entire Octaves folder from the EmotionInstrument repository to robot/data/audios using the command

        $ mv /remote/directory/EmotionInstrument/Octaves /robot/data/audios

8. In T1, change directory to the repository EmotionInstrument
9. In T2, change directory to the repository EmotionInstrument
10. Open a third terminal (T3) on QTPC and run the following command to make QTPC run on the ROS master of QT132 (This is necessary to enable the nodes on the different computers to publish on and subscribe to the same topics)

        $ export ROS_MASTER_URI=http://qtrobot@192.168.100.1:11311

11. In T3, change directory to the repository EmotionInstrument

You are now setup to run the code.

## Running the code

1. In T1, run the following command to start the musicPub node

        $ python musicPub.py

2. In T2, run the following command to start the emotionConverter node (remember that T2 is currently in QT132, which is very important). After running this command, QT should start playing the same note over and over

        $ python emotionConverter.py

3. In T3, run the following command to start the emotionReader node

        $ python emotionReader.py


Now stand up and go or put someone else in front of QT. When the person in front of QT changes his or her facial expression (neutral, angry, happy or surprised), the note played by QT will change according to the emotion detected.

## Running the code together with another program

Instead of using the provided, boring musicPub node, the code can work with another program which was written to use QT as an instrument.

From now on, we will call the entire other program QTInstrumentProgram.

### Prerequisites

QTInstrumentProgram needs to meet some (very few) criteria in order to work well with the code provided here:

- QTInstrumentProgram publishes individual notes as data of type Int16, in the format ONN, where 3 <= O <= 5 (octave between 3 and 5) and 01 <= NN <= 12 (note between 1 and 12, where 1 = C and 12 = B (e.g. 7 = F# = Gb)) to the topic /QTInstrument/music
- The advised maximal rate of publishing is around 2.5 - 2.6 publications per second
- QTInstrumentProgram does not publish audio files to play to the topic /qt_robot/audio/play by itself

### How to run the programs together

1. Close T3, we don't need it anymore
2. Start QTInstrumentProgram in a/some new terminal/s
3. In T2, run the following command to start the emotionConverter node (remember that T2 is in QT132). After running this command, if someone plays music with QT, QT should emit the normal notes played by the player

        $ python emotionConverter.py

4. In T1, run the following command to start the emotionReader node

        $ python emotionReader.py

Now, the notes played by the player in front of QT will be shifted according to his or her facial expression.

