import time


class State:
    def __init__(self):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

    def alarm(self):
        raise NotImplementedError


class ReadyState(State):
    def alarm(self, timeout):
        print("ALARM SENT")
        return TimeoutState()


class TimeoutState(State):
    def __init__(self):
        self.start = time.time()

    def alarm(self, timeout):
        if timeout < time.time() - self.start:
            return ReadyState()

        return self


class Timer:
    def __init__(self, timeout=5):
        self.timeout = timeout
        self.state = ReadyState()

    def alarm(self):
        self.state = self.state.alarm(self.timeout)


if __name__ == "__main__":
    timer = Timer(timeout=5)

    for i in range(10):
        print('Sending alarm...')
        timer.alarm()
        print('  State is: {}'.format(timer.state))
        time.sleep(1)
