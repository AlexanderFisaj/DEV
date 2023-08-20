import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def update(self, title=None, body=None):
        self.title = title if title is not None else self.title
        self.body = body if body is not None else self.body
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }