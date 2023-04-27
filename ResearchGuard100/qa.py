from mediawikiapi import MediaWikiAPI
import wikipediaapi
import os
from keywordExtracter import keywordExtracter

wiki_wiki = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI)

def getLinks(keyword):
    wiki_api = MediaWikiAPI()
    searchTerms = wiki_api.search(keyword, results=7)

    links = []
    for term in searchTerms:
        page = wiki_wiki.page(term)
        links.append(page.fullurl)

        references = getReferences(page)
        
        links += references
    
    return links


def getReferences(page):
    references_raw = page.links
    references = []
    for title in sorted(references_raw.keys()):
        references.append(references_raw[title])
    return references

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader

context = input("Please describe what you want to search about : ")
terms = keywordExtracter(context)

urls = []
for term in terms:
    urls += getLinks(term)

loader = UnstructuredURLLoader(urls=urls)
data = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)
embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

chain = RetrievalQAWithSourcesChain.from_chain_type(
    OpenAI(temperature=0), 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={"k": 1})
)

os.system("cls || clear")
print(f"Context Give: {context}")
print(f"Terms: {terms}")
print(f"Initial Search Links : {urls}")
print("\n")
print("---------------------")
print("\n")

status = True

while status:
    query = input("Query : ")

    if query == "exit()":
        status = False
        break

    res = chain({"question": query}, return_only_outputs=True)
    print(f"Answer: {res['answer']}")
    if "I don't know." not in res['answer']:
        print(f"Sources: {res['sources']}")