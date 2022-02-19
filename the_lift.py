import operator as op


class Dinglemouse(object):
    def __init__(self, queues, capacity):
        # print(queues, capacity)
        self.queues = {level: list(queue) for level, queue in enumerate(queues)}
        self.level_min = 0
        self.level_max = len(queues) - 1
        self.lift_capacity = capacity
        self.lift_people = []
        self.lift_level = self.level_min
        self.lift_stops = [self.lift_level]
        self.UP = True
        self.DOWN = False
        self.lift_direction = self.UP

    def trackStop(self):
        if self.lift_stops[-1] != self.lift_level:
            self.lift_stops.append(self.lift_level)

    def getPeopleToServe(self):
        return sum(len(q) for l, q in self.queues.items()) + len(self.lift_people)

    def peopleWantToLeaveHere(self):
        return self.lift_people.count(self.lift_level)

    def getPeopleToServeInDirectionHere(self):
        """returns number of people waiting to be served in the currenct direction (including current level)"""
        waiting = 0
        if self.lift_direction == self.UP:
            for level in range(self.lift_level, self.level_max + 1):
                for goto in self.queues[level]:
                    if goto>self.lift_level:
                        waiting+=1
        else:
            for level in range(self.lift_level, self.level_min - 1, -1):
                for goto in self.queues[level]:
                    if goto<self.lift_level:
                        waiting+=1
        return waiting

    def peopleWaitingMyDirection(self):
        """
        Returns:
            list: people who want to go in the direction of the lift
        """
        waiting = [
            goto
            for goto in self.queues[self.lift_level]
            if self.lift_direction == self.UP
            and goto > self.lift_level
            or self.lift_direction == self.DOWN
            and goto < self.lift_level
        ]
        return waiting

    def letPeopleLeaveHere(self):
        n = self.peopleWantToLeaveHere()
        while n:
            self.lift_people.remove(self.lift_level)
            n -= 1
        pass

    def letPeopleEnterHere(self):
        free = self.getLiftFreeCapacity()
        waiting = self.peopleWaitingMyDirection()
        for person in waiting[:free]:
            self.queues[self.lift_level].remove(person)
            self.lift_people.append(person)
        pass

    def getLiftFreeCapacity(self):
        return self.lift_capacity - len(self.lift_people)

    def nextLevelFromHere(self):
        if self.lift_direction == self.UP:
            self.lift_level += 1
            if self.lift_level == self.level_max:
                self.lift_direction = self.DOWN
        else:
            self.lift_level -= 1
            if self.lift_level == self.level_min:
               self.lift_direction = self.UP

    def pauseLift(self):
        self.lift_level = 0
        self.trackStop()

    def liftLevelController(self):
        if self.peopleWantToLeaveHere():
            self.letPeopleLeaveHere()
            self.trackStop()
        if len(self.peopleWaitingMyDirection()):
            self.letPeopleEnterHere()
            self.trackStop()
        if self.getPeopleToServe() == 0:
            self.pauseLift()
        else:
            self.nextLevelFromHere()

    def theLift(self):
        while self.getPeopleToServe():
            self.liftLevelController()
        return self.lift_stops


# Floors:    G     1      2        3     4      5      6         Answers:
tests = [
    [((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0], 5],
    [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0], 5],
    [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0], 5],
    [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0], 5], 
    [
        (
            (),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        ),
        [0, 6, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 3, 2, 1, 0, 1, 0], 5
    ],
    [((), (), (4, 4, 4, 4), (), (2, 2, 2, 2), (), ()), [0, 2, 4, 2, 4, 2, 0], 2],
]

for queues, answer, capacity in tests[::-1]:
    lift = Dinglemouse(queues, capacity)
    print(lift.theLift() == answer)
