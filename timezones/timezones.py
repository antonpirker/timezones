from flask import Flask, jsonify, request
from tzwhere import tzwhere

tz = tzwhere.tzwhere()


app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify({"timezones": f"{request.base_url}timezones"})


@app.route("/timezones", methods=["GET"])
def timezones():
    lat = request.args.get("lat", None)
    lon = request.args.get("lon", None)

    if not lat and not lon:
        return jsonify({"timezones": sorted(tz.timezoneNamesToPolygons.keys())})

    if lat and lon:
        try:
            timezone_name = tz.tzNameAt(float(lat), float(lon))
            return jsonify({"timezone": timezone_name or "UTC"})
        except Exception as e:
            return (
                f"[400] BAD REQUEST: Error while fetching timezone for lat/lon: {lat}/{lon}",
                400,
            )

    else:
        return (
            f"[400] BAD REQUEST: Please specify both query parameters ('lat' AND 'lon') or no query parameter to get a list of all timezones available.",
            400,
        )
