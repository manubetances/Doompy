from sprite_object import *


class ObjectHandler:
    def __init__(self, game):
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/staticSprites'
        self.animated_sprite_path = 'resources/sprites/animatedSprites'
        add_sprite = self.add_sprite

        # sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
