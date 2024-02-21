from maps import env_list
import numpy as np
import collections

env = env_list[0].environment
Args = Point = collections.namedtuple('Args', 'type_reward')
args = Args('MA_Binary_WO_Pen')
print('num_towers: {}, num_agents: {}', env.board.num_towers, env.board.agents.num_agents)

for i in range(100):
    state = env.get_state()
    action = np.array([env.action_space.sample() for i in range(env.board.agents.num_agents)])
    # print(action)
    next_state, reward, done, position = env.step(action=action, args=args)
    print('iteration: {}, state: {}, action: {}, reward: {}, next_state: {}'.format(i, state, action, reward, next_state))


state = env.reset()
print('reset the environment to its initial point: {}'.format(state))