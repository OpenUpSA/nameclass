#!.env/bin/flask

import pickle
from flask import Flask
from features import gen_features

app = Flask(__name__)


def load_classifier(filename):
    #logging.info("Loading model: %s" % filename)

    f = open(filename, 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

def get_classifier(modelfile, cache=True, use_classify_many=False):
    classifier = load_classifier(modelfile)
    cache_dict = {}

    def classify(name):
        name = name.upper()
        if name in cache_dict:
            return cache_dict[name]
        else:
            label = classifier.classify(gen_features(name))
            if cache:
                cache_dict[name] = label
            return label
    return classify

classify = get_classifier("models/race.model")

@app.route('/race/<name>')
def index(name):
    return classify(name)

if __name__ == '__main__':
    app.run(debug=True)
