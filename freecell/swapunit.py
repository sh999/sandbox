import unittest
'''
	Move one stack to another stack in free cell appropriately
	There are 4 blanks
	Card order = left most item is the card that is closest to vertical top
	stack 1 = ['9h','Jc','4s','3h','2s']
	stack 2 = ['2d','5h']
	You can move cards 4s, 3h, 2s to stack 2 to give new stack 2:
		2d, 5h, 4s, 3h, 2s

	Identical as swap.py but with unit test
'''
def ret_movable(stack1,stack2):
	'''
		Pretend there are infinite blanks
		Can you move stack 1 to stack 2?
		If so, return [True,<the_movable_cards_list>]
	'''
	'''
		Look at the bottom/last card in stack 2
		Find if there is a card in stack 1 that can be moved to stack 2
		See if this card and set of cards below it are black/red alternating, if so return true
	'''
	s2_lastcard = stack2[-1]
	s2_lastcard_val = s2_lastcard[0]
	s2_lastcard_suit = s2_lastcard[1]
	if s2_lastcard_val.isdigit():
		expected_val = int(s2_lastcard_val)-1
	if s2_lastcard_suit == 'h' or s2_lastcard_suit == 'd':
		expected_suits = ['s','c']
	else:
		expected_suits = ['h','d']
	expected_cards = []
	for suit in expected_suits:
		expected_cards.extend([str(expected_val)+suit])
	movable = []  # Movable cards from stack 1
	for exp_card in expected_cards:
		for c in range(0,len(stack1)):
			if stack1[c] == exp_card:
				movable = stack1[c:]
				# print movable
				return True,movable
	return False,None

def move_stacks_norestrict(stack1,stack2):
	'''
		Move stack1 to stack2 with no restrictions on blanks
	'''
	# print ret_movable(stack1,stack2)
	movable_bool,movable_cards = ret_movable(stack1,stack2)
	if movable_bool:
		stack2.extend(movable_cards)
	return stack2
	# print stack2

def move_stacks_restrict(stack1,stack2,blanks):
	'''
		Move stack1 to stack2 with restrictions on blanks
	'''
	if len(stack2) == 0:
		return stack1
	elif len(stack1) == 0:
		return stack2
	else:
		movable_bool,movable_cards = ret_movable(stack1,stack2)
		# print len(movable_cards)
		if movable_bool == False:
			return stack2
		elif len(movable_cards) < blanks and movable_bool:
			stack2.extend(movable_cards)
		return stack2

def main():
	blanks = 4 	# Number of blank spots
	stack1 = ['9h','Jc','4s','3h','2s']
	stack2 = ['2d','5h']

	print ret_movable(stack1,stack2)
	movable_bool,movable_cards = ret_movable(stack1,stack2)
	if movable_bool:
		stack2.extend(movable_cards)
	print stack2

def test_move_stacks_norestrict():
	stack1 = ['9h','Jc','4s','3h','2s']
	stack2 = ['2d','5h']
	print stack1
	print stack2
	print "stack2:out:"
	stack2 = move_stacks_norestrict(stack1,stack2)
	print stack2

def test_move_stacks_restrict():
	blanks = 0
	stack1 = ['9h','Jc','4s','3h','2s']
	stack2 = ['2d','5h']
	print stack1
	print stack2
	move_stacks_restrict(stack1,stack2,blanks)
	print stack2

class TestSwapFuncs(unittest.TestCase):
	def test_infinite_blank_swap(self):
		stack1 = ['9h','Jc','4s','3h','2s']
		stack2 = ['2d','5h']
		stack2 = move_stacks_norestrict(stack1,stack2)
		self.assertEqual(stack2,['2d','5h','4s','3h','2s'])
		self.assertEqual(stack1,['9h','Jc'])
	def test_infinite_blank_swap2(self):
		stack1 = ['9h','Jc','4s','4h','2s']
		stack2 = ['2d','5s']
		stack2 = move_stacks_norestrict(stack1,stack2)
		self.assertEqual(stack2,['2d','5s','4h','2s'])
	def test_restricted_blank_swap2(self):
		stack1 = ['9h','Jc','4s','4h','2s']
		stack2 = ['2d','5s']
		stack2 = move_stacks_restrict(stack1,stack2,4)
		self.assertEqual(stack2,['2d','5s','4h','2s'])
	def test_swap_to_none(self):
		stack1 = ['9h','Jc','4s','3h','2s']
		stack2 = []
		stack2 =move_stacks_restrict(stack1,stack2,4)
		self.assertEqual(stack2,stack1)
	def test_blank_origin(self):
		stack1 = []
		stack2 = ['2d','5s'] 
		old_stack2 = stack2
		stack2 = move_stacks_restrict(stack1,stack2,4)
		self.assertEqual(stack2,old_stack2)
	def test_swap_does_nothing(self):
		stack1 = ['2d','5s']
		stack2 = ['9h','Jc','4s','4h','2s']
		old_stack2 = stack2
		stack2 = move_stacks_restrict(stack1,stack2,4)
		self.assertEqual(stack2,old_stack2)
if __name__ == "__main__":

	unittest.main()

