# Cotton Weed Detection - Competition Dataset

## Quick Start

### 📚 For Learning (Start Here)
1. **Download** this dataset from Kaggle
2. **Open** `cotton_weed_starter_notebook.ipynb`
3. **Follow** the step-by-step workflow to understand the concepts

### 🚀 For Fast Iteration (After Learning)
Once you understand the workflow, use the scripts for faster experimentation:
1. **Edit** `train.py` or `predict.py` configuration section
2. **Run** the script:
```bash
# Train model
python train.py

# Generate predictions
python predict.py

# Submit to Kaggle
# Upload submission.csv
```

## Overview

- **Task**: Multi-class weed detection (3 classes)
- **Format**: YOLO with normalized coordinates
- **Model**: YOLOv8n only (edge device constraints)
- **Focus**: Data-centric AI approach

## Dataset Structure

```
cotton_weed_competition_dataset/
├── train/                    # 542 training images + labels
├── val/                      # 133 validation images + labels
├── test/images/              # 170 test images (no labels)
├── dataset.yaml              # YOLO configuration
├── cotton_weed_starter_notebook.ipynb  # Interactive tutorial
├── train.py                  # Training script 
├── predict.py                # Prediction script
├── sample_submission.csv
└── README.md
```

## Classes

- **0**: Carpetweed - Mat-forming annual weed
- **1**: Morning Glory - Climbing vine
- **2**: Palmer Amaranth - Herbicide-resistant "super weed"

## Submission Format

CSV file with columns: `image_id,prediction_string`

**Prediction string**: Space-separated values for each detection:
```
class_id confidence x_center y_center width height
```

**Example**:
```csv
image_id,prediction_string
20190613_6062W_CM_29,0 0.95 0.5 0.3 0.2 0.4 1 0.87 0.7 0.6 0.15 0.25
20200624_iPhone6_SY_132,no box
```

**Requirements**:
- Column names must be lowercase
- Coordinates normalized to [0, 1]
- Use `no box` for images with no detections

## Competition Rules

### ✅ Allowed
- YOLOv8n model only (REQUIRED)
- Hyperparameter tuning and augmentation
- Data corrections and improvements
- 3 submissions per day

### ❌ Prohibited
- Larger models (YOLOv8s, YOLOv8m, etc.)
- Model ensembles or stacking
- Test-time augmentation (TTA)

### Why These Constraints?
Real edge devices have fixed computational, power, and thermal budgets. This competition simulates production constraints where hardware is deployed first, and improvements must come from data and training strategies.

## Getting Started

### Prerequisites
```bash
pip install 3lc-ultralytics 
3lc login <your_api_key>
3lc service  # Keep running in separate terminal
```

### Two Ways to Work

#### Option 1: Notebook (Recommended for Learning)
**Best for:** Understanding concepts, first-time users, visual learners

Start with `cotton_weed_starter_notebook.ipynb`:
- Interactive cells with explanations
- Visual examples and analysis
- Step-by-step guidance through the full pipeline
- Learn 3LC Dashboard workflows

**Workflow (3 Phases):**
1. **Setup** (30 min): Install dependencies, register dataset with 3LC
2. **Baseline** (60 min): Train YOLOv8n, generate predictions, submit
3. **Iterate** (ongoing): Analyze errors → Fix data → Retrain → Improve

#### Option 2: Scripts (Best for Iteration)
**Best for:** Fast experimentation, quick iterations, automation

Use `train.py` and `predict.py` after learning the concepts. Both scripts use **edit-in-place configuration**:

**Training:**
1. Open `train.py` in your editor
2. Edit the CONFIGURATION section:
```python
# 3LC Table URLs (get from Dashboard)
TRAIN_TABLE_URL = "your/train/table/url"
VAL_TABLE_URL = "your/val/table/url"

# Run configuration
RUN_NAME = "baseline_v1"  # Change for each experiment
EPOCHS = 30  # Number of training epochs
BATCH_SIZE = 16  # Batch size
USE_AUGMENTATION = False  # Set to True to enable augmentation
```
3. Run the script:
```bash
python train.py
```

**Prediction:**
1. Open `predict.py` in your editor
2. Edit the CONFIGURATION section:
```python
# Model weights path (from training)
MODEL_WEIGHTS = "runs/detect/baseline_v1/weights/best.pt"

# Inference settings
CONFIDENCE_THRESHOLD = 0  # Adjust as needed
OUTPUT_CSV = "submission.csv"  # Output file name
```
3. Run the script:
```bash
python predict.py
```

**No command-line arguments to remember!** Just edit the configuration and run.

### Which Should I Use?

| Scenario | Use |
|----------|-----|
| First time with competition | **Notebook** - Learn concepts |
| Understanding 3LC Dashboard | **Notebook** - Visual guides |
| Rapid training iterations | **Scripts** - Faster workflow |
| Testing hyperparameters | **Scripts** - Edit & run |
| Batch experiments | **Scripts** - Automation friendly |
| Team collaboration | **Both** - Notebook for onboarding, scripts for work |

**💡 Recommended:** Start with the notebook, switch to scripts once comfortable!

## Data-Centric AI Approach

Since the model is fixed, **all improvements come from data**:

1. Train baseline model
2. Use 3LC Dashboard to identify issues (missing labels, mislabels, bbox errors)
3. Fix data problems
4. Retrain with improved data
5. Submit and repeat

This mirrors real production AI where model capacity is constrained.

## Expected Performance

| Metric | Local (YOLO) | Kaggle (COCO) |
|--------|--------------|---------------|
| Baseline | 55-65% | 30-45% |
| Optimized | 70-85% | 45-65% |
| Top Score | 85%+ | 70%+ |

**Note**: Kaggle scores are 10-15% lower because COCO evaluation is stricter than YOLO's native validation.

## Common Issues

| Issue | Solution |
|-------|----------|
| Kaggle score much lower than local | Normal! COCO evaluation is stricter |
| CSV submission rejected | Check lowercase column names: `image_id,prediction_string` |
| Invalid coordinate range | Ensure all coordinates are in [0, 1] |
| Model not improving | Use 3LC Dashboard for error analysis - it's likely a data issue |

## Submission Guidelines

- **3 submissions per day** maximum
- Select **up to 2 final submissions** for judging
- Leaderboard: **50% public, 50% private** (prevents overfitting)
- Evaluation: **mAP@0.5** using COCO methodology

## Dataset Details

- **Training**: 542 images, ~2,000 weed instances
- **Validation**: 133 images, ~500 weed instances
- **Test**: 170 images (labels withheld)
- **Resolution**: 1024×768 to 4032×3024 pixels
- **Quality**: Intentional label imperfections (production reality)

## Script Features

Both `train.py` and `predict.py` are production-quality scripts with:

✅ **Edit-in-place configuration** - Modify settings at top of file  
✅ **Clear structure** - All options in one CONFIGURATION section  
✅ **Validation** - Checks formats and catches errors early  
✅ **Progress tracking** - Clear status messages throughout  
✅ **Safe operations** - Creates backups instead of deleting  
✅ **Modular code** - Easy to customize if needed  


## Resources

- **3LC Documentation**: https://docs.3lc.ai/
- **YOLOv8 Guide**: https://docs.ultralytics.com/
- **Competition Forum**: Ask questions, share insights

## License

Dataset provided for competition use. See official competition rules for complete terms.

---

**Ready to begin?** Open `cotton_weed_starter_notebook.ipynb` and follow the workflow! 🌾