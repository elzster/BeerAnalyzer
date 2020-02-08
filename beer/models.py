from .app import db

class beerdata(db.Model):
    __tablename__ = 'brew_data'

    id = db.Column(db.Integer, primary_key=True)
    brewery_id = db.Column(db.Text)
    brewery_name = db.Column(db.Text)
    review_time = db.Column(db.Text)
    review_overall = db.Column(db.Float)
    review_aroma = db.Column(db.Float)
    review_appearance = db.Column(db.Text)
    review_profilename = db.Column(db.Text)
    beer_style = db.Column(db.Text)
    review_palate = db.Column(db.Float)
    review_taste = db.Column(db.Float)
    beer_name = db.Column(db.Text)
    beer_abv = db.Column(db.Float)
    beer_beerid = db.Column(db.Text)
    
def __repr__(self):
    return '<Crash %r>' % (self.name)

