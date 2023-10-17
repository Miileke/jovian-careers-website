from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))        
    jobs = []
    for row in result.all():
      result_dict = row._asdict()             
      jobs.append(result_dict)
    return jobs
    
    
  
  



