import pygame
import sys
from settings import *
from grid import Grid
from player import Player
from ai_prey import AIPrey
from ai_predator import AIPredator

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Predator vs Prey - Human vs AI")
clock = pygame.time.Clock()

# Change this flag:
HUMAN_IS_PREY = True   # True: human = prey vs AI predator
                       # False: human = predator vs AI prey

SURVIVE_TURNS = 40     # how many turns prey must survive


def main():
    running = True

    grid = Grid()

    # Ensure spawn positions are not obstacles
    human_start = (1, 1)
    ai_start = (GRID_SIZE - 2, GRID_SIZE - 2)
    while human_start in grid.obstacles:
        human_start = (human_start[0] + 1, human_start[1] + 1)
    while ai_start in grid.obstacles:
        ai_start = (ai_start[0] - 1, ai_start[1] - 1)

    # Setup roles
    if HUMAN_IS_PREY:
        human = Player(human_start[0], human_start[1], BLUE)
        ai_agent = AIPredator(ai_start[0], ai_start[1], RED)
    else:
        human = Player(human_start[0], human_start[1], BLUE)
        ai_agent = AIPrey(ai_start[0], ai_start[1], RED)

    turns = 0
    font = pygame.font.SysFont(None, 24)
    game_over = False
    result_text = ""

    while running:
        window.fill((30, 30, 30))

        moved = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and not moved:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        moved = human.move(0, -1, grid)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        moved = human.move(0, 1, grid)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        moved = human.move(-1, 0, grid)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        moved = human.move(1, 0, grid)

            # After human moves, AI moves
            if moved:
                turns += 1

                if HUMAN_IS_PREY:
                    # AI is predator
                    ai_agent.decide_and_move(grid, (human.x, human.y))
                else:
                    # AI is prey
                    ai_agent.decide_and_move(grid, (human.x, human.y))

                # Check collision (capture)
                if HUMAN_IS_PREY:
                    # predator catches human
                    if (ai_agent.x, ai_agent.y) == (human.x, human.y):
                        game_over = True
                        result_text = "You were caught! Predator (AI) wins."
                else:
                    # human is predator
                    if (ai_agent.x, ai_agent.y) == (human.x, human.y):
                        game_over = True
                        result_text = "You caught the prey! You win."

                # Check survive condition
                if not game_over and turns >= SURVIVE_TURNS:
                    game_over = True
                    if HUMAN_IS_PREY:
                        result_text = "You survived! Prey (You) win."
                    else:
                        result_text = "Time Up! Prey survived. AI wins."

        # Draw grid + agents
        grid.draw(window)
        human.draw(window)
        ai_agent.draw(window)

        # Show text: turns, mode, result
        info = f"Turns: {turns} | Mode: {'Human=Prey' if HUMAN_IS_PREY else 'Human=Predator'}"
        text_surface = font.render(info, True, WHITE)
        window.blit(text_surface, (10, 10))

        if game_over:
            result_surface = font.render(result_text, True, GREEN if "win" in result_text.lower() and "AI" not in result_text else RED)
            window.blit(result_surface, (10, 40))
            hint_surface = font.render("Press R to restart", True, WHITE)
            window.blit(hint_surface, (10, 60))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Restart game (simple way: recall main)
                main()
                return

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
