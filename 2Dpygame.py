import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設置視窗大小
寬度 = 800
高度 = 600
視窗 = pygame.display.set_mode((寬度, 高度))
pygame.display.set_caption("2D 圖片移動遊戲")

# 定義顏色
白色 = (190, 190, 190)

'''

# 載入玩家走路動畫圖片
IMG_PATH = '/walk'
走路動畫 = [pygame.image.load(f'{IMG_PATH}{i}.PNG') for i in range(1, 4)]
走路動畫 = [pygame.transform.scale(img, (50, 50)) for img in 走路動畫]

# 定義walk4PNG為walk2PNG的左右反轉
walk2 = pygame.image.load(f'{IMG_PATH}2.PNG')
walk2 = pygame.transform.scale(walk2, (50, 50))
walk4 = pygame.transform.flip(walk2, True, False)
走路動畫.append(walk4)

'''
# 定義玩家大小
agares大小 = (64, 64)
gaap大小 = (84, 84)

IMG_PATH_a = 'agares/walk'
走路動畫a = []
for i in range(1, 5):  # 現在範圍是 1 到 4
    if i == 3:
        # 第三格使用第一格的圖片
        走路動畫a.append(走路動畫a[0])
    else:
        img = pygame.image.load(f'{IMG_PATH_a}{i}.PNG')
        img = pygame.transform.scale(img, (agares大小))
        走路動畫a.append(img)

# 第二個玩家（WASD鍵控制）
IMG_PATH_g = 'gaap/walk'  # 為第二個玩家設置不同的路徑
走路動畫g = []
for i in range(1, 5):  # 範圍是 1 到 4
    if i == 3:
        # 第三格使用第一格的圖片
        走路動畫g.append(走路動畫g[0])
    else:
        img = pygame.image.load(f'{IMG_PATH_g}{i}.PNG')
        img = pygame.transform.scale(img, (gaap大小))
        走路動畫g.append(img)

# 初始化動畫變數
當前幀a = 當前幀g = 0 
動畫速度 = 5
動畫計數器a = 動畫計數器g = 0

# 獲取圖片矩形
agares = 走路動畫a[0].get_rect()
agares.center = (寬度 // 2, 高度 // 2)
gaap = 走路動畫g[0].get_rect()
gaap.center = (寬度 // 2, 高度 // 2)

# 設置移動速度
速度 = 5

# 遊戲主循環
while True:
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 獲取按鍵狀態
    按鍵 = pygame.key.get_pressed()
    
    # 移動玩家
    移動a = False
    if 按鍵[pygame.K_LEFT] and agares.left > 0:
        agares.x -= 速度
        移動a = True 
    if 按鍵[pygame.K_RIGHT] and agares.right < 寬度:
        agares.x += 速度
        移動a = True
    if 按鍵[pygame.K_UP] and agares.top > 0:
        agares.y -= 速度
        移動a = True
    if 按鍵[pygame.K_DOWN] and agares.bottom < 高度:
        agares.y += 速度
        移動a = True

    移動g = False
    if 按鍵[pygame.K_a] and gaap.left > 0:
        gaap.x -= 速度
        移動g = True
    if 按鍵[pygame.K_d] and gaap.right < 寬度:
        gaap.x += 速度
        移動g = True
    if 按鍵[pygame.K_w] and gaap.top > 0:
        gaap.y -= 速度
        移動g = True
    if 按鍵[pygame.K_s] and gaap.bottom < 高度:
        gaap.y += 速度
        移動g = True

     # 更新a動畫
    if 移動a:
        動畫計數器a += 1
        if 動畫計數器a >= 動畫速度:
            當前幀a = (當前幀a + 1) % len(走路動畫a)
            動畫計數器a = 0
    else:
        當前幀a = 0  # 靜止時顯示第一幀

    # 更新g動畫
    if 移動g:
        動畫計數器g += 1
        if 動畫計數器g >= 動畫速度:
            當前幀g = (當前幀g + 1) % len(走路動畫g)
            動畫計數器g = 0
    else:
        當前幀g = 0

    # 清空視窗
    視窗.fill(白色)

    # 繪製玩家圖片
    # 視窗.blit(玩家圖片, 玩家)

    視窗.blit(走路動畫a[當前幀a], agares)
    視窗.blit(走路動畫g[當前幀g], gaap)

    # 更新顯示
    pygame.display.flip()

    # 控制遊戲速度
    pygame.time.Clock().tick(60)