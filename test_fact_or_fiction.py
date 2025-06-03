import gym
import textarena

env = gym.make("FactOrFiction-v0")
obs, info = env.reset()

done = False
while not done:
    storyteller = env.current_storyteller
    challenger = env.current_challenger

    # Storyteller submits claim
    print(f"\nStoryteller (Player {storyteller})'s turn:")
    claim = input("Enter your claim: ")
    truth_input = input("Is it true? (y/n): ").lower()
    is_true = truth_input == 'y'
    env.submit_claim(claim, is_true)

    # Show claim to challenger
    print(f"\nChallenger (Player {challenger}) sees the claim:")
    print(f"'{claim}'")
    action = int(input("Enter action (0=Accept, 1=Challenge): "))

    # Step and update
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"Updated Scores: Player 0 = {env.player_scores[0]}, Player 1 = {env.player_scores[1]}")
    done = terminated or truncated

print("\nGame Over! Final Scores:")
print(f"Player 0: {env.player_scores[0]}")
print(f"Player 1: {env.player_scores[1]}")
