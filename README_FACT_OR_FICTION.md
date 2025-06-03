# FactOrFiction Game (Multiplayer Shell)

This is a scalable shell for a multiplayer "Fact or Fiction" game, added as a custom environment to the **TextArena** fork. It supports:
- **Dynamic Storyteller & Challenger Roles**: Players alternate turns.
- **Dynamic Claim Submission**: Storyteller creates a claim (true or fabricated).
- **Placeholder for Truth Verification**: To be replaced with an API or AI integration.
- **Scoring System**: Points awarded/deducted based on player decisions.

## 📂 Files
- `fact_or_fiction.py`: The core Gym environment implementing the game logic. Located in `textarena/envs`.
- `test_fact_or_fiction.py`: A simple script to run the game interactively in the console.
  - Players take turns submitting and challenging claims.
  - Future versions will integrate human vs AI play via an API.
- `README_FACT_OR_FICTION.md`: This file, documenting the game and setup instructions.

## 🛠️ Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YingYangito/TextArena.git
   cd TextArena
