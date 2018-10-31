from sqlalchemy import exc
from helpers.error_handler import ErrorHandler


class SaveContextManager():
    '''Manage sqlalchemy exceptions.'''

    def __init__(self, model_obj, model_param, model_name):
        self.model_obj = model_obj
        self.model_param = model_param
        self.model_name = model_name

    def __enter__(self):
        try:
            self.model_obj.save()
        except exc.IntegrityError as err:
            error_message = 'Database integrity error'
            if "duplicate key value violates unique constraint" in str(err):
                error_message = ErrorHandler.check_conflict(
                    self, self.model_param, self.model_name)
            elif "violates foreign key constraint" in str(err):
                error_message = ErrorHandler.foreign_key_conflict(
                    self, self.model_param, self.model_name)
            return error_message
        except exc.DBAPIError:
            return ErrorHandler.db_connection(self)

    def __exit__(self, type, value, traceback):
        return False
