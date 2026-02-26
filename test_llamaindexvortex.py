# test_llamaindexvortex.py
"""
Tests for LlamaindexVortex module.
"""

import unittest
from llamaindexvortex import LlamaindexVortex

class TestLlamaindexVortex(unittest.TestCase):
    """Test cases for LlamaindexVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LlamaindexVortex()
        self.assertIsInstance(instance, LlamaindexVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LlamaindexVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
