from pprint import pprint
import pywikibot
site = pywikibot.Site('en', 'wikipedia')  # The site we want to run our bot on
if False:  # works
    page = pywikibot.Page(site, 'User:LucSaffre/sandbox')
    page.text = page.text.replace('foo', 'bar')
    page.save('kkk')  # Saves the page

# compare https://www.wikidata.org/wiki/Q3462598    
page = pywikibot.Page(site, "Vana-Vigala")
item = pywikibot.ItemPage.fromPage(page)
#print(item.get()['sitelinks'])
claims = item.get()['claims']
for k in claims.keys():
    print(k, claims[k])
    break

