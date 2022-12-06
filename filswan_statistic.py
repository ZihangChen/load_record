from sqlalchemy import Column, Integer

from db import Base

class FilswanStatistic(Base):
    """ Model use to store swan stats """
    __tablename__ = "filswan_statistic"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    updated_at = Column(Integer, nullable=False, default=0)
    sp_quantity = Column(Integer, nullable=False, default=0)
    active_sp_quantity = Column(Integer, nullable=False, default=0)
    total_cid = Column(Integer, nullable=False, default=0)
    active_storage_deals = Column(Integer, nullable=False, default=0)
    daily_upload = Column(Integer, nullable=False, default=0)
    total_upload = Column(Integer, nullable=False, default=0)
    total_sealed_storage = Column(Integer, nullable=False, default=0)
    miners_receiving_deals = Column(Integer, nullable=False, default=0)
    data_transfered = Column(Integer, nullable=False, default=0)
    daily_sealed_deals = Column(Integer, nullable=False, default=0)