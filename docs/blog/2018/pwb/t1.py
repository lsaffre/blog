import pywikibot

site = pywikibot.Site('en', 'wikipedia')
page = pywikibot.Page(site, 'User:LucSaffre/sandbox')
page.text = page.text.replace('foo', 'bar')
page.save('Replaced foo by bar')  # Saves the page using the given summary
