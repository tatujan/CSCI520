import unittest

from dictionary import Dictionary
from add_entry_msg import AddEntryMsg
from vote_req_msg import RequestVoteMsg
from node import Node
from follower import Follower
from candidate import Candidate
from leader import Leader

class CandidateTest( unittest.TestCase ):

    def setUp( self ):
    	dict = Dictionary()
    	state = Follower()
    	self.node = Node( 0, state, [], dict, [] )

    	dict2 = Dictionary()
    	state2 = Candidate()
    	self.node2 = Node( 1, state2, [], dict2, [ self.node ] )
    	self.node2.neighbors.append( self.node2 )

    def test_candidate_node_initiated_election( self ):

    	self.assertEquals( 1, len( self.node.dictionary) )

    	self.node.rcvd_msg(self.node.dictionary.rcvd_msg())

    	self.assertEquals( 1, len( self.node2.dictionary) )
    	self.assertEquals( True, self.node2.dictionary.rcvd_msg().content["response"])
