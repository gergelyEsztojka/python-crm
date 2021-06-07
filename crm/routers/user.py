from fastapi import APIRouter

router = APIRouter(
    tags='User',
    prefix='/user'
)


@router.post('/')
def create_user():
    pass
