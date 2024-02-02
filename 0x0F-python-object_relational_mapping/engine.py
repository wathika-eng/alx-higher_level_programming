#!/usr/bin/python3
"""Template for engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


class MainEngine:
    """Main class"""

    if len(sys.argv) != 4:
        sys.exit(1)
    else:
        user = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]
    main_engine = create_engine(
        f"mysql://{user}:{password}@localhost:3306/{db}", pool_pre_ping=True
    )

    Session = sessionmaker(bind=main_engine)
    session = Session()
