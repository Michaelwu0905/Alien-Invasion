import game_functions as gf
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from alien import Alien
from button import Button
from scoreboard import Scoreboard

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("ALIEN INVASION")

    # 创建play按钮
    play_button=Button(ai_settings,screen,'Play')

    # 创建一个用于存储游戏统计信息的实例，并创建计分牌
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    # 创建一艘飞船
    ship=Ship(ai_settings,screen)

    # 创建一个用于储存子弹的编组
    bullets=Group()

    # 创建一个外星人
    # alien = Alien(ai_settings, screen)

    # 创建外星人群
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 设置背景色
    bg_color=(230,230,230)



    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()

            # print(len(bullets))
            # 每次循环都重绘屏幕 让最近绘制的屏幕可见

            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) 
 

run_game()
