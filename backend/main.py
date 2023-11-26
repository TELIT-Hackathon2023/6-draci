from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain.evaluation import load_evaluator
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader, TextLoader
from sklearn.metrics.pairwise import cosine_similarity
import os
import nltk

openai_api_key = "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"
llm = OpenAI(openai_api_key=openai_api_key)

loaders = {
    "technical": TextLoader("dataset_technical.txt"),
    "functional": TextLoader("dataset_functional.txt"),
    "compliance": TextLoader("dataset_compliance.txt"),
    "domain": TextLoader("dataset_domain.txt"),
}

topic = ["technical"]

technical_query = f"Summarize how should RFP files must look like from functional point of view"
functinal_query = "Summarize how should RFP files must look like from technical point of view"
compliance_query = "Summarize how should RFP files must look like from compliance point of view"
domain_query = "Summarize how should RFP files must look like from domain point of view"

query_pdf = """Summarize how should RFP files must look like from function point of view", return as "F:"data",
Summarize how should RFP files must look like from technical point of view"return as "T:"data", """

query_summary = """Write summary about document using in these points
ROBLEM STATEMENT: A concise description of the issue or need that the RFP intends to address.
SCOPE OF THE WORK: The boundaries of the project, including what is to be accomplished and the expected deliverables.
REQUIRED TECHNOLOGY STACK: A list of the technology tools, frameworks, and languages that are necessary to complete the work.
PRICING MODEL: Details about how the costs of the work will be calculated and charged. T&M or Fixed Price.
SERVICE LEVEL AGREEMENTS (SLAS): The agreed levels of service performance and availability, as well as any penalties for non-
compliance.
SELECTION CRITERIA: The standards or requirements that proposals must meet to be considered for selection.
TIMELINES: Key dates and milestones for the RFP processing schedule.
CONTACT DETAILS: Information for the point of contact, such as name, address, phone number, and email.
PENALTY CLAUSES: Conditions under which penalties may be applied for failure to meet the terms of the contract.
REQUIRED OFFER TYPE (BINDING OR NON-BINDING): Whether the proposals are legally binding and the conditions under which they 
may be binding or no"""

loadUserData = PyPDFLoader("test.pdf")
loaderFolder = DirectoryLoader('./files', glob='**/*.txt')
template = """Only fill json  
Always say "thanks for asking!" at the end of the answer.
{context}
Question: {question}
Helpful Answer:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)


def compareEmbeddings(string1, string2):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    evaluator = load_evaluator("pairwise_embedding_distance", embeddings=embeddings)
    return evaluator.evaluate_string_pairs(
        prediction=string1, prediction_b=string2
    )


def embendingsCriteria(loader, query):
    data = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    docsearch = FAISS.from_documents(texts, embeddings)

    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(), chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

    result = qa.run(query)
    return result


def embendingsSummary(loader, query):
    data = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    docsearch = FAISS.from_documents(texts, embeddings)

    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(), chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

    result = qa.run(query)
    return result


# Example usage
string1 = embedCriteria(loaderFolder, technical_query)
string2 = embedCriteria(loadUserData, query_pdf)
print(string1)
print(compareEmbeddings(string1, string2))

