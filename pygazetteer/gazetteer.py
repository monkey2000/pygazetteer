#!/usr/bin/env python3
from ahocorasick import Automaton
import os

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'gaze.txt')

class Gazetteer:
    def __init__(self, gaze_file=data_path):
        self.locations = {}
        self.vocab_to_location = {}
        self.automaton = Automaton()

        with open(gaze_file) as cin:
            self.load_gazes(cin)
        
        self.automaton.make_automaton()

    
    def load_gazes(self, cin):
        for line in cin:
            line = line.split('\t')
            line[-1] = line[-1].rstrip()
            self.locations[line[0]] = tuple(line)

            for vocab in line[3:]:
                if vocab in self.vocab_to_location:
                    self.vocab_to_location[vocab].append(line[0])
                else:
                    self.vocab_to_location[vocab] = [line[0]]
       
        for vocab, value in self.vocab_to_location.items():
            self.automaton.add_word(vocab, tuple(value))


    def match(self, string):
        ret = {}

        for end_index, value in self.automaton.iter(string):
            for lid in value:
                if lid in ret:
                    ret[lid] = (ret[lid][0], ret[lid][1]+1)
                else:
                    ret[lid] = (self.locations[lid], 1)

        return ret

if __name__ == '__main__':
    a = Gazetteer()
    print(a.match('诶，连任也要按照香港的法律啊，对不对？要要……要按照香港的……当然我们的决定权也是很重要的。香港的特区……特别行政区是属于中国……人民共和（中华人民共和国）的中央人民政府啊。啊？到那个时候我们会表态的！'))
    print(a.match('U.S. President Donald Trump’s warm words for Chinese President Xi Jinping as a “good man” will reassure Beijing that he finally understands the importance of good ties but risk leaving America’s allies in the region puzzling over where they fit into the new order.'))
