'''
    urllib is a package that have several modules to work with url's
        request is a module of urllib
        url open is a function of request
        we can use it in the python command prompt
    step 1:- scrap the data
    step 2:- parse the data (HTML Data)
    step 3:- display/save the data

    >>> from urllib.request import urlopen as ureq
>>> from bs4 import BeautifulSoup as soup
>>> quotespage = 'https://bluelimelearning.github.io/my-fav-quotes/'
>>> uclient = ureq(quotespage)
>>> pagehtml = uclient.read()
>>> uclient.close()
>>> page = soup(pagehtml,"html.parser")
>>> quotes = page.findAll("div",{"class":"quotes"})
>>> len(quotes)
19
>>> quotes[1]
<div class="quotes">
<p class="aquote">
                    Feeling gratitude and not<br/> expressing it is like wrapping<br/> a present and not giving it.
                </p>
<p class="author">
                    William Arthur Ward
                </p>
</div>
>>> quotes[1].text.strip()
'Feeling gratitude and not expressing it is like wrapping a present and not giving it.\n                \n\n                    William Arthur Ward'
>>> page.h1
<h1>Words of Wisdom</h1>
>>> page.h1.text.strip()
'Words of Wisdom'

>>> favquo = page.findAll("p",{"class":"aquote"})
>>> favauth = page.findAll("p",{"class":"author"})
>>> print("author :",favauth[0],"\n Quote :",favquo[0])
author : <p class="author">
                Confucious
            </p>
 Quote : <p class="aquote">
                I hear and i forget.<br/> I see and i remember.<br/> I do and i understand.
            </p>

>>> print(" Author :",favauth[0].text.strip(),"\n Quote :",favquo[0].text.strip())
 Author : Confucious
 Quote : I hear and i forget. I see and i remember. I do and i understand.
'''