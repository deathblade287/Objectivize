#### FAILED ####

import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI)


references = []

def append_titles(categorymembers, level=0, max_level=1):
    global references
    for c in categorymembers.values():
        references.append(c.title)
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            append_titles(c.categorymembers, level=level + 1, max_level=max_level)

cat = wiki_wiki.page("Category:Physics")
# print("Category members: Category:Physics")
append_titles(cat.categorymembers)
print(references)
