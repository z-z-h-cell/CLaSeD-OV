_base_ = './base_config.py'

# model settings
model = dict(
    classname_path='./configs/cls_floodnet.txt',
    confidence_threshold=0.80,
    prob_thd=0.10,
)

# dataset settings
dataset_type = 'FloodNetDataset'
data_root = 'data/FlodNet'

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        reduce_zero_label=False,
        data_prefix=dict(
            img_path='val/val-org-img',
            seg_map_path='val/val-label-img'),
        pipeline=test_pipeline))
