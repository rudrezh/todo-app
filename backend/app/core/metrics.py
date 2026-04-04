from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from flask import request, Response
import time

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
    ["endpoint"]
)

def init_metrics(app):

    @app.before_request
    def start_timer():
        request.start_time = time.time()

    @app.after_request
    def record_metrics(response):
        endpoint = request.path

        latency = time.time() - request.start_time
        REQUEST_LATENCY.labels(endpoint).observe(latency)

        REQUEST_COUNT.labels(
            request.method,
            endpoint,
            str(response.status_code)
        ).inc()

        return response

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)