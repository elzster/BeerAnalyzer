from .app import db

class database(db.Model):
    __tablename__ = 'beer'

    id = db.Column(db.serial, primary_key=True)
    brewery_id = db.Column(db.varchar)
    brewery_name = db.Column(db.varchar)
    review_time = db.Column(db.timestamp)
    review_overall = db.Column(db.double_precision)
    review_aroma = db.Column(db.varchar)
    review_appearance = db.Column(db.varchar)
    review_profilename = db.Column(db.varchar)
    beer_style = db.Column(db.varchar)
    review_palate = db.Column(db.varchar)
    review_taste = db.Column(db.varchar)
    beer_name = db.Column(db.varchar)
    beer_abv = db.Column(db.double_precision)
    beer_beerid = db.Column(db.varchar)
    
def __repr__(self):
    return '<Crash %r>' % (self.name)

