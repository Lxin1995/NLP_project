import string
from nltk import word_tokenize   ##相当于word.split()
from nltk import WordNetLemmatizer   ##还原单词形式
from nltk.corpus import stopwords
import pickle


class BaseModel:
    def __init__(self):
        self.lematizer = WordNetLemmatizer()
        self.stop = stopwords.words('english')
        self.transtbl = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        self.model = None
        self.vec = None

    # Load Vec
    def load_vec(self, vec_path, mode='rb'):
        with open(vec_path, mode) as pkl_file:
            self.vec = pickle.load(pkl_file)    ##哦哦pickle是python自带的存储object的，NLP2里面讲了，mnb_model.pkl,tf_vec.pkl就是之前写好的两个function
                                                ##然后pickle.load()就可以再load进来，直接用就可以

    # Load Model
    def load_model(self, model_path, mode='rb'):
        with open(model_path, mode) as pkl_file:
            self.model = pickle.load(pkl_file)

    # Preprocessing
    def preprocessing(self, line: str) -> str:
        line = line.translate(self.transtbl)
        tokens = [self.lematizer.lemmatize(t.lower(), 'v')
                  for t in word_tokenize(line)
                  if t.lower() not in self.stop]
        return ' '.join(tokens)

    # Predict
    def predict(self, line):
        if not self.model or not self.vec:
            print('Model / Vec is not loaded')
            return ""

        line = self.preprocessing(line)
        features = self.vec.transform([line])
        return self.model.predict(features)[0]