import logging
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from config import settings
from pb.flight_pb2_grpc import add_FlightServicer_to_server
from services.flight import FlightBaseService


class FlightService(FlightBaseService):
    pass


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_FlightServicer_to_server(FlightService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=settings.logging_level, format=settings.log_format)
    logging.info('Flight Server Starter...')

    serve()
