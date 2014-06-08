### TwitterBot
[@MacroEconBot](https://twitter.com/MacroEconBot)

==========
#### About
This is a Twitter bot/page-scraper that I wrote to notify Macroeconomics students at my university (through Twitter) when they sold out their goods on the [Virtual Macroeconomy](http://macro.exeter.ac.uk/macro/site/login).

#### What's Virtual Macroeconomy
[Virtual Macroeconomy](http://macro.exeter.ac.uk/macro/site/login) was a game/simulator of a small economy run by our Macroeconomics professor. Throughout the whole semester students had to trade and buy as many goods as possible between each other everyday between 9am and 6pm. The amount a student sold over the course of several weeks would translate into actual grades (max %5 out of total module grade ). The rule was that you could only post on sale 10 items at a time no more than 25 times a day, so knowing when you sold out as soon as it happened allowed you to quickly post more items and ensure that you always had stuff on sale in the economy. The point of the whole game was to generate tons of data and demonstrate student ideas behind [Modigliani–Miller theorem](http://en.wikipedia.org/wiki/Modigliani%E2%80%93Miller_theorem).

#### How it works
The way the bot works is it logs in for each student into the [Virtual Macroeconomy](http://macro.exeter.ac.uk/macro/site/login), checks if that student sold anything since the last login, if he did, it sends that student a tweet with his current stock levels.

#### History
The bot worked for about a week notifying me and several other students. Unfortunately, soon after the professor behind the website detected tons of traffic from our accounts and almost disqualified us from the game. Fortunately, we worked it out and I was even offered to integrate the Twitter notifications into the simulator itself.
