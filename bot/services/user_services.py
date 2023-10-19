from bot.repositories.db_helpers.models import User
from bot.repositories.user_repository import UserRepository
from .helpers.amplitude_api import AmplitudeAPI


class UserService:
    repository = UserRepository()
    def start_actions(
            self,
            user_id: int,
            username: str,
            name: str,
            surname: str
    ) -> [User, bool]:
        user, was_in_db = self.repository.get_or_create(
            user_id=user_id,
            username=username,
            name=name,
            surname=surname
        )
        if not was_in_db:
            status_code, response = AmplitudeAPI.register(
                user_id=user_id
            )

        return user, was_in_db
