# https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Iterate_over_a_SPARQL_query
# http://tinyurl.com/y9sybx3v
import pywikibot
from pywikibot import pagegenerators as pg

# wdt:P31 : instance of
# wd:Q6256 : country
# wdt:P300 : ISO 3166-2 code
query = """
SELECT ?item ?countryLabel ?official_name ?iso_code Where {
  ?item wdt:P31 wd:Q6256.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  OPTIONAL { ?item wdt:P1448 ?official_name }
  OPTIONAL { ?item wdt:P297 ?iso_code. }
}
GROUP BY ?iso_code

"""

site = pywikibot.Site("wikidata", "wikidata")
generator = pg.WikidataSPARQLPageGenerator(query, site=site)

for n, i in enumerate(generator):
    ii = i.get()
    print(ii.keys())
    print(ii['labels'])
    break
