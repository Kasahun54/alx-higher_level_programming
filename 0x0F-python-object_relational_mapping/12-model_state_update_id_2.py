#!/usr/bin/python3
"""
uses sqlalchemy to list state
"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    
    session.commit()
    session.close()
