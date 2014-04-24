### TwitterBot ([@MacroEconBot](https://twitter.com/MacroEconBot))
==========
#### About
This is a Twitter bot/page-scraper that I wrote to notify Macroeconomics students (through Twitter) when they sold out their stock on the Virtual Macroeconomy.

#### What's Virtual Macroeconomy
Virtual Macroeconomy was a simulation of a small economy where students had to trade and buy as many goods as possible between each other everyday between 9am and 6pm. The amount a student sold over the course of several weeks would translate into actual grades (max %5 out of total module grade ). The rule was that you could only post 10 items for sale at a time no more than 25 times a day, so knowing when you sold out as soon as it happened allowed you to quickly post more items and ensure that you always had stuff on sale in the economy.

#### How it works
The way the bot works is it logs in for each student into the [Virtual Macroeconomy](http://macro.exeter.ac.uk/macro/site/login), checks if that student sold anything since the last login, if he did, it sends that student a tweet with his current situation.

#### History
The bot worked for about a week tweeting notifications to me and several other students before the professor behind the website detected tons of traffic from our accounts and almost disqualified us from the game. Fortunately, we worked it out and I was even offered to integrate the Twitter notifications into the simulator itself.
