from langchain import OpenAI, SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
AWS_DB_URL = os.environ.get('AWS_DB_URL')
AWSOF_DB_PASSWORD = os.environ.get('AWSOF_DB_PASSWORD')

db = SQLDatabase.from_uri(f"mysql+pymysql://admin:{AWSOF_DB_PASSWORD}@{AWS_DB_URL}/ofandb")
llm = OpenAI(temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

# db_chain.run('Cuanto hay en existencias del modelo TPGW9250 en la tienda 1211 Palmas en total')

# db_chain.run('Cual es el costo del modelo TPGW9250')

# db_chain.run('Que tienda vende mas el modelo TPGW9250')

db_chain.run('Cuales son los modelos mas vendidos en el ultimo mes?')





