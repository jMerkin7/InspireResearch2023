import time
import cv2
import numpy as np
from selenium import webdriver
from javascript import require, Once, On, once, AsyncTask, off

mineflayer = require('mineflayer')
pathfinder = require('node_modules\mineflayer-pathfinder')
viewer = require('prismarine-viewer').mineflayer
RANGE_GOAL = 1
#use executable path if neccesary, download correct webdrier and provide path to driver
driver = webdriver.Chrome()

bot = mineflayer.createBot({
    'host': 'localhost',
    'port': 25565,
    'username': 'Mini_Proj_3'
})
bot.loadPlugin(pathfinder.pathfinder)
print('Started mineflayer')

@On(bot, 'spawn')
def hand(*args):
    print('Bot Spawned')
    bot.chat('Spawned')
    movements = pathfinder.Movements(bot)
    viewer(bot, {'firstPerson': True, 'port': 3000, 'version': '1.19.3'})
#viewer.setFirstPersonCamera(None, 0, -45) #sets pitch down 45 degrees
    driver.get('http://localhost:3000/')
    time.sleep(5)

    bot.chat('Mini_Proj_3 is ready.')


    @On(bot, 'chat')
    def handleMsg(this, sender, message, *args):
        if ((message == 'start') & (sender != 'Mini_Proj_3')):
            counter = 0
            bot.setControlState('forward', True)
            stopBot = False
            while not stopBot:
                driver.save_screenshot('Assets\ss1.png')
                time.sleep(1) #second between screenshots
                driver.save_screenshot('Assets\ss2.png')
                #load grayscale images of ss1 and ss2

                ss1 = np.asarray(cv2.imread('Assets\ss1.png', 0)).flatten()
                ss2 = np.asarray(cv2.imread('Assets\ss2.png', 0)).flatten()

                correlation = np.corrcoef(ss1, ss2)
                #sum = np.sum(np.abs(ss1 - ss2))
                #print(sum)
                print(correlation[0])
                print(correlation[1])

                if correlation[0][1] == correlation[0][0]:
                    bot.chat('Attempting to jump.')
                    bot.setControlState('jump', True)
                    time.sleep(2)
                    bot.setControlState('jump', False)
                    counter = counter+1
                if counter > 5:
                    bot.chat('Bot may be stuck. Waiting for next input.')
                    bot.chat('/tp _Retrospective_')
                    bot.setControlState('forward', False)
                    break
        if (message == 'leave'):
            bot.chat('leaving')
            driver.close()
            bot.end()
        if (message == 'tp'):
            bot.chat('/tp _Retrospective_')
        if (message == 'kick'):
            bot.chat('/kick PathfinderBot')
