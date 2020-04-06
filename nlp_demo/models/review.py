from models.base import BaseModel



class ReviewModel(BaseModel):
    def __init__(self):
        super().__init__()  ##调用父类函数
        self.load_vec('models/tf_vec.pkl')
        self.load_model('models/mlp_model.pkl')

    def predict(self, line, highlight=True):
        sentiment = super(ReviewModel, self).predict(line)    ##第一个就是写子类（菜鸟教程）
        # highlight words, hack
        if highlight:
            highlight_words = \
                [w for w in self.preprocessing(line).split()
                 if super(ReviewModel, self).predict(w) == sentiment]
            return sentiment, highlight_words    ##我明白了，这个地方return highlight_words应该是想在web上hightlight那些重点单词（标黄）
        else:
            return sentiment



