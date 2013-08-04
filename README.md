anki-chinese-word-frequency
===========================

Add bulk word frequency information to your anki chinese decks, based on an internet chinese word usage corpus

Why
------------
When I read a random article and find new words I don't know, sometimes they are really common, useful words.  Other times they are incredibly obscure.  I have no way to know at the time, and memorize them all.  Then I'm in the weird situation of knowing an extremely literary, weird way to say something, but not knowing the normal way.

The other problem is that you are very rarely going to run into a rare word again, so it won't get reinforced much, and you'll probably forget it.

So overall, it's almost always better to study words that are common!


Screenshots
-----------------

![ScreenShot](https://raw.github.com/ernop/anki-chinese-word-frequency/master/verybasic.png)

![ScreenShot](https://raw.github.com/ernop/anki-chinese-word-frequency/master/common.png)

![ScreenShot](https://raw.github.com/ernop/anki-chinese-word-frequency/master/obscure.png)

How
-------------
This will go through the decks you have now and fill in two new fields, permillion (frequency of this word appearing per million words in a chinese internet corpus), and frequency_html which is just text describing how frequent the word is from:

-very basic (1st 500 words)
-basic (500-1000)
-very common (1000-200)
-common (2000-3700)
-uncommon (3700-6300)
-rare (6300-10500)
-very rare (10500-18600)
-obscure (18600-50000)

Most articles *will* have obscure words in them, which is annoying - but they will always be different obscure words, so it will take years of memorizing before you can reliably know them.



How to set up 
---------------------------------

WARNING:: ALPHA CODE, DEFINITELY BACK UP YOUR DECKS; this has a nonzero chance of destroying your work.    ALSO, TRY IT FOR JUST ONE DECK FIRST!
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. DISABLE AUTO SYNC! in case you mess up the deck

2. Back up your decks

3. Add two fields to the deck you want: 

-permillion (word appearances per million words in the internet corpus)

-frequency_html (description of this rareness (looking at raw numbers is too distracting))

4. Put internet-zh.num in the same folder (or somewhere else and edit the code to point to it)

5. Put the test_addon.py file in the root of your addons directory, which on windows is at something like "c:/users/<your username>/my docs/Anki/addons"

6. Modify the code line cards=mw.col.findCards('"deck:other"') to choose which cards you want to modify.  Changing it to just mw.col.findCards('') will do them all.

7. Restart anki

8. In the tools dropdown there is an option "fill in card frequency info" which will start the process

9. Running it again will do all the work again, replacing old permillion & frequency_html fields, in case you want to modify the descriptions, etc.  You need to restart anki every time you change the script.

10. Search in the search box for "obscure" to find those super rare (less than 2/million occurances) words; decide if you really want to spend time learning them.





