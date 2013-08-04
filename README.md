anki-chinese-word-frequency
===========================

Bulk add word frequency information to your anki chinese decks, based on an internet chinese word usage corpus

Shots
-----------------

![ScreenShot](https://raw.github.com/ernop/anki-chinese-word-frequency/master/verybasic.png)

![ScreenShot](https://raw.github.com/ernop/anki-chinese-word-frequency/master/common.png)

![ScreenShot](https://raw.github.com/ernop/anki-chinese-word-frequency/master/obscure.png)


How to set up 
---------------------------------

0. DISABLE AUTO SYNC! in case you mess up the deck

1. . add two fields to the deck you want: 
-permillion (word appearances per million words in the internet corpus)
-frequency_html (description of this rareness (looking at raw numbers is too distracting))

2. put internet-zh.num in the same folder (or somewhere else and edit the code to point to it)

3. put the test_addon.py file in the root of your addons directory, which on windows is at something like "c:/users/<your username>/my docs/Anki/addons"

4. modify the code line cards=mw.col.findCards('"deck:other"') to choose which cards you want to modify.  Changing it to just mw.col.findCards('') will do them all.

5. restart anki

6. WARNING:: ALPHA CODE, DEFINITELY BACK UP YOUR DECKS; this has a nonzero chance of destroying your work.  

ALSO, TRY IT FOR JUST ONE DECK FIRST!

7. in the tools dropdown there is an option "fill in card frequency info" which will do the work.

8. Running it again will do all the work again, replacing old permillion & frequency_html fields, in case you want to modify the descriptions, etc.  You need to restart anki every time you change the script.

9. search in the search box for "obscure" to find those super rare (less than 2/million occurances) words; decide if you really want to spend time learning them.





