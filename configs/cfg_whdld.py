_base_ = './base_config.py'

# model settings
model = dict(
    classname_path='./configs/cls_whdld.txt',
    confidence_threshold=0.5,
    prob_thd=0.10,
    bg_idx=255,
)

# dataset settings
dataset_type = 'WHDLDDataset'
data_root = 'data/WHDLD'

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
        # Official WHDLD labels are 1..6 with no background pixels in GT.
        reduce_zero_label=True,
        data_prefix=dict(
            img_path='Images',
            seg_map_path='Labels'),
        pipeline=test_pipeline))
