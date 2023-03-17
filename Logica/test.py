from WebDevP1.Logica.Modelos import usuarios as u 

def create_user(nick_name, full_name):
    user = u.Users(nick_name=nick_name, full_name=full_name)
    try:
        u.session.add(user)
        u.session.commit()
        return 'successful'
    except Exception as error:
        u.session.rollback()
        raise  f"Error {str(error)}"
