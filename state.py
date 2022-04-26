from aiogram.dispatcher.filters.state import State, StatesGroup

class waiting(StatesGroup):
	waiting_for_offer = State()
	#waiting_for_desigeon = State()

class admin(StatesGroup):
	wait_for_descr = State()
	wait_for_desigeon = State()