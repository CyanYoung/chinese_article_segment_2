import torch.nn as nn


class Rnn(nn.Module):
    def __init__(self, embed_mat, bidirect, layer_num):
        super(Rnn, self).__init__()
        self.vocab_num, self.embed_len = embed_mat.size()
        self.feat_len = 400 if bidirect else 200
        self.embed = nn.Embedding(self.vocab_num, self.embed_len, _weight=embed_mat)
        self.ra = nn.LSTM(self.embed_len, 200, batch_first=True,
                          bidirectional=bidirect, num_layers=layer_num)
        self.dl = nn.Sequential(nn.Dropout(0.2),
                                nn.Linear(self.feat_len, 1))

    def forward(self, x):
        x = self.embed(x)
        x, h_n = self.ra(x)
        return self.dl(x)