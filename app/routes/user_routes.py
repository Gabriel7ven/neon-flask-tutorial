from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from app.models.user import User
from app import db

# Create a blueprint named 'user' with a URL prefix '/user'
user_bp = Blueprint('user', __name__, url_prefix='/user')

# Route for creating a new user (HTML form submission)
@user_bp.route('/create', methods=['POST'])
def create_user():
    if request.method == 'POST':
        data = request.form
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user.list_users'))
    return render_template('create_user.html')

# Route for displaying all users (HTML)
@user_bp.route('/list', methods=['GET'])
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

# API route for retrieving all users (JSON)
@user_bp.route('/api/list', methods=['GET'])
def get_users_api():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Route for displaying a single user (HTML)
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

# API route for retrieving a single user (JSON)
@user_bp.route('/api/<int:user_id>', methods=['GET'])
def get_user_api(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())