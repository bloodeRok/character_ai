
@extend_schema_view(
    post=extend_schema(
        tags=["telegram profiles", "create"],
        operation_id="Create Telegram Profile",
        description="Creates Telegram Profile with supplied parameters.\n"
                    "* Binds telegram profile to user with passed dota_id."
                    "* Creates user if it was not found by dota_id.",
        request=TelegramProfileCreateRequest,
        responses={
            204: TelegramProfileResponse().updated()
        }
    )
)
@api_view(["POST"])
def tgprofiles(
        request: Request
) -> HttpResponse:
    data = TelegramProfileCreateRequest(data=request.data)
    data.is_valid(raise_exception=True)
    data = data.validated_data

    nickname = TelegramProfileService().get_or_create(
        chat_id=data["chat_id"],
        dota_user_id=data["dota_user_id"]
    )
    return Response(
        data={"nickname": nickname},
        status=status.HTTP_201_CREATED
    )
