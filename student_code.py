import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts # empty at first
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if fact.name == 'fact':
            self.facts.append(fact);

        # print(fact.name)
        # print(fact.statement)
        # print(fact.asserted)

        # print("Asserting {!r}".format(fact))
        # print(self.facts)
        # print(1)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        # print(self.facts)
        bindings = ListOfBindings()
        # print('bindings: ')
        # print(bindings)
        state1 = fact.statement
        # print('state1: ')
        # print(state1)
        for index in self.facts:
            # print('index: ')
            # print(index.statement)      
            state2 = index.statement
            match_result = match(state1, state2)
            if match_result != False:
                bindings.add_bindings(match_result)

                # bindings.add_bindings(match_result)
                # print('bindings 2 :')
                # print(bindings)
                # print('1111111')
                # print('bindings :')
                # print(bindings)
        if bindings == '':
            return False

        else:
            return bindings
          
        # print("Asking {!r}".format(fact))
