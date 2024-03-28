from app import db
from .models import Vote

def add_vote(candidate):
    vote = Vote(candidate=candidate)
    db.session.add(vote)
    db.session.commit()

def get_votes():
    votes = Vote.query.all()
    vote_count = {}
    for vote in votes:
        if vote.candidate in vote_count:
            vote_count[vote.candidate] += 1
        else:
            vote_count[vote.candidate] = 1
    return vote_count
