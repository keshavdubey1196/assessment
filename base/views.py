from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


@api_view(["GET"])
def home(request):
    return Response(
        {
            "status": 200,
            "message": "worked successfully",
            "method_called": "GET method called",
        },
    )


@api_view(["POST"])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "valid data",
                    "data": serializer.data,
                }
            )

        return Response(
            {
                "status": False,
                "message": "invalid data",
                "data": serializer.errors,
            }
        )

    except Exception as e:
        print(e)

    return Response(
        {
            "status": False,
            "message": "something went wrong",
        }
    )


@api_view(["GET"])
def get_todos(request):
    todos = Todo.objects.all()
    serailizer = TodoSerializer(todos, many=True)

    return Response(
        {
            "status": 200,
            "data": serailizer.data,
        }
    )
