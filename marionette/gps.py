from flask import Blueprint, jsonify

bp = Blueprint("gps", __name__, url_prefix="/gps")


@bp.route("/location")
def location():
    # TODO: Get the location of the GPS device
    return jsonify({
        'location': {
            'latitude': 1.0,
            'longitude': 2.0,
        },
    })

@bp.route("/status")
def status():
    # TODO: Get the status of the GPS device
    return jsonify({'status': 'Status of the GPS device.'})
