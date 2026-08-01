# Audio Configuration
SAMPLE_RATE = 16000
N_MELS = 128
N_FFT = 1024
HOP_LENGTH = 512

# Training Configuration
IMAGE_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 20
LEARNING_RATE = 0.0001

# Classes
NUM_CLASSES = 2

# Labels
REAL = 0
FAKE = 1

# AST Configuration
MODEL_NAME = "MIT/ast-finetuned-audioset-10-10-0.4593"

TRAIN_PROTOCOL = "ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"

TRAIN_AUDIO = "ml/asvspoof/ASVspoof2019_LA_train/flac"

MODEL_SAVE = "ml/models/best_ast_model.pth"