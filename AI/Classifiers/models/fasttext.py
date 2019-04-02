import torch
from torch import nn

class FastText(nn.Module):
    def __init__(self, config, weights):
        super(FastText, self).__init__()
        self.config = config

        if self.config.PRETRAINED:
            self.embedding = nn.Embedding.from_pretrained(weights)
        else:
            self.embedding = nn.Embedding(config.EMBED_NUM, config.EMBED_DIM)

        linear_hidden_size = 10
        self.pre = nn.Sequential(
            nn.Linear(self.config.EMBED_DIM, linear_hidden_size),
            nn.BatchNorm1d(linear_hidden_size),
            nn.ReLU(inplace=True)
        )

        self.fc = nn.Sequential(
            nn.Linear(linear_hidden_size, self.config.CLASS_NUM)
        )

    def forward(self, inputs):
        # embed (batch, seq, embedding)
        embed = self.embedding(inputs)
        # mean_embed (batch, embedding)
        mean_embed = torch.mean(embed, dim=1).squeeze()
        # mean_embed (batch, embedding)
        mean_embed = mean_embed.view(-1, self.config.EMBED_DIM)
        # hidden_layer (batch, self.config["linear_hidden_size"])
        hidden_layer = self.pre(mean_embed)

        # out (batch, self.config["label_size"])
        out = self.fc(hidden_layer)
        return out
