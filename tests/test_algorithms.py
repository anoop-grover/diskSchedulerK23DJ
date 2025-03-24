import unittest
from src.algorithms import fcfs, sstf, scan, c_scan  # Importing all algorithms

class TestDiskScheduling(unittest.TestCase):

    def test_fcfs(self):
        """ Test FCFS Algorithm """
        requests = [98, 183, 37, 122, 14]
        head = 53
        expected_seek_time = 640  # Expected total seek time
        
        seek_sequence, seek_time = fcfs(requests, head)
        
        self.assertEqual(seek_sequence, [53, 98, 183, 37, 122, 14])
        self.assertEqual(seek_time, expected_seek_time)

    def test_sstf(self):
        """ Test SSTF Algorithm """
        requests = [98, 183, 37, 122, 14]
        head = 53
        seek_sequence, seek_time = sstf(requests, head)
        
        self.assertTrue(isinstance(seek_sequence, list))
        self.assertTrue(isinstance(seek_time, int))

    def test_scan(self):
        """ Test SCAN Algorithm """
        requests = [98, 183, 37, 122, 14]
        head = 53
        max_cylinder = 200
        
        seek_sequence, seek_time = scan(requests, head, max_cylinder)
        
        self.assertIn(200, seek_sequence)  # SCAN should go to max cylinder

    def test_cscan(self):
        """ Test C-SCAN Algorithm """
        requests = [98, 183, 37, 122, 14]
        head = 53
        max_cylinder = 200
        
        seek_sequence, seek_time = c_scan(requests, head, max_cylinder)
        
        self.assertIn(0, seek_sequence)  # C-SCAN should go to cylinder 0
        self.assertIn(200, seek_sequence)  # C-SCAN should go to max cylinder

if __name__ == '__main__':
    unittest.main()
