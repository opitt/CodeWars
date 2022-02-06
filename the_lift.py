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
        self.lift_direction = self.DOWN

    def stopHere(self):
        if self.lift_stops[-1] != self.lift_level:
            self.lift_stops.append(self.lift_level)

    def getPeopleToServe(self):
        return sum(len(q) for l, q in self.queues.items()) + len(self.lift_people)

    def getQueueHere(self):
        """returns the queue at the current lift level"""
        return self.queues[self.lift_level]

    def getPeopleWantToLeaveHere(self):
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

    def getPeopleWantToGoInLiftDirectionHere(self):
        """
        Returns:
            list: people who want to go in the current direction of the lift
        """
        queue = self.getQueueHere()
        waiting = [
            person
            for person in queue
            if self.lift_direction == self.UP
            and person > self.lift_level
            or self.lift_direction == self.DOWN
            and person < self.lift_level
        ]
        return waiting

    def letPeopleLeaveHere(self):
        n = self.getPeopleWantToLeaveHere()
        while n:
            self.lift_people.remove(self.lift_level)
            n -= 1
        pass

    def letPeopleEnterHere(self):
        free = self.getLiftFreeCapacity()
        waiting = self.getPeopleWantToGoInLiftDirectionHere()
        for person in waiting[:free]:
            self.queues[self.lift_level].remove(person)
            self.lift_people.append(person)
        pass

    def getLiftFreeCapacity(self):
        return self.lift_capacity - len(self.lift_people)

    def liftIsEmpty(self):
        return self.getLiftFreeCapacity() == self.lift_capacity

    def nextDirectionHere(self):
        if self.lift_level == self.level_max:
            self.lift_direction = self.DOWN
        elif self.lift_level == self.level_min:
            self.lift_direction = self.UP
        elif self.lift_direction == self.UP:
            # The Lift never changes direction until there are no more people wanting to get on/off in the direction it is already travelling
            if (
                not any(
                    map(lambda goingto: goingto > self.lift_level, self.lift_people)
                )
                and self.getPeopleToServeInDirectionHere() == 0
            ):
                self.lift_direction = self.DOWN
        elif self.lift_direction == self.DOWN:
            # The Lift never changes direction until there are no more people wanting to get on/off in the direction it is already travelling
            if (
                not any(
                    map(lambda goingto: goingto < self.lift_level, self.lift_people)
                )
                and self.getPeopleToServeInDirectionHere() == 0
            ):
                self.lift_direction = self.UP
        pass

    def nextLevelUp(self):
        # When empty the Lift tries to be smart. For example,
        if self.liftIsEmpty():
            #  If it was going up then it may continue up to collect the highest floor person wanting to go down
            for level in [l for l in sorted(self.queues.keys(), reverse=True) if l> self.lift_level]:
                if any(map(lambda goingto: goingto < level, self.queues[level])):
                    self.lift_level = level
                    break
            else:
                self.lift_level += 1
        else:
            self.lift_level += 1
        return self.lift_level

    def nextLevelDown(self):
        # When empty the Lift tries to be smart. For example,
        if self.liftIsEmpty():
            #  If it was going down then it may continue down to collect the lowest floor person wanting to go up
            for level in [l for l in sorted(self.queues.keys()) if l<self.lift_level]:
                if any(map(lambda goingto: goingto > level, self.queues[level])):
                    self.lift_level = level
                    break
            else:
                self.lift_level -= 1
        else:
            self.lift_level -= 1
        return self.lift_level

    def nextLevel(self):
        if self.lift_direction == self.UP:
            return self.nextLevelUp()
        else:
            return self.nextLevelDown()

    def pauseLift(self):
        self.lift_level = 0
        self.stopHere()

    def liftController(self):
        # When called, the Lift will stop at a floor even if it is full,
        # although unless somebody gets off nobody else can get on!
        self.nextDirectionHere()
        if self.getPeopleWantToLeaveHere():
            self.stopHere()
            self.letPeopleLeaveHere()
        if len(self.getPeopleWantToGoInLiftDirectionHere()):
            self.stopHere()
            self.letPeopleEnterHere()
        self.nextLevel()

    def theLift(self):
        while self.getPeopleToServe():
            self.liftController()
        self.pauseLift()
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
