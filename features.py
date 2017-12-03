import logging
import os
from glob import glob
from collections import Counter

logger = logging.getLogger(__name__)

def fix_name_extensions(name):
    name = name.replace("-", " ")
    name = name.replace(" JANSE VAN RENSBURG ", " JANSEVANRENSBURG")
    name = name.replace(" VAN DER ", " VANDER")
    name = name.replace(" VAN DEN ", " VANDEN")
    name = name.replace(" VAN ", " VAN")
    name = name.replace(" VON ", " VON")
    name = name.replace(" DU ", " DU")
    name = name.replace(" DE ",  " DE")
    name = name.replace(" DA ",  " DA")
    return name

def gen_ngrams(name, n):
    ngrams = []
    for name_part in name.split():
        word_ngrams = [name_part[i:i + n] for i in range(len(name_part) - n + 1)]
        if len(name_part) >= n:
            first = "b_" + word_ngrams[0]
            last = "l_" + word_ngrams[-1]
            word_ngrams += [first, last]
        ngrams += word_ngrams
    return ngrams

def gen_features(name, include_name_part=False, include_bigrams=True, include_trigrams=True, include_4grams=True, include_surname=False, include_fullname=False):
    def generate_ngrams(token):
        features = []
        if include_bigrams:
            if len(token) > 3:
                total_bigrams = gen_ngrams(token, 2)
                if len(total_bigrams) < 3:
                    features.append("length_short")
                features.extend(total_bigrams)
        if include_trigrams:
            if len(token) > 4:
                total_trigrams = gen_ngrams(token, 3)
                features.extend(total_trigrams)
        if include_4grams:
            if len(token) > 5:
                total_quadgrams = gen_ngrams(token, 4)
                features.extend(total_quadgrams)
        return features

    name = name.upper()
    fixed_name = fix_name_extensions(name)
    features = []
    for n in fixed_name.split():
        features.extend(generate_ngrams(n))
        if include_name_part:
            features.append("namepart_" + n)

        try:
	    if include_surname:
                surname = fixed_name.split()[-1]
                surname_features = generate_ngrams(surname)
                features += ["s_" + f for f in surname_features]
		features.append("surname_" + surname)
        except IndexError:
            logger.warn("No surname found: %s" % name)

    if include_fullname:
        features.append("name_" + name.replace(" ", "_"))

    return Counter(features)
