

import pygame
import pygame.math
import sys

# 定数
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# 水平方向の運動では重力はゼロ、または無視する
# 摩擦力や空気抵抗を表現する場合は、加速度を小さく設定することも可能です
ACCELERATION = 0.5
FPS = 60

class Player:
    def __init__(self, x, y, size, color):
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.size = size
        self.color = color
        self.is_grounded = False  # 地面にいるかどうかの状態を管理するフラグ

    def update(self):
        # 1. 常に重力加速度を適用する
        self.acceleration.y = 0.5  # 下向きの重力

        # 2. 速度の更新
        self.velocity += self.acceleration

        # 3. 摩擦の減衰（水平方向のみ）
        self.velocity.x *= 0.95

        # 4. 位置の更新
        self.position += self.velocity

    def draw(self, screen):
        # 画面に四角形を描画
        rect_obj = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect_obj)
# --- ゲームの初期化とループ ---
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# プレイヤーの生成
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 50, (255, 255, 255))

# ゲームループ
# ゲームループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # SPACEキーを押したときのジャンプ処理
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.is_grounded:
                # 負の値にすることで上向きにジャンプ
                player.velocity.y = -15
                player.is_grounded = False  # ジャンプ後は地面にいない状態にする

    # キーボード入力を取得 (水平方向の動き)
    keys = pygame.key.get_pressed()
    player.acceleration.x = 0  # 水平方向の加速度をリセット

    if keys[pygame.K_LEFT]:
        player.acceleration.x = -ACCELERATION
    if keys[pygame.K_RIGHT]:
        player.acceleration.x = ACCELERATION
    
    # プレイヤーの状態を更新
    player.update()

    # --- 地面との当たり判定 ---
    # プレイヤーが画面の下端に到達したら、それ以上落下させず、接地状態にする
    if player.position.y + player.size > SCREEN_HEIGHT:
        player.position.y = SCREEN_HEIGHT - player.size  # 画面内に位置を固定
        player.velocity.y = 0                         # 垂直方向の速度をゼロにする
        player.is_grounded = True                     # 地面にいる状態にする

    # 画面描画
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()

    # フレームレートを固定
    clock.tick(FPS)

pygame.quit()
sys.exit()