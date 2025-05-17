from concurrent import futures

import grpc

import course_service_pb2_grpc
import course_service_pb2


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseService"""

    def GetCourse(self, request, context: grpc.ServicerContext):
        """Метод обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetCourse c id курса: {request.course_id}')

        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов",
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    port = "50051"
    server.add_insecure_port(f"[::]:{port}")

    server.start()
    print(f"Сервер запущен на порту {port}")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()