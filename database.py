from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://dl1z7h9c1e1vywyzx8g1:pscale_pw_BkJK4K4jmn4ZzryGv0zkptnT3UscLAZxQQsi5aD2k2b@aws.connect.psdb.cloud/calebcareers?charset=utf8mb4"

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