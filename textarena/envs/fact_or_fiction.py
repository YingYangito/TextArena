import gym
from gym import spaces

class FactOrFictionEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self):
        super(FactOrFictionEnv, self).__init__()
        self.max_rounds = 5  # Total rounds before game ends
        self.current_round = 0
        self.current_storyteller = 0  # Player 0 starts as storyteller
        self.current_challenger = 1  # Player 1 starts as challenger
        self.player_scores = [0, 0]  # [Player 0 score, Player 1 score]
        
        # Placeholder observation and action spaces
        self.observation_space = spaces.Discrete(1)  # Unused in this shell
        self.action_space = spaces.Discrete(2)  # 0=Accept, 1=Challenge
        
        self.claim_text = None
        self.truth = None  # Placeholder for future API truth check

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self.current_round = 0
        self.current_storyteller = 0
        self.current_challenger = 1
        self.player_scores = [0, 0]
        return 0, {"info": "Game start"}

    def step(self, action):
        # Placeholder truth check – to be replaced with API call later
        correct = (action == 1 and not self.truth) or (action == 0 and self.truth)
        
        # Scoring logic
        if correct:
            self.player_scores[self.current_challenger] += 1
            self.player_scores[self.current_storyteller] -= 1
        else:
            self.player_scores[self.current_storyteller] += 1
            self.player_scores[self.current_challenger] -= 1
        
        self.current_round += 1
        terminated = self.current_round >= self.max_rounds
        truncated = False

        # Rotate storyteller and challenger
        self.current_storyteller, self.current_challenger = self.current_challenger, self.current_storyteller

        info = {
            "storyteller": self.current_storyteller,
            "challenger": self.current_challenger,
            "claim_text": self.claim_text,
            "truth": self.truth
        }
        return 0, 0, terminated, truncated, info

    def submit_claim(self, claim_text, is_true):
        """
        Storyteller submits a claim. 'is_true' should be verified (API placeholder).
        """
        self.claim_text = claim_text
        self.truth = is_true  # Placeholder – future API integration

    def render(self, mode="human"):
        if mode == "human":
            print(f"Storyteller (Player {self.current_storyteller}) says: {self.claim_text}")
            print(f"Current scores: Player 0 = {self.player_scores[0]}, Player 1 = {self.player_scores[1]}")
        else:
            raise NotImplementedError(f"Render mode {mode} not supported.")
