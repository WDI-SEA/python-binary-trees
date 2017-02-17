class QuestionNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class QuestionTree:
    def __init__(self):
        self.root = QuestionNode("hippo")
        
    def play_game(self):
        print("Welcome to 20 Questions.")
        self.play_game_helper(self.root)
        
    def play_game_helper(self, node):
        if node.left == None and node.right == None:
            print("You're thinking of:", node.data)
            response = input("y/n?")
            if response == "y":
                print("I win!!")
                return node
            else:
                # call a function that will insert a new question node
                return self.add_answer(node)
        else:
            print(node.data)
            response = input("y/n?")
            if response == "y":
                node.right = self.play_game_helper(node.right)
            elif response == "n":
                node.left = self.play_game_helper(node.left)
            else:
                # if someone put in bad in put just ask the question again.
                self.play_game_helper(node)
            return node
          
    # create a new node that adds a dis-ambiguiating question
    # and a new answer.
    def add_answer(self, node):
        print("TODO: implement a method that returns a node containing")
        print("TODO: a new question and answers on the bottom")
        question = input("enter your disambiguating question")
        yes_or_no = input("enter y/n for your question")
        # TODO: build up the node on the left or the right.
        new_node = QuestionNode("new node")
        return new_node
        
twenty_questions = QuestionTree()
twenty_questions.play_game()    
