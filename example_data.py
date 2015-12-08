from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="User One", email="test@udacity.com")
session.add(User1)
session.commit()

# Create Category
soccer = Category(user_id=1, name="Soccer")
session.add(soccer)
session.commit()

# Create Catagory Item
jersey = CategoryItem(user_id=1, name="Jersey", description="Red Number 0 Soccer Jersey", category=soccer)
session.add(jersey)
session.commit()

print "added catalog items!"
