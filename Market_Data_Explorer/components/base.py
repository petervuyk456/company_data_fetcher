class BaseBlock:
    def __init__(self, app):
        self.app = app

        if self.app is not None and hasattr(self, 'callbacks'):
            self.callbacks(self.app)
