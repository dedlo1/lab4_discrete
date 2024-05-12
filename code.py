import random


class FSM:
    def __init__(self):
        self.sleep = self._setup_sleep()
        next(self.sleep)
        self.study = self._setup_study()
        next(self.study)
        self.eat = self._setup_eat()
        next(self.eat)
        self.chill = self._setup_chill()
        next(self.chill)
        
        self.current_state = self.sleep


    def send(self, hour):
        self.current_state.send(hour)


    def _setup_sleep(self):
        while True:
            hour = yield

            if hour < 6:
                self.current_state = self.sleep
            elif hour == 7 and random.random() < 0.5:
                self.current_state = self.chill
            elif hour == 8:
                self.current_state = self.eat
            else:
                self.current_state = self.sleep


    def _setup_chill(self):
        while True:
            hour = yield

            if hour == 8 and random.random() < 0.5:
                self.current_state = self.eat
            elif hour == 9:
                self.current_state = self.study
            elif hour == 15 and random.random() < 0.5:
                self.current_state = self.eat
            elif 16 <= hour <= 18:
                self.current_state = self.chill
            elif hour == 19:
                self.current_state = self.eat
            elif hour == 20:
                self.current_state = self.sleep
            else:
                self.current_state = self.chill


    def _setup_eat(self):
        while True:
            hour = yield

            if hour == 9:
                self.current_state = self.study
            elif hour == 16:
                self.current_state = self.chill
            elif hour == 20:
                self.current_state = self.sleep
            else:
                self.current_state = self.eat

    def _setup_study(self):
        while True:
            hour = yield

            if hour == 15:
                self.current_state = self.eat
            elif hour == 19:
                self.current_state = self.sleep
            else:
                self.current_state = self.study





def main():
    fsm = FSM()
    for hour in range(1, 25):
        fsm.send(hour)
        print(f'{hour}: {fsm.current_state.__name__[7:]}')

main()
