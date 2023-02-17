# Coldbrew-Coders Discord Bots


# Product Vision Statement
Discord is an online Voice-over-Internet-Protocol(VoIP) and messaging application. In addition to messaging capabilities, Discord offers support for "bots", programmable robotic users that can interact with human users. These bots are capable of a plethora of interactive actions. For example, a Discord bot can help with the governance of a Discord server, relay real time sports game data, and even play music within a voice channel. 
The goal of our project is to design and build a Discord bot that can do many actionable tasks that are useful, intuitive, and entertaining to any Discord user. This project will be a backend-intensive undertaking and will have the frontend development abstracted away using a Discord developer account, which allows developers to test backend code with Discord's user interface. We will also have a custom API server connected to a front-end displaying information and biographical details about the bots.


# About Us
 ## Shashanka Sharma
https://github.com/Shashanka-Sharma

## Ty Arpornsuksant
https://github.com/Tyarporn

## Cameron Vong
https://github.com/cameronvong

## Tahmeed Chowdhury
https://github.com/chowdhurytahmeed



# Product History 
The purpose of our project is to build a Discord bot using the tech stack mentioned in class. 
We will be using Python with Discord's Python library ```discord.py``` which contains extensive implementations for Discord's API in a pythonic way for the backend of the project, Heroku for cloud deployment, Github / Github Actions for version control, and Discord's API in order to interact with the Discord UI. In addition to the available libraries for python and discord, there is a flask module specifically designed for discord called ```flask_discord_interactions``` which enables the efficient use of flask as our routing framework. Furthermore, if we wish for the project to use a database, we can collect user data through the bot, store it in a database, and fetch the data for use in the application.

We are all interested in using this technology as we all share a common interest in gaming and the constant rise in use cases for Discord, and as a close derivative, Slack. By developing our skills in our product stack, we will not only learn skills to build for Discord, but apps that target other fields as well.



# Building and Testing The Project
## Initial Setup (API Server)
1. Clone the repository onto your local machine with ```https://github.com/Tyarporn/coldbrew-coders```.
2. Create a new terminal shell
3. Navigate to server with ```cd back-end/server``` and run local.sh using ```./local.sh```.
4. Open ```http://52.72.178.160:8080``` on a web browser of your choice.

## Front-End Setup (React Server)
1. Create a new terminal shell.
2. Navigate to front-end directory with ```cd front-end```
3. Run npm install
4. Run npm start

## Bot Setup
1. Navigate to the respective group member's name.
2. Create a ```.env``` within that directory.
3. Define ```DISCORD_TOKEN``` variable in the .env file and set it to the discord token for the bot, accessed from the discord developer portal.
4. Define ```DISCORD_GUILD``` in the .env file, which is the name of the discord server you wish to add the bot to. Ensure you have proper permissions to add users to your chosen discord server.
5. Run the respective python script for the bot. Example: Run ```shank-bot.py``` under ```shashanka-testing``` directory. 
6. Ensure you have a discord user exist in the same server as the bot and use the Discord UI to communicate with the bot using commands.
## Testing Backend Routes
1. Navigate to the master directory with the ```makefile``` within that directory.
2. Run ```export PYTHONPATH=<project directory path>/back-end:<project directory path>/back-end/db:$PYTHONPATH``` to set the python path locally. 
3. Run ```make all_tests```.



# Tech Stack
Main Language: Python 3.9 or greater

OS: UNIX-like (MacOS, Linux, Windows Subsystem for Linux, etc.)

Testing: pytest

API server: flask and flask-restx

Finance API: YFinance - Yahoo Finance
News and Reviews API: NYT - New York Times

Database: MongoDB

Build: make

Lint: flake8

CI/CD: GitHub Actions

Cloud deployment: AWS EC2 (Server) 

Bot Frontend: Discord UI 

Web Frontend: React JS

Project management: Kanban board on GitHub
