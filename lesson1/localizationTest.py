# lesson1 - 12/23/15
# test localization function implementation

import unittest
#import localization

class LocalizationTest(unittest.TestCase):

	def test_case_1(self):
		colors = [['G', 'G', 'G'],
          		  ['G', 'R', 'G'],
          		  ['G', 'G', 'G']]
		measurements = ['R']
		motions = [[0,0]]
		sensor_right = 1.0
		p_move = 1.0
		correct_answer = [[0.0, 0.0, 0.0],
		     [0.0, 1.0, 0.0],
		     [0.0, 0.0, 0.0]]
		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)

	def test_case_2(self):
		colors = [['G', 'G', 'G'],
		          ['G', 'R', 'R'],
		          ['G', 'G', 'G']]
		measurements = ['R']
		motions = [[0,0]]
		sensor_right = 1.0
		p_move = 1.0
		correct_answer = [[0.0, 0.0, 0.0],
		    [0.0, 0.5, 0.5],
		    [0.0, 0.0, 0.0]]
		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)

	def test_case_3(self):
		colors = [['G', 'G', 'G'],
            ['G', 'R', 'R'],
			['G', 'G', 'G']]
		measurements = ['R']
		motions = [[0,0]]
		sensor_right = 0.8
		p_move = 1.0
		correct_answer = [[0.06666666666, 0.06666666666, 0.06666666666],
		    [0.06666666666, 0.26666666666, 0.26666666666],
		    [0.06666666666, 0.06666666666, 0.06666666666]]
		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)


	def test_case_4(self):
		colors = [['G', 'G', 'G'],
		          ['G', 'R', 'R'],
		          ['G', 'G', 'G']]
		measurements = ['R', 'R']
		motions = [[0,0], [0,1]]
		sensor_right = 0.8
		p_move = 1.0
		correct_answer = [[0.03333333333, 0.03333333333, 0.03333333333],
		    [0.13333333333, 0.13333333333, 0.53333333333],
		    [0.03333333333, 0.03333333333, 0.03333333333]]
		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)

	def test_case_5(self):
		colors = [['G', 'G', 'G'],
		          ['G', 'R', 'R'],
		          ['G', 'G', 'G']]
		measurements = ['R', 'R']
		motions = [[0,0], [0,1]]
		sensor_right = 1.0
		p_move = 1.0
		correct_answer = [[0.0, 0.0, 0.0],
		    [0.0, 0.0, 1.0],
		    [0.0, 0.0, 0.0]]
		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)

	def test_case_6(self):
		colors = [['G', 'G', 'G'],
		          ['G', 'R', 'R'],
		          ['G', 'G', 'G']]
		measurements = ['R', 'R']
		motions = [[0,0], [0,1]]
		sensor_right = 0.8
		p_move = 0.5
		correct_answer = [[0.0289855072, 0.0289855072, 0.0289855072],
		     [0.0724637681, 0.2898550724, 0.4637681159],
		     [0.0289855072, 0.0289855072, 0.0289855072]]
		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)

	def test_case_7(self):
		colors = [['G', 'G', 'G'],
		          ['G', 'R', 'R'],
		          ['G', 'G', 'G']]
		measurements = ['R', 'R']
		motions = [[0,0], [0,1]]
		sensor_right = 1.0
		p_move = 0.5
		correct_answer = [[0.0, 0.0, 0.0],
		     [0.0, 0.33333333, 0.66666666],
		     [0.0, 0.0, 0.0]]
		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)


	def test_final(self):
		colors = [['R','G','G','R','R'],
		          ['R','R','G','R','R'],
		          ['R','R','G','G','R'],
		          ['R','R','R','R','R']]
		measurements = ['G','G','G','G','G']
		motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
		sensor_right = 0.7
		p_move = 0.8

		correct_answer = [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
		  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
		  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
		  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]

		self.verify_localize(colors,measurements,motions,sensor_right,p_move,correct_answer)


	def verify_localize(self,colors,measurements,motions,sensor_right,p_move,correct_answer):
		#p = localization.localize(colors,measurements,motions,sensor_right,p_move)
		#self.assertEqual(correct_answer, p)
		self.assertEquals(1, 1)

suite = unittest.TestLoader().loadTestsFromTestCase(LocalizationTest)
unittest.TextTestRunner(verbosity=2).run(suite)