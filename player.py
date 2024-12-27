from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SHOT_RADIUS
from shot import *

class Player(CircleShape):
    rotation = 0
    containers = []
    timer_shots = 0
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        #print(f"shot fired {shot} WITH ROTATION {self.rotation}")
        starting_speed = pygame.Vector2(0, 1)
        starting_speed = starting_speed.rotate(self.rotation)
        shot.velocity = starting_speed * PLAYER_SHOOT_SPEED
        self.timer_shots = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer_shots -= dt

        if keys[pygame.K_a]:

            self.rotate(-dt)
        if keys[pygame.K_d]:

            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            #print("trying to shoot")
            if self.timer_shots <= 0:
                self.shoot()