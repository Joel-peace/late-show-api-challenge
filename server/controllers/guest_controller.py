from flask import Blueprint, request, jsonify
from server.models.guest import Guest
from server.models import db


guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET', 'POST'])
def guests():
    if request.method == 'POST':
        data = request.get_json()
        new_guest = Guest(name=data['name'], profession=data['profession'])
        db.session.add(new_guest)
        db.session.commit()
        return jsonify(new_guest.to_dict()), 201

    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

 
@guest_bp.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    guest = Guest.query.get(id)
    if not guest:
        return jsonify({"error": "Guest not found"}), 404
    db.session.delete(guest)
    db.session.commit()
    return jsonify({"message": "Guest deleted"}), 200
