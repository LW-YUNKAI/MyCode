from app import db
from app.models import User


# ===============================================================================
# 为用户添加分数
# ===============================================================================
def user_add_score(id, score):
    user = User.query.filter_by(id=id).one()
    new_score = user.score + score
    db.session.query(User).filter_by(id=id).update({User.score: new_score})
    db.session.commit()
