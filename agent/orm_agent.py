from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_type = Column(String(50), nullable=False)
    transaction_date = Column(Date, nullable=False)
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(100), nullable=True)


class FinancialORMAgent:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_engine(database_url, echo=False, future=True)

    def create_schema(self):
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return Session(self.engine)

    def add_transaction(self, transaction_data: dict):
        with self.get_session() as session:
            transaction = Transaction(**transaction_data)
            session.add(transaction)
            session.commit()
            return transaction

    def list_transactions(self):
        with self.get_session() as session:
            return session.query(Transaction).all()
