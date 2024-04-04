import time


def timing_middleware(get_response):
    def middleware(request):
        start_time = time.time()

        response = get_response(request)

        end_time = time.time()

        execution_time = end_time - start_time

        response['X-Class-Execution-Time'] = str(execution_time)

        return response
    return middleware

# timing_middleware(middleware)(request)
# TimingMiddleware(middleware)(request)
# __call__()


class TimingMiddleware:

    def __init__(self, get_response, *args, **kwargs):
        self.get_response = get_response
        self.args = args
        self.kwargs = kwargs

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request, *self.args, **self.kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        response['X-Class-Execution-Time'] = str(execution_time)

        return response

