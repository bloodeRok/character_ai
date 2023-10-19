from bot.repositories.db_helpers.connect_to_db import session
from bot.repositories.db_helpers.models import User


class UserRepository:
    model = User

    def get_or_create(
            self,
            user_id: int,
            username: str,
            name: str,
            surname: str
    ) -> [User, bool]:
        was_in_db = False
        user = session.query(self.model).filter_by(user_id=user_id).first()
        if not user:
            new_user = self.model(
                user_id=user_id,
                username=username,
                name=name,
                surname=surname
            )
            session.add(new_user)
            session.commit()
            return new_user, was_in_db

        was_in_db = True
        return user, was_in_db
