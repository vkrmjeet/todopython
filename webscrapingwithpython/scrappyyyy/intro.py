'''
     first your have to install scrappy on your machine or environment
     pip install scrappy if you have pip
     or for conda
     conda install -c conda-forge scrapy


     then you have to create a project for your application
     scrapy startproject project_name

     components of scrappy project
     scrapy.cfg is a configuration file which you can edit if you want any specific configuration
     project_name folder contains all the file
     init.py is required to treat directories as containing python package .
     valid modules are hidden.
     it can also be empty.
     it is there to mock disk in the computer as python packages.

     items.py are used to populate script data , it is the container of script data i.e website data.
     middleware.py : it is a framework of hooks or middleware which allows to include custom functionalities
     that can be used to process request or items that are generated from the spider.
     it allows a bunch of isolated system or functionality to contact each other. fr ex payment system and python app,

     pipelines is used to processing items that are processed by spider
     it is used to cleansing the data, then validate and store it in a item or a database.

     settings.py it is the setting for the project , which can be modified.

     spiders are used to provide certain services



E:\courses\python\webscrapingwithpython\scrappyyyy\webscrap>Scrapy shell "https://bluelimelearning.github.io/my-fav-quotes/"
2022-03-07 12:31:53 [scrapy.utils.log] INFO: Scrapy 2.4.1 started (bot: webscrap)
2022-03-07 12:31:53 [scrapy.utils.log] INFO: Versions: lxml 4.8.0.0, libxml2 2.9.12, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 22.2.0, Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)], pyOpenSSL 21.0.0 (OpenSSL 1.1.1l  24 Aug 2021), cryptography 36.0.0, Platform Windows-10-10.0.19042-SP0
2022-03-07 12:31:53 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2022-03-07 12:31:53 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'webscrap',
 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
 'LOGSTATS_INTERVAL': 0,
 'NEWSPIDER_MODULE': 'webscrap.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['webscrap.spiders']}
2022-03-07 12:31:53 [scrapy.extensions.telnet] INFO: Telnet Password: 1b6a10b1e3000bf4
2022-03-07 12:31:53 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole']
2022-03-07 12:31:53 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2022-03-07 12:31:53 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2022-03-07 12:31:53 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2022-03-07 12:31:53 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2022-03-07 12:31:53 [scrapy.core.engine] INFO: Spider opened
2022-03-07 12:31:56 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://bluelimelearning.github.io/robots.txt> (referer: None)
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 5 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 10 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 17 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 19 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 20 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 22 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 23 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 25 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 26 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 28 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 29 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 30 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 31 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 32 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 33 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 34 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 35 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 39 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 44 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 45 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 46 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 60 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 66 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 67 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 71 without any user agent to enforce it on.
2022-03-07 12:31:56 [protego] DEBUG: Rule at line 75 without any user agent to enforce it on.
2022-03-07 12:31:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://bluelimelearning.github.io/my-fav-quotes/> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x0000015F5B9672B0>
[s]   item       {}
[s]   request    <GET https://bluelimelearning.github.io/my-fav-quotes/>
[s]   response   <200 https://bluelimelearning.github.io/my-fav-quotes/>
[s]   settings   <scrapy.settings.Settings object at 0x0000015F5B967460>
[s]   spider     <DefaultSpider 'default' at 0x15f5be90100>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>My Favorite Quotes</title>\n   ...'>]
>>> response.css('div.quotes')
[<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n            <p c...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quotes ')]" data='<div class="quotes">\n                ...'>]
>>> response.css('title::text')
[<Selector xpath='descendant-or-self::title/text()' data='My Favorite Quotes'>]
>>> response.css('title::text').extract()
['My Favorite Quotes']
>>> response.css('div.quotes::text').extract()
['\n            ', '\n            ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ', '\n                ', '\n                ', '\n        ']
>>> response.css('h1')
[<Selector xpath='descendant-or-self::h1' data='<h1>Words of Wisdom</h1>\n      <div i...'>]
>>> response.css('h1::text').extract()
['Words of Wisdom']
>>>



>>> quote = response.css('div.quotes')[0]
>>> aquote = quote.css("p.aquote::text").extract()
>>> print(aquote)
['\n                I hear and i forget.', ' I see and i remember.', ' I do and i understand.\n            ']

'''