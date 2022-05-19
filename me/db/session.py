from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from me.core.settings import settings

engine = create_engine(url = settings.pg_dsn, pool_pre_ping = True)
LocalSession: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)