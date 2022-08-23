from main import db


class SkillUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name