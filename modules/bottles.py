import json
import bottle


class BottleJson(bottle.Bottle):
    def default_error_handler(self, res):
        error_message = dict(
            code=res.status_code,
            message=res.body
        )
        res.headers["Content-Type"] = 'application/json'
        return json.dumps(error_message)
