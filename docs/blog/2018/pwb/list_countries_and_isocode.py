# started on 20180723, continued 20181109
# https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Iterate_over_a_SPARQL_query
# https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Big_Data
# http://tinyurl.com/y9sybx3v
# https://janakiev.com/blog/wikidata-mayors/
import pywikibot
from pywikibot import pagegenerators as pg

# wdt:P31 : instance of
# wd:Q6256 : country
# wdt:P300 : ISO 3166-2 code
# wdt:P297 ?ISO_3166_1_alpha_2_code  https://www.wikidata.org/wiki/Property:P297
query = """
SELECT ?item ?countryLabel ?official_name ?iso_code Where {
  ?item wdt:P31 wd:Q6256.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  OPTIONAL { ?item wdt:P1448 ?official_name }
  OPTIONAL { ?item wdt:P297 ?iso_code. }
}
GROUP BY ?iso_code

"""

query = """
SELECT ?item ?official_name ?ISO_3166_1_alpha_2_code WHERE {
  SERVICE wikibase:label { 
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  ?item wdt:P31 wd:Q6256.
  OPTIONAL { ?item wdt:P1448 ?official_name. }
  OPTIONAL { ?item wdt:P297 ?ISO_3166_1_alpha_2_code. }
}
LIMIT 1000"""

site = pywikibot.Site("wikidata", "wikidata")
generator = pg.WikidataSPARQLPageGenerator(query, site=site)

for n, i in enumerate(generator):
    # print(i.title())
    ii = i.get()
    print(ii.keys())
    # ['aliases', 'labels', 'descriptions', 'claims', 'sitelinks']
    #print("{} {}".format(i, ii['labels']['en']))
    # print(ii['claims'].keys())
    p = ii['claims'].get("P1448")
    claims = ii['claims'].get("P297")
    if claims is not None:
        assert len(claims) == 1
        iso_code = claims[0]
        # iso_code = iso_code['datavalue']
        # print(ii['descriptions'])
        label_en = ii['labels']['en']
        print("{} {}".format(iso_code, label_en))
        #help(iso_code)
        # help(p)
        break
