import torch
from ast_dataset import ASTDataset
from collate import collate_fn

from torch.utils.data import random_split
from torch.utils.data import DataLoader

from ast_dataset import ASTDataset

dataset = ASTDataset(
    protocol_file="ml/asvspoof/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt",
    audio_folder="ml/asvspoof/ASVspoof2019_LA_train/flac"
)

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_dataset, val_dataset = random_split(
    dataset,
    [train_size, val_size]
)

train_loader = DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True,
    collate_fn=collate_fn
)

val_loader = DataLoader(
    val_dataset,
    batch_size=4,
    shuffle=False,
    collate_fn=collate_fn
)

print("Train Samples :", len(train_dataset))
print("Validation Samples :", len(val_dataset))

from transformers import ASTForAudioClassification

print("\nLoading AST Model...")

model = ASTForAudioClassification.from_pretrained(
    "MIT/ast-finetuned-audioset-10-10-0.4593",
    num_labels=2,
    ignore_mismatched_sizes=True
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model.to(device)

print("Device :", device)

print("Model Loaded Successfully!")

from torch.optim import AdamW

optimizer = AdamW(
    model.parameters(),
    lr=2e-5
)

loss_fn = torch.nn.CrossEntropyLoss()

print("\nOptimizer Ready")
print("Loss Function Ready")

from transformers import get_linear_schedule_with_warmup

epochs = 3

total_training_steps = len(train_loader) * epochs

scheduler = get_linear_schedule_with_warmup(
    optimizer,
    num_warmup_steps=0,
    num_training_steps=total_training_steps
)

print("Scheduler Ready")
print("Total Training Steps :", total_training_steps)

print("\nCUDA Available :", torch.cuda.is_available())

if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
else:
    print("Running on CPU")

    trainable = sum(
    p.numel()
    for p in model.parameters()
    if p.requires_grad
)

print("Trainable Parameters :", trainable)

print("\n==============================")
print("Starting AST Training...")
print("==============================\n")

best_accuracy = 0.0

for epoch in range(epochs):

    # -------------------- TRAIN --------------------

    model.train()

    train_loss = 0
    train_correct = 0
    train_total = 0

    for batch in train_loader:

        input_values = batch["input_values"].to(device)
        labels = batch["label"].to(device)

        optimizer.zero_grad()

        outputs = model(
            input_values=input_values,
            labels=labels
        )

        loss = outputs.loss
        logits = outputs.logits

        loss.backward()

        optimizer.step()

        scheduler.step()

        train_loss += loss.item()

        predictions = torch.argmax(logits, dim=1)

        train_correct += (predictions == labels).sum().item()
        train_total += labels.size(0)

    train_accuracy = 100 * train_correct / train_total

    # -------------------- VALIDATION --------------------

    model.eval()

    val_loss = 0
    val_correct = 0
    val_total = 0

    with torch.no_grad():

        for batch in val_loader:

            input_values = batch["input_values"].to(device)
            labels = batch["label"].to(device)

            outputs = model(
                input_values=input_values,
                labels=labels
            )

            loss = outputs.loss
            logits = outputs.logits

            val_loss += loss.item()

            predictions = torch.argmax(logits, dim=1)

            val_correct += (predictions == labels).sum().item()
            val_total += labels.size(0)

    val_accuracy = 100 * val_correct / val_total

    print("-" * 50)
    print(f"Epoch {epoch + 1}/{epochs}")
    print(f"Train Loss       : {train_loss:.4f}")
    print(f"Train Accuracy   : {train_accuracy:.2f}%")
    print(f"Validation Loss  : {val_loss:.4f}")
    print(f"Validation Acc   : {val_accuracy:.2f}%")

    if val_accuracy > best_accuracy:

        best_accuracy = val_accuracy

        torch.save(
            model.state_dict(),
            "ml/model/ast_best_model.pth"
        )

        print("✅ Best Model Saved")

print("\n==============================")
print("Training Completed")
print("==============================")
print(f"Best Validation Accuracy : {best_accuracy:.2f}%")