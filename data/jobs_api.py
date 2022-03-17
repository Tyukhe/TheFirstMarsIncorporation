import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'job'))
                 for item in jobs]
        }
    )

@blueprint.route('/api/jobs/<int:id>', methods=['GET'])
def get_one_jobs(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': news.to_dict(only=('team_leader', 'job'))
        }
    )

@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json[''],
        collaborators=request.json[''],
        start_date=request.json[''],
        end_date=request.json['']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})