from subprocess import CalledProcessError, run

from flask import Blueprint, request, jsonify

bp = Blueprint("interior_sign", __name__, url_prefix="/interior_sign")


@bp.route("/say", methods=("POST",))
def say():
    try:
        message = request.json['message']
    except (AttributeError, KeyError, TypeError):
        return jsonify({'error': 'Message is required.'}), 400

    cmd = ["echo", message]
    cp = run(cmd, capture_output=True, encoding='utf8')
    try:
        cp.check_returncode()
    except CalledProcessError:
        return jsonify({'error': cp.stderr}), 500

    return jsonify({'response': cp.stdout})
