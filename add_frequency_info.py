from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import codecs
import re


levels={200:'very basic', #1-477                    = 500                          cum 500
    100:'basic',               #477-1016             = 500                          1000
    50:'very common',      #1017-2060           = 1000                        2000
    25:'common',               #2060-3760          = 1700                        3700
    13:'uncommon',           #3760-6313           = 2600                        6300
    7:'rare',                    #6300-10050         = 3750                        10000
    2:'very rare',           #10500-18600        = 8100                        18000
    0:'obscure'}              #18600-50000       = 31400                      50000
slevels=sorted(levels.items(),key=lambda x:x[0]*-1)
words=sorted([w.upper() for w in levels.values()],key=lambda x:-1*len(x))      

corpus_path='d:/proj/ankifreq/internet-zh.num'

if os.path.exists(corpus_path):
    blob=codecs.open(corpus_path,'r','utf8').read()
else:
    showInfo('you need to copy the internet-zh.num file to %s , or edit the source file to point to the file.'%corpus_path)

def lookup_frequency(hanzi):
    pat=re.compile('(.+ '+hanzi+')\n')
    try:
        res=pat.findall(blob)[0]
    except Exception,e:
        #~ showInfo('%s%s'%(repr(e),hanzi))
        #word did not exist in dict.
        return False
    description=''
    frequency_html=''
    if res and type(res)!=tuple:
        order,permillion,chars=res.split()
        permillion=float(permillion)
        try:
            for num,name in slevels:
                if permillion>num: 
                    description=name.upper()
                    frequency_html='<div class="frequency-note frequency-%s">%s</div>'%(name.replace(' ','-'), name)
                    break
        except Exception,e:
            #~ showInfo(repr(e))
            return False
    else:
        description=''
        permillion=''
        frequency_html='<div class="frequency-note frequency-unknown">unknown</div>'
    return (permillion,frequency_html)



def add_frequency_info():
    
    cardCount = mw.col.cardCount()
    ii=0
    #~ cards=mw.col.findCards('deck:"other"')
    cards=mw.col.findCards('')
    showInfo('got %s cards.  it will take about 1 second for every 10 cards; just let it run.'%str(len(cards)))
    has_shown=False
    editcount=0
    for id in cards:
        card=mw.col.getCard(id)
        note = card.note()
        hanzi=None
        changed_this=False
        if 'permillion' not in note or 'frequency_html' not in note:
            if not has_shown:
                showInfo('you need to add the permillion and frequency_html field to one of your decks. %s'+repr(note.items()))
                has_shown=True
            continue
        hanzi=note['Hanzi']
        if hanzi:
            res=lookup_frequency(hanzi)
            if res:
                permillion,frequency_html=res
                permillion=str(permillion)
                editcount+=1
                note['permillion'] = permillion
                note['frequency_html']=frequency_html
        ii+=1
        note.flush()
            
    showInfo('changed %d cards.'%editcount)
    
action = QAction("fill in card info", mw)
mw.connect(action, SIGNAL("triggered()"), add_frequency_info)
mw.form.menuTools.addAction(action)