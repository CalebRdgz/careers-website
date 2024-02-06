from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")

db_connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASS}@aws.connect.psdb.cloud/calebcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ca": "/etc/ssl/cert.pem",
                           }
                       })

#get some information out of the engine
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.mappings().all():
            jobs.append(dict(row))
        return jobs