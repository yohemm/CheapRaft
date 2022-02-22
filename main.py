import pygame
from game import *

pygame.init()
game = Game()
UNITY = 100
pygame.display.set_caption('Cheap Raft')
SCREEN = pygame.display.set_mode((1200, 675))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.click(SCREEN, UNITY)
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                if event.key == pygame.K_w:
                    game.inventory['wood'] += 5
                if event.key == pygame.K_p:
                    game.inventory['plastic'] += 5
                if event.key == pygame.K_l:
                    game.inventory['leaf'] += 5
    game.blitMap(SCREEN, UNITY)
    game.reloadStat()
    game.menuVillager.changeText(str(game.villager) + ' villageois :\n food ' + str(game.villagerStat['food'] / game.villager * 100) + '%\n watter ' + str(game.villagerStat['watter'] / game.villager * 100) + '%\n hummor ' + str(game.villagerStat['hummor'] / game.villager * 100) + '%')
    game.menuVillager.blit(SCREEN)
    game.menuInventory.changeText('bois: ' + str(game.inventory['wood']) + '\nplastique: ' + str(game.inventory['plastic']) + '\nfeuillage: ' + str(game.inventory['leaf']))
    game.menuInventory.blit(SCREEN,  alignX='right')
    pygame.display.update()
    SCREEN.fill((0,0,0))