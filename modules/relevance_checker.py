# NEW (current)
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config.settings import OPENAI_API_KEY

def get_relevance_chain():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)

    template = """
    You are an AI recruiter. Compare the following Job Description (JD) and Resume.
    Give:
    1. Relevance Score (0-100)
    2. Matched Skills
    3. Missing Skills
    4. Short Summary

    JD:
    {jd}

    Resume:
    {resume}
    """

    prompt = PromptTemplate.from_template(template)
    return LLMChain(llm=llm, prompt=prompt)

def check_relevance(jd_text, resume_text):
    chain = get_relevance_chain()
    return chain.run(jd=jd_text, resume=resume_text)
