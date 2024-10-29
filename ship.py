import pygame
class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船设置并设定初始位置"""
        self.screen=screen
        self.ai_settings=ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')

        # 缩放
        # 定义新的尺寸（例如，将宽度和高度都缩小到原来的50%）
        new_width = self.image.get_width() // 2
        new_height = self.image.get_height() // 2

        # 缩放图像
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # 每次都将新飞船放在界面底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)

        # 移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更改：更新飞船的center值，而非rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            # self.rect.centerx+=1
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.right>self.screen_rect.left:
            # self.rect.centerx-=1
            self.center-=self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx=self.center

    def center_ship(self):
        """让飞船在屏幕上剧中"""
        self.center=self.screen_rect.centerx

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)