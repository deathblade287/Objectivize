from mediawikiapi import MediaWikiAPI
# mediawikiapi = MediaWikiAPI()

# results = mediawikiapi.search("Barack")
# print(results)

# page = mediawikiapi.page(results[0])
# print(page.title)
# print(page.url)


def getLinks(keyword):
    mediawikiapi = MediaWikiAPI()
    searchTerms = mediawikiapi.search("Barack")
    print(searchTerms[1])

    links = []
    for term in searchTerms:
        page = mediawikiapi.page(term)
        links.append(page.url)
    
    return links

print(getLinks("Barack"))