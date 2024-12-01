GAME_CONFIG=configs/medium.json
AGENT1=human
# AGENT1=human # set AGENT1 as "human" to play the game yourself
AGENT2=my_agent

python main.py --config_path $GAME_CONFIG \
                --agent1 $AGENT1 \
                --agent2 $AGENT2 \
                --interactive