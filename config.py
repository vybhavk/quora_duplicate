# -*- coding: utf-8 -*-
"""Model configs.
"""
import os


class DirConfig(object):
    DEBUG = 0
    W2V_FILE = '../embeddings/GoogleNews-vectors-negative300.bin'
    GLOVE_FILE = '../embeddings/glove.840B.300d.txt'
    BASE_DIR = '../'
    DATA_DIR = '../dataset/'
    TRAIN_FILE = DATA_DIR + 'train.csv'
    TEST_FILE = DATA_DIR + 'test.csv'
    TRAIN_FEATURES_FILE = DATA_DIR + 'train_xgb_features.csv'
    TEST_FEATURES_FILE = DATA_DIR + 'test_xgb_features.csv'
    SAMPLE_TRAIN_FILE = DATA_DIR + 'sample_train.csv'
    SAMPLE_TEST_FILE = DATA_DIR + 'sample_test.csv'
    SAMPLE_TRAIN_FEATURES_FILE = DATA_DIR + 'sample_train_xgb_features.csv'
    SAMPLE_TEST_FEATURES_FILE = DATA_DIR + 'sample_test_xgb_features.csv'
    HISTORYA_DIR = os.path.join(BASE_DIR, 'history')
    SUBM_DIR = '../subm/'
    Q1_CACHE_TRAIN = '../dataset/cache_train_q1.npy'
    Q2_CACHE_TRAIN = '../dataset/cache_train_q2.npy'
    Q1_CACHE_TEST = '../dataset/cache_test_q1.npy'
    Q2_CACHE_TEST = '../dataset/cache_test_q2.npy'
    CHAR1_CACHE_TRAIN = '../dataset/cache_train_char1.npy'
    CHAR2_CACHE_TRAIN = '../dataset/cache_train_char2.npy'
    CHAR1_CACHE_TEST = '../dataset/cache_test_char1.npy'
    CHAR2_CACHE_TEST = '../dataset/cache_test_char2.npy'
    CHAR_INDEX_CACHE = '../dataset/char_index.npy'
    W2V_CACHE = '../dataset/w2v_matrix.npy'
    GLOVE_CACHE = '../dataset/glove_matrix.npy'
    WORD_INDEX_CACHE = '../dataset/word_index.npy'
    TARGETS_CACHE = '../dataset/cache_targets.npy'
    TEST_ID_CACHE = '../dataset/cache_test_id.npy'


class TrainConfig(object):
    TEST_SIZE = 0.1
    RE_WEIGHT = True
    BATCH_SIZE = 1024
    NB_EPOCH = 5 if DirConfig.DEBUG else 50
    CLASS_WEIGHT = {0: 1.0, 1: 1.708574797505075}
    SHARE_RNN = 1
    USE_CHAR = 0
    REMOVE_STOPWORDS = 0
    USE_STEM = 0
    W2V_TYPE = 'word2vec'
    KFOLD = 1
    MAX_SEQUENCE_LENGTH = 40
    MAX_NB_WORDS = 200000
    WORD_EMBEDDING_DIM = 300
    MAX_NB_CHARS = 50
    MAX_CHAR_PER_WORD = 10
    CHAR_EMBEDDING_DIM = 20
    CHAR_LSTM_DIM = 50
    VALIDATION_SPLIT = 0.1


class TestConfig(object):
    RE_WEIGHT = True
    BATCH_SIZE = 1024
    CLASS_WEIGHT = {0: 1.309028344, 1: 0.472001959}


class BasicRnnConfig(object):
    SEED = 2017 + 1
    MODEL = 'BasicRNN'
    RNN_UNIT = 'gru'
    TRIAL = 4
    BASE_DIR = '../models/'
    RNN_DIM = 225
    DENSE_DIM = 125
    DROP_RATE = 0.2
    ACT = 'relu'
    RNN_DIM_LAYER = 1
    CHECKPOINT = '../checkpoint/{}_trial_{}_db_{}.h5'.format(MODEL, TRIAL, DirConfig.DEBUG)
    INFO = '%s_%s_lstm_%d_layer_%d_dense_%d_shareRNN_%d_drop_%.2f_char_%d_k_%d' % \
            (MODEL, RNN_UNIT, RNN_DIM, RNN_DIM_LAYER, DENSE_DIM, TrainConfig.SHARE_RNN,
             DROP_RATE, TrainConfig.USE_CHAR, TrainConfig.KFOLD)


class AttentionConfig(object):
    SEED = 2017 + 7
    MODEL = 'decomposable'
    RNN_UNIT = 'gru'
    TRIAL = 7
    BASE_DIR = '../models/'
    CONTEXT_LSTM_DIM = 200
    DENSE_DIM = 100
    DROP_RATE = 0.2
    ACT = 'relu'
    CHECKPOINT = '../checkpoint/{}_trial_{}_db_{}.h5'.format(MODEL, TRIAL, DirConfig.DEBUG)
    INFO = '%s_%s_context_%d_dense_%d_drop_%.2f_char_%d_k_%d' % \
            (MODEL, RNN_UNIT, CONTEXT_LSTM_DIM, DENSE_DIM,
             DROP_RATE, TrainConfig.USE_CHAR, TrainConfig.KFOLD)


class CompareAggreConfig(object):
    SEED = 2017 + 7
    MODEL = 'compare_aggregate'
    RNN_UNIT = 'gru'
    TRIAL = 7
    BASE_DIR = '../models/'
    CONTEXT_LSTM_DIM = 200
    DENSE_DIM = 100
    DROP_RATE = 0.2
    ACT = 'relu'
    CHECKPOINT = '../checkpoint/{}_trial_{}_db_{}.h5'.format(MODEL, TRIAL, DirConfig.DEBUG)
    INFO = '%s_%s_context_%d_dense_%d_drop_%.2f_char_%d_k_%d' % \
            (MODEL, RNN_UNIT, CONTEXT_LSTM_DIM, DENSE_DIM,
             DROP_RATE, TrainConfig.USE_CHAR, TrainConfig.KFOLD)


class ResDistanceConfig(object):
    SEED = 2017 + 4
    MODEL = 'ResDistance'
    RNN_UNIT = 'lstm'
    TRIAL = 1
    BASE_DIR = '../models/'
    CONTEXT_LSTM_DIM = 100
    AGGREGATION_LSTM_DIM = 100
    DENSE_DIM = 100
    RATE_DROP_REPRES = 0.2
    DROP_RATE = 0.2
    WITH_HIGHWAY = 0
    USE_CHAR = 0
    CHECKPOINT = '../checkpoint/{}_trial_{}_db_{}.h5'.format(MODEL, TRIAL, DirConfig.DEBUG)
    INFO = '%s_rnn_%s_seq_%d_context_%d_aggreg_%d_highway_%d_shareRNN_%d_drop_%.2f_char_%d' % \
            (MODEL, RNN_UNIT, TrainConfig.MAX_SEQUENCE_LENGTH, CONTEXT_LSTM_DIM, AGGREGATION_LSTM_DIM,
             WITH_HIGHWAY, TrainConfig.SHARE_RNN, DROP_RATE, TrainConfig.USE_CHAR)
