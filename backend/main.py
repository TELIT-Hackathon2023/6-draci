from langchain.llms import  OpenAI
from   langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import  pinecone
loader = PyPDFLoader("test.pdf")
key = ""
data=loader.load()

llm = OpenAI(temperature=0.9,openai_api_key=key)
chain = load_qa_chain(llm,chain_type="stuff")
text_spliter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
texts = text_spliter.split_documents(data)

pinecone.init(
    api_key="",
    environment="gcp-starter"

)
query = "which attachment is Score Summary Matrix "
emb = OpenAIEmbeddings(openai_api_key=key)
docsearch = Pinecone.from_texts([t.page_content for t in texts],emb,index_name="copilot1")
docs = docsearch.similarity_search(query)
##print(texts[1])
print(chain.run(input_documents=docs,question=query))

##print(docs[0])


