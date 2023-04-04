from .serializers import TodoSerializer, TimingTodoSerializer
from .models import Todo, TimingTodo
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# from rest_framework.decorators import api_view
# from rest_framework.views import APIView


class TodoApi(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=["GET"])
    def get_timing_todo(self, request):
        timing_todo_objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(timing_todo_objs, many=True)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "timing_todo_fetched",
                "data": serializer.data,
            }
        )

    @action(detail=False, methods=["POST"])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "success",
                        "data": serializer.data,
                    }
                )
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "invalid data",
                    "data": serializer.errors,
                }
            )

        except Exception as e:
            print(e)

        return Response(
            {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "something went wrong",
            }
        )
