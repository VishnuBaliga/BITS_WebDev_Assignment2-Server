

class BaseMessages(object):
    def __init__(self):
        self.form_error = 'Form contains error, please try again.'
        self.obj_create_success = '{obj_name} created successfully.'
        self.obj_update_success = '{obj_name} updated successfully.'
        self.obj_retrive_success = '{obj_name} retrieved successfully.'
        self.obj_delete_success = "{obj_name} deleted successfully."
        self.object_not_found = 'Sorry, {obj_name} not found.'


class AuthMessages(BaseMessages):
    
    def __init__(self):
        super().__init__()
        self.login_failed = 'Incorrect Username/Password. Please try again.'
        self.login_success = 'Logged in successfully.'
        self.user_not_found = 'User not found or not exists.'
