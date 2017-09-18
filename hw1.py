from enum import Enum

class Primitive(Enum):
	DRAW = 'D'
	WIN = 'W'
	UNKNOWN = 'U'
	LOSE = 'L'
	TIE = 'T'

def init_pos(n=4):
	"""
		Returns the initial position
	"""
	return n

def primitive(pos):
	if pos == 0:
		return Primitive.LOSE
	return Primitive.UNKNOWN

def generate_moves(pos):
	if pos == 0:
		return []
	elif pos == 1:
		return [-1]
	return [-1, -2]

def do_move(pos, action):
	return pos + action
	

def solver(init_pos, primitive, generate_moves, do_move):
	# solve the game
	solved_cache = {}

	def memo_solver(pos, primitive, generate_moves, do_move, solved_cache):
		if pos in solved_cache:
			return solved_cache[pos]

		next_states = []
		for move in generate_moves(pos):
			next_state = do_move(pos, move)
			if next_state in solved_cache:
				next_states.append(solved_cache[next_state])
			else:
				prim = memo_solver(next_state, primitive, generate_moves, do_move, solved_cache)
				solved_cache[next_state] = prim
				next_states.append(prim)

		r = Primitive.LOSE
		for s in next_states:
			if s is Primitive.LOSE:
				r = Primitive.WIN
		return r
	return memo_solver(init_pos(), primitive, generate_moves, do_move, solved_cache)




if __name__ == '__main__':
    print(solver(init_pos, primitive, generate_moves, do_move))