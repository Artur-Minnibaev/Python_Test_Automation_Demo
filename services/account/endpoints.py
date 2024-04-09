HOST = 'https://demoqa.com/Account/v1'


class Endpoints:

    auth_user = f"{HOST}/Authorized"
    post_create_user = f"{HOST}/User"
    get_user_by_id = lambda self, UUID: f"{HOST}/User/{UUID}"
    delete_user_by_id = lambda self, UUID: f"{HOST}/User/{UUID}"
