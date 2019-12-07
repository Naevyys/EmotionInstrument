# About

Contains the code for the final technical deliverable of Iris Kremer: a python program that adapts music played with QT according to the emotion of the person in front of it.

# Code information

## General algorithm

- Node emotionReader reads the facial expression of the user from the topic "qt_nuitrack_app/faces" and computes a shift for the notes according to the emotion detected
- On topic "/QTInstrument/emotion", the node emotionReades publishes the shift computed
- The node emotionConverter subscribes to the topic "/QTInstrument/emotion" to get the shift and to the topic "/QTInstrument/music" to get the note which should be played originally
- Using the ASCII number of the note, adding the shift and taking the modulo, the emotionConverter node will then compute the new note according to the emotion detected
- Finally, the emotionConverter node publishes the corresponding file to play to the topic "/QTrobot/audio/play"

### Notes shift

Written in the form [shift] / [octave].

- Neutral: 0 / C major
- Angry: 1 (test placeholder) 
- Happy: 2 (test placeholder)
- Surprised: 3 (test placeholder)

## To do

- Test border cases and octaves
- Import audio files in this repository to have everything at one place

## Current issues

None.

## Important notes

- I have to create a separate, more rudimentary music publisher in order to test my code and prove that this project is independent from Eliott's project
- It is impossible to adapt the music played such that it really matched the emotion of the user, because the program has no influence on the sequence of notes played by the musician, only on each individual note, which means I cannot make the musician play on a major or minor octave for instance.

# Resources and useful links

## Documentation

### ROS

- Tutorials: <http://wiki.ros.org/ROS/Tutorials>

## OpenCV

- Tutorials: <https://docs.opencv.org/master/d6/d00/tutorial_py_root.html>

### QT

#### General information

- <http://luxai.com/who-is-qtrobot-for-autism/>
- <http://luxai.com/qtrobot-for-research>

#### Sample code

- <https://github.com/luxai-qtrobot/tutorials> (*demos* and *examples* documents)

#### Documentation

- <http://wiki.ros.org/Robots/qtrobot>
- <https://robots.ros.org/qtrobot>

### Other

- BSP3 activity report: <https://docs.google.com/spreadsheets/d/1qnNxgRPuyIrlm4as1ygEL9L_l0cXcXdnA1QgmarJsdk/>
- Final report read-only link: <https://www.overleaf.com/read/bkndvbmrtryc>
- Markdown documentation: <https://www.markdownguide.org/basic-syntax/>
- Workshop info: <https://airobolab.uni.lu/Workshops/AIFA-2020>

## Research

### Similar projects

- <http://www.paulvangent.com/2016/06/30/making-an-emotion-aware-music-player/>

# Git commands from bash

All commands should work both in Linux Ubuntu bash and Windows command promt. To use a command, you must be located inside the repository.

**Clone repository**

    $ git clone REPOSITORYURL

**Change branch**

    $ git checkout YOUR-BRANCH

**Change username and email**

    $ git config [--global|--local] user.name "YOUR-USERNAME"
    $ git config [--global|--local] user.email "YOUR-EMAIL" 

**Push to github**

1. Stage files

        $ git add FILENAMES

2. Commit changes

        $ git commit -m "COMMIT MESSAGE"

3. Push to github

        $ git push origin YOUR-BRANCH

**Fetch**

    $ git fetch origin BRANCH

**Pull**

    $ git pull origin BRANCH

**Check status**

    $ git status

# Scientific part

## Explainable AI (XAI)

- <https://www.degruyter.com/downloadpdf/j/pjbr.2018.9.issue-1/pjbr-2018-0009/pjbr-2018-0009.pdf>

## Human-Robot Interaction (HRI)

### Emotions and affective robots

- <http://groups.csail.mit.edu/lbr/hrg/2001/ecal.pdf>
- <https://www.researchgate.net/profile/Frank_Kaptein/publication/322876575_The_role_of_emotion_in_self-explanations_by_cognitive_agents/links/5b110f64a6fdcc4611d9c546/The-role-of-emotion-in-self-explanations-by-cognitive-agents.pdf>
- <https://link.springer.com/chapter/10.1007/978-3-319-96722-6_6>
- <https://www.researchgate.net/profile/Malte_Jung/publication/334095719_Emotion_Expression_in_HRI_-When_and_Why/links/5d16411c299bf1547c86ee1e/Emotion-Expression-in-HRI-When-and-Why.pdf>
- <https://www.researchgate.net/profile/Eduard_Fosch_Villaronga/publication/335706066_I_Love_You_Said_the_Robot_Boundaries_of_the_Use_of_Emotions_in_Human-Robot_Interactions/links/5da9b56e299bf111d4be4e0f/I-Love-You-Said-the-Robot-Boundaries-of-the-Use-of-Emotions-in-Human-Robot-Interactions.pdf>
- <https://books.google.lu/books?hl=en&lr=&id=gQhFzMzW9fsC&oi=fnd&pg=PA1&dq=emotion+selection+in+evolution&ots=vZ6RNEmth3&sig=t_poUAWjTLZ3o6ueWLiQtFlaaL0&redir_esc=y#v=onepage&q=emotion%20selection%20in%20evolution&f=false>

## Robots and music

### Musician robots

- <http://magnus.ece.gatech.edu/Papers/Paper3.pdf>

### Music teacher robots

- <https://www.researchgate.net/profile/Ali_Meghdari/publication/308928265_Social_Robots_and_Teaching_Music_to_Autistic_Children_Myth_or_Reality/links/59cb13400f7e9bbfdc36bdeb/Social-Robots-and-Teaching-Music-to-Autistic-Children-Myth-or-Reality.pdf>
- <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.592.2947&rep=rep1&type=pdf>

