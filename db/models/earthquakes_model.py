from sqlalchemy import Column, Integer, String
from .declarative_base import Base

class Earthquakes(Base):
    __tablename__ = 'triggered_earthquakes'
    id = Column(Integer, primary_key = True)

    lat = Column(String)
    long = Column(String)
    pga = Column(String)
    pgv = Column(String)
    magnitude = Column(String)

    def __repr__(self):
        return "<Sample(id='{}', lat='{}', long='{}', pga='{}', pgv='{}', magnitude='{}')>".format(
            self.id,
            self.lat,
            self.long,
            self.pga,
            self.pgv,
            self.magnitude
        )
        