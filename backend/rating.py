from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import pandas as pd
import json

openai_api_key = "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"
chat_model = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, max_tokens=1000)

response_schemas = [
    ResponseSchema(name="input_industry", description="This is the input_industry from the user"),
    ResponseSchema(name="standardized_industry", description="This is the industry you feel is most closely matched to the users input"),
    ResponseSchema(name="match_score",  description="A score 0-100 of how close you think the match is between user input and your match")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()
print (output_parser.get_format_instructions())

template = """
You will be given a series of industry names from a user.
Find the best corresponding match on the list of standardized names.
The closest match will be the one with the closest semantic meaning. Not just string similarity.

{format_instructions}

Wrap your final output with closed and open brackets (a list of json objects)

input_industry INPUT:
{user_industries}

STANDARDIZED INDUSTRIES:
{standardized_industries}

YOUR RESPONSE:
"""

prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template(template)
    ],
    input_variables=["user_industries", "standardized_industries"],
    partial_variables={"format_instructions": format_instructions}
)

standardized_industries='Corporate Services, Recreation & Travel, Legal, Wellness & Fitness, Entertainment, Consumer Goods, Design, Arts, Manufacturing, Finance, Health Care, Construction, Nonprofit, Real Estate, Software & IT Services, Hardware & Networking, Agriculture, Education, Public Administration, Transportation & Logistics, Public Safety, Media & Communications, Energy & Mining, Retail'

user_input = "lietadla ktore lietaju do USA a Europy, aquapark,lunapark, aviation, planes that fly, farming, bread, wifi networks, twitter media agency"

_input = prompt.format_prompt(user_industries=user_input, standardized_industries=standardized_industries)


output = chat_model(_input.to_messages())

print (type(output))
print (output.content)

