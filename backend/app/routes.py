from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def test_route():
    return {
        "message": "Routes module is working successfully."
    }