from functools import wraps

class on_fail(object):
	""" this is a decorator that adds a default output if a function fails """
	def __init__(self, default_output, logger=None):
		assert logger is None or callable(logger), 'logger needs to be a callable function'
		self.default_output = default_output
		self.logger = logger

	def __call__(self, wrapped_function):
		@wraps(wrapped_function)
		def wrapper(*args, **kwargs):
			try:  # try to run the function
				return wrapped_function(*args, **kwargs)
			except Exception as ex: # if it fails
				if self.logger is not None:
					# log the error if a logger was defined
					self.logger(repr(ex))
				# then return the default output
				return self.default_output
		return wrapper


if __name__ == '__main__':
	@on_fail('waffles')
	def my_function(a,b,c):
		return a*b/c

	print(my_function(1,2,3))
	print(my_function(1,2,'fish'))

	import logging

	@on_fail('waffles', logger=logging.warning)
	def my_function(a,b,c):
		return a*b/c

	print(my_function(1,2,3))
	print(my_function(1,2,'fish'))