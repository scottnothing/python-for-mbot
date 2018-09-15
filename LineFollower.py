#!/usr/bin/env python
import time

from lib.mBot import *


class LineFollower(object):
    def __init__(self, bot):
        self.robot = bot
        self.robot.startWithHID()
        time.sleep(0.2)

        self.follower_status = None
        self.speed = 75

    def spin(self):

        def callback(value):
            self.follower_status = value

        while not self.robot.exiting:
            self.robot.requestLineFollower(1, 2, callback)
            self.update()
            time.sleep(0.05)

    def update(self):
        if self.follower_status == 0.0:
            self.robot.doMove(self.speed, self.speed)
        elif self.follower_status == 1.0:
            self.robot.doMove(0, self.speed)
        else:
            self.robot.doMove(self.speed, 0)

    def __del__(self):
        print 'shutdown'
        self.robot.doMove(0, 0)
        time.sleep(0.2)



if __name__ == '__main__':


    follower = LineFollower(mBot())

    # while(True):
    #     follower.robot.requestLineFollower(1, 2, callback)
    #     sleep(0.2)
    follower.spin()