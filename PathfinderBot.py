import time

from javascript import require, Once, On, once, AsyncTask, off
mineflayer = require('mineflayer')
pathfinder = require('node_modules\mineflayer-pathfinder')

RANGE_GOAL = 1
bot = mineflayer.createBot({
    'host': 'localhost',
    'port': 25565,
    'username': 'PathfinderBot'
})
bot.loadPlugin(pathfinder.pathfinder)
print('Started mineflayer')

@On(bot, 'spawn')
def handle(*args):
    print('Bot spawned')
    bot.chat('Hello')
    movements = pathfinder.Movements(bot)

    @On(bot, 'chat')
    def handleMsg(this, sender, message, *args):
        print("Got message", sender, message)
        if sender and (sender != 'PathfinderBot'):
            bot.chat(sender+' said '+message)
            if 'come' in message:
                player = bot.players[sender]
                print('Target: '+str(player))
                target = player.entity
                if not target:
                    bot.chat("Cannot currently reach you.")
                    #bot struggles to travel distances over ~100 block due to loading new chunks

                pos = target.position
                bot.pathfinder.setMovements(movements)
                bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, RANGE_GOAL))

        @On(bot, 'end')
        def handle(*args):
            print('Bot ended.', args)

    @AsyncTask(True)
    def giveLocation(*args):
        while True:
            botPos = bot.players['PathfinderBot'].entity.position
            print(botPos.x, botPos.y, botPos.z)
            bot.chat(str(botPos.x)+' '+str(botPos.y)+' '+str(botPos.z))
            time.sleep(10.0)

