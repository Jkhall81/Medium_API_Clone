from rest_framework.exceptions import APIExceptions


class YouHaveAlreadyRated(APIExceptions):
    status_code = 400
    default_detail = "You already rated this article."
    default_code = "bad_request"
