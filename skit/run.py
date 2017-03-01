import parser
import tagger
import dataReader

def main():
	sv_tags = ["<ROOT>", "ADJ", "ADP", "ADV", "AUX", "CONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB"]
	en_tags = ["<ROOT>", "ADJ", "ADP", "ADV", "AUX", "CONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X"]
		
	n_examples = 2000
	sv_train_file = "sv_train.conllu"
	sv_test_file = "sv_dev.conllu"
	en_train_file = "en_train"
	en_test_file = "en_dev.conllu"
	myTagger = tagger.Tagger(sv_tags)
	myParser = parser.Parser(myTagger)
	dataReader.evaluate(sv_train_file, sv_test_file, myParser)

if __name__ == '__main__':
	main()